import sys

from PySide6 import QtWidgets

from connection import Connection
from services.parsing import Parser
from services.parsing_thread import ParserThread
from services.styles import style_parse_button, style_stop_button, style_checkbox
from ui import main_window_ui, settings_albums_window_ui, settings_wall_window_ui


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.conn = Connection()
        self.token = self.conn.get_token()

        self.parser = Parser(token=self.token)

        self.wall_photos_count = {
            "type": "Все",
            "count": "",
        }
        self.checked_albums = {}
        self.albums_size = 0
        self.total_count = 0

        self.ui = main_window_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.check_box_wall.checkStateChanged.connect(
            lambda: self.change_settings_button_state(self.ui.check_box_wall, self.ui.button_wall_settings)
        )
        self.ui.check_box_album.checkStateChanged.connect(
            lambda: self.change_settings_button_state(self.ui.check_box_album, self.ui.button_album_settings)
        )

        self.ui.line_edit_token.setText(self.conn.get_token())
        self.ui.line_edit_client_id.setText(self.conn.get_client_id())

        app_url = '1. Перейдите на <a href=\"https://dev.vk.com/ru/admin/apps-list\" style="color:blue">страницу управления приложениями</a>.'
        self.ui.label_step_1.setText(app_url)
        self.ui.label_step_1.setOpenExternalLinks(True)

        self.ui.button_get_token.clicked.connect(lambda: self.parser.get_token_url(self.ui.line_edit_client_id))
        self.ui.button_save.clicked.connect(self.save_token_data)

        self.ui.button_wall_settings.clicked.connect(self.open_wall_settings_window)
        self.ui.button_album_settings.clicked.connect(self.open_album_settings_window)
        self.ui.button_select_path.clicked.connect(self.select_path)

        self.ui.button_parse.clicked.connect(self.parse_photos)

        self.check_token()

    def change_settings_button_state(
        self, 
        checkbox: QtWidgets.QCheckBox, 
        button: QtWidgets.QPushButton
    ):
        """ В зависимости от состояния чекбокса делает кнопку активной или неактивной
        """

        if checkbox.isChecked():
            button.setEnabled(True)
        else:
            button.setEnabled(False)

    def check_token(self):
        """ Проверяет действительность токена и выводит соответствующее сообщение
        Для проверки токена делается тестовый запрос к VK API
        """

        is_true_token = self.parser.check_token_url(self.token)

        if is_true_token:
            self.parser = Parser(self.token)
            self.ui.label_token_info.setText("\u2705 Токен действителен")
            self.ui.label_token_info.setStyleSheet("color: green")
            self.ui.params_tabwidget.setTabText(1, "\u2705 Авторизация")
        else:
            self.ui.label_token_info.setText("\u274C Токен не действителен!")
            self.ui.label_token_info.setStyleSheet("color: red")
            self.ui.params_tabwidget.setTabText(1, "\u274C Авторизация")
 
    def save_token_data(self):
        """ Сохраняет токен и ID приложения в базу данных, при этом в базе
        гарантированно хранится только одна запись с данными
        После сохранения токен проверяется на действительность
        """

        client_id = self.ui.line_edit_client_id.text()
        self.token = self.ui.line_edit_token.text()
        self.conn.update_client_id(client_id)
        self.conn.update_token(self.token)

        self.check_token()

    def select_path(self):
        """ Открывает окно выбора папки для загрузки фотографий
        """

        path = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "Выберите папку для загрузки"
        )
        self.ui.line_edit_select_path.setText(path)

    def open_wall_settings_window(self):
        """ Открывает окно с настройками загрузки фотографий со стены при условии,
        что действителен ID группы, введённый в поле group_id, что проверяется
        с помощью тестового запроса к VK API
        """

        self.wall_window = QtWidgets.QDialog()
        self.wall_ui = settings_wall_window_ui.Ui_Dialog()
        self.wall_ui.setupUi(self.wall_window)

        group_id = self.ui.line_edit_group_id.text()
        if self.parser.check_group_id(group_id):
            self.wall_window.show()

            self.wall_ui.label_count.setText(self.parser.get_total_photos(self.ui.line_edit_group_id))

            self.wall_ui.combo_box_select_photos.setCurrentText(self.wall_photos_count["type"])
            self.wall_ui.line_edit_count.setText(self.wall_photos_count["count"])

            self.wall_ui.combo_box_select_photos.currentTextChanged.connect(self.get_wall_settings)
            self.wall_ui.button_save.clicked.connect(self.save_wall_settings)

            self.change_count_line_edit_state()

        else:
            QtWidgets.QMessageBox.critical(
                self,
                "Ошибка ID группы",
                "Проверьте правильность введённого ID группы и действительность токена",
                buttons=QtWidgets.QMessageBox.Ok,
                defaultButton=QtWidgets.QMessageBox.Ok,
            )

    def get_wall_settings(self):
        """ Получает параметры настройки количества загружаемых со стены фотографий
        Если в ComboBox были выбраны поля "Последние" или "Первые" то для ввода
        количества фотографий становится доступен виджет lineEdit  
        """

        self.wall_photos_count["type"] = self.wall_ui.combo_box_select_photos.currentText()
        self.change_count_line_edit_state()

    def change_count_line_edit_state(self):
        """ Делает активным поле ввода при выборе количества загружаемых
        со стены фотографий и неактивным при выборе загрузки всех фотографий
        """

        if self.wall_photos_count["type"] == "Последние" or self.wall_photos_count["type"] == "Первые":
            self.wall_ui.line_edit_count.setEnabled(True)
        else:
            self.wall_ui.line_edit_count.setDisabled(True)

    def save_wall_settings(self):
        """ Сохраняет выбор количества загружаемых со стены фотографий
        """

        if self.wall_ui.line_edit_count.isEnabled():
            self.wall_photos_count["count"] = self.wall_ui.line_edit_count.text()

            if not self.wall_photos_count["count"].isdigit():
                frame = self.wall_ui.wall_frame
                info_label = QtWidgets.QLabel(frame)
                info_label.setText("Введённое значение должно быть числом")
                info_label.setStyleSheet("color: red")
                info_label.setGeometry(10, 10, 200, 300)

                return

        self.wall_window.close()

    def open_album_settings_window(self):
        """ Открывает окно с настройками загрузки альбома.
        Получает список всех альбомов группы и генерирует чекбоксы с их
        названиями для выбора
        """

        self.album_window = QtWidgets.QDialog()
        self.album_ui = settings_albums_window_ui.Ui_Dialog()
        self.album_ui.setupUi(self.album_window)

        group_id = self.ui.line_edit_group_id.text()
        if self.parser.check_group_id(group_id):
            self.album_window.show()

            group_id = int(self.ui.line_edit_group_id.text())
            albums = self.parser.get_albums(group_id)

            checkboxes_albums_list = []
            for name in albums.keys():
                checkboxes_albums_list.append(name)

            layout = self.album_ui.layout
            scroll_widget = self.album_ui.scrollAreaWidgetContents
            scroll_area = self.album_ui.scrollArea

            scroll_area.setWidgetResizable(True)
            scroll_area.setWidget(scroll_widget)
            layout = QtWidgets.QVBoxLayout(scroll_widget)

            checkboxes = []
            num = 1
            for value in checkboxes_albums_list:
                checkbox = QtWidgets.QCheckBox(value)

                album_id = albums[checkbox.text()]["id"]

                if album_id in self.checked_albums:
                    checkbox.setChecked(True)

                checkbox.setObjectName(f"checkbox_album_{num + 1}")
                checkbox.setStyleSheet(style_checkbox)
                layout.addWidget(checkbox)
                checkboxes.append(checkbox)
                num += 1
            layout.addStretch(1)

            self.album_ui.button_save.clicked.connect(
                lambda: self.save_albums_settins(checkboxes, albums)
            )

        else:
            QtWidgets.QMessageBox.critical(
                self,
                "Ошибка ID группы",
                "Проверьте правильность введённого ID группы",
                buttons=QtWidgets.QMessageBox.Ok,
                defaultButton=QtWidgets.QMessageBox.Ok,
            )

    def save_albums_settins(self, checkboxes: list, albums: dict):
        """ Сохраняет в атрибует checked_albums словарь с ID и названиями выбранных
        альбомов, и увеличивает величину атрибута albums_size на общее количество
        фотофий в выбранных альбомах
        """

        for checkbox in checkboxes:
            if checkbox.isChecked():
                self.checked_albums[albums[checkbox.text()]["id"]] = albums[checkbox.text()]["title"]
                self.albums_size += albums[checkbox.text()]["size"]

        self.album_window.close()

    def parse_photos(self):
        """ Парсит фотографии в соответствии с переданными параметрами
        """

        path = self.ui.line_edit_select_path.text()
        group_id = int(self.ui.line_edit_group_id.text())
        token = self.conn.get_token()
        checkbox_wall = self.ui.check_box_wall.isChecked()
        checkbox_album = self.ui.check_box_album.isChecked()
        checked_albums = self.checked_albums
        total_photos = self.parser.get_total_photos(self.ui.line_edit_group_id)

        try:
            count = int(self.wall_photos_count["count"])
        except ValueError:
            count = total_photos

        if checkbox_wall:
            self.total_count += int(count)
        if checkbox_album:
            self.total_count += int(self.albums_size) 

        offset = None

        if self.wall_photos_count["type"] == "Последние":
            offset = int(total_photos) - int(count)

        self.parser_thread = ParserThread(
            checkbox_wall,
            checkbox_album,
            token,
            group_id,
            path,
            count,
            offset,
            checked_albums
        )
        self.parser_thread.progress_signal.connect(self.update_parsing_info)
        self.parser_thread.finished_signal.connect(self.is_finish_parsing)
        self.parser_thread.start()

        self.ui.button_parse.setText("Стоп")
        self.ui.button_parse.setStyleSheet(style_stop_button)
        self.ui.button_parse.clicked.disconnect(self.parse_photos)
        self.ui.button_parse.clicked.connect(self.stop_parsing)
     
    def update_parsing_info(self, value: int) -> None:
        """ Выводит сообщение о процессе загрузки
        """

        self.ui.label_info.setText("Идёт загрузка: " + str(value) + "/" + str(self.total_count))

    def stop_parsing(self):
        """ Останавливает парсинг фотографий и выводит соответствующее сообщение
        """

        self.parser_thread.terminate()
        self.ui.label_info.setText("Загрузка остановлена!")

        self.ui.button_parse.setText("Скачать")
        self.ui.button_parse.setStyleSheet(style_parse_button)
        self.ui.button_parse.clicked.disconnect(self.stop_parsing)
        self.ui.button_parse.clicked.connect(self.parse_photos)

    def is_finish_parsing(self):
        """ Выводит сообщение об успешном окончании загрузки
        """

        self.ui.label_info.setText("Загрузка успешно завершена!")

        self.ui.button_parse.setText("Скачать")
        self.ui.button_parse.setStyleSheet(style_parse_button)
        self.ui.button_parse.clicked.disconnect(self.stop_parsing)
        self.ui.button_parse.clicked.connect(self.parse_photos) 


def main():
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
