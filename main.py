import vk_api
import os
import sys
import urllib.request
import ssl 
import requests
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from connection import Connection
from parsing import Parser
from ui.main_window_ui import Ui_MainWindow
from ui import change_token_window_ui, setting_album_window_ui, setting_wall_window_ui


class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.conn = Connection()
        self.token = self.conn.get_token()
        
        self.parser = Parser(token=self.token)
        
        self.vk_session = vk_api.VkApi(token=self.token)
        self.vk = self.vk_session.get_api()
        
        self.count = 0
        self.offset = 0
        self.amount = 0
        self.selected_amount = None
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.button_add_token.clicked.connect(self.open_token_window)
        self.ui.button_setting_wall.clicked.connect(self.open_wall_settings_window)
        self.ui.button_setting_album.clicked.connect(self.open_album_settings_window)
        self.ui.button_select_path.clicked.connect(self.select_path)
        
        self.check_token()
        
    def open_token_window(self):
        """ Открывает окно настройки токена
        """
        
        self.token_window = QtWidgets.QDialog()
        self.token_ui = change_token_window_ui.Ui_Dialog()
        self.token_ui.setupUi(self.token_window)
        self.token_window.show()
        
        self.token_ui.line_edit_token.setText(self.conn.get_token())
        self.token_ui.line_edit_client_id.setText(self.conn.get_client_id())
        
        app_url = "1. Перейдите на <a href=\"https://dev.vk.com/ru/admin/apps-list\" style='color:blue'>страницу управления приложениями</a>."
        self.token_ui.label_step_1.setText(app_url)
        self.token_ui.label_step_1.setOpenExternalLinks(True)
        
        self.token_ui.button_get_token.clicked.connect(lambda: self.parser.get_token_url(self.token_ui.line_edit_client_id))
        self.token_ui.button_save.clicked.connect(self.save_token_data)
        
    def check_token(self):
        """ Проверяет действительность токена и выводит соответствующее сообщение
        Для проверки токена делается тестовый запрос к VK API
        """
        
        is_true_token = self.parser.check_token_url(self.token)
        
        if is_true_token:
            self.ui.label_token_info.setText("\u2713 Токен действителен")
            self.ui.label_token_info.setStyleSheet('color: green')
        else:
            self.ui.label_token_info.setText("\u2717 Токен не действителен!")
            self.ui.label_token_info.setStyleSheet('color: red')    

    def save_token_data(self):
        """ Сохраняет токен и ID приложения в базу данных, при этом в базе 
        гарантированно хранится только одна запись с данными
        После сохранения токен проверяется на действительность
        """
        
        client_id = self.token_ui.line_edit_client_id.text()
        self.token = self.token_ui.line_edit_token.text()
        self.conn.update_client_id(client_id)
        self.conn.update_token(self.token)
        
        self.token_window.close()
        self.check_token()
        
    def select_path(self):
        """ Открывает окно выбора папки для загрузки изображений
        """
        
        path = QFileDialog.getExistingDirectory(
            self,
            "Выберите папку для загрузки"
            )
        self.ui.line_edit_select_path.setText(path)

    def open_wall_settings_window(self):
        """ Открывает окно с настройками загрузки изображений со стены при условии,
        что действителен ID группы, введённый в поле group_id, что проверяется
        с помощью тестового запроса к VK API
        """
        
        self.wall_window = QtWidgets.QDialog()
        self.wall_ui = setting_wall_window_ui.Ui_Dialog()
        self.wall_ui.setupUi(self.wall_window)
        
        group_id = self.ui.line_edit_group_id.text()
        if self.parser.check_group_id(self.token, group_id):
            self.wall_window.show()
            
            self.wall_ui.label_count.setText(self.parser.get_total_photos(self.ui.line_edit_group_id))
            self.wall_ui.combo_box_select_photos.currentTextChanged.connect(self.get_amount_of_photos)
            self.wall_ui.button_save.clicked.connect(self.save_amount_of_photos)
            
        else:
            QMessageBox.critical(
            self,
            "Ошибка ID группы",
            "Проверьте правильность введённого ID группы",
            buttons=QMessageBox.Ok,
            defaultButton=QMessageBox.Ok,
        )
            
    def get_amount_of_photos(self):
        """ Получает параметры настройки количества загружаемых со стены изображений
        Если в ComboBox были выбраны поля "Последние" или "Первые" то для ввода
        количества фотографий становится доступен виджет lineEdit  
        """
        
        self.selected_amount = self.wall_ui.combo_box_select_photos.currentText()
        if self.selected_amount == "Последние" or self.selected_amount == "Первые":
            self.wall_ui.line_edit_count.setEnabled(True)
        else:
            self.wall_ui.line_edit_count.setDisabled(True)
            
    def save_amount_of_photos(self):
        """ Сохраняет параметры настройки количества загружаемых со стены изображений
        в соответствующие атрибуты класса
        """
        
        if self.wall_ui.line_edit_count.isEnabled():
            self.amount = self.wall_ui.line_edit_count.text()
            if not self.amount.isdigit():
                frame = self.wall_ui.wall_frame
                info_label = QtWidgets.QLabel(frame)
                info_label.setText("Введённое значение должно быть числом")
                info_label.setStyleSheet("color: red")
                info_label.setGeometry(10, 10, 200, 300)
            else:
                print(self.selected_amount, self.amount)
                self.wall_window.close()
        
    def open_album_settings_window(self):
        """ Открывает окно с настройками загрузки альбомов
        """
        
        self.album_window = QtWidgets.QDialog()
        self.album_ui = setting_album_window_ui.Ui_Dialog()
        self.album_ui.setupUi(self.album_window)
        
        group_id = self.ui.line_edit_group_id.text()
        if self.parser.check_group_id(self.token, group_id):
            self.album_window.show()
        else:
            QMessageBox.critical(
            self,
            "Ошибка ID группы",
            "Проверьте правильность введённого ID группы",
            buttons=QMessageBox.Ok,
            defaultButton=QMessageBox.Ok,
        )

    def parsing(self):
        images_folder = 'images'
        
        if not os.path.exists(images_folder):
            os.makedirs(images_folder)
            
        path = os.getcwd() + '/' + images_folder
        print(self.token)
        while True:
            images = self.vk.photos.get(owner_id=-220740378, album_id='wall', photo_sizes=1, count=1000, offset=self.offset)
            
            for image in images['items']:
                max_size_photo = sorted(image['sizes'], key=lambda dict: dict['height'])
                url = max_size_photo[-1]['url']
                name = f'{path}/{self.count}.jpg' 
                urllib.request.urlretrieve(url, name)
                self.count += 1
                
            self.offset += 1000
            if self.offset >= images['count']:
                break


def main():
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()
