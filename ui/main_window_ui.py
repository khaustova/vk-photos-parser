# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)
import ui.icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(441, 241)
        MainWindow.setMinimumSize(QSize(441, 241))
        MainWindow.setMaximumSize(QSize(441, 241))
        MainWindow.setStyleSheet(u"background-color: #edeef0;\n"
"font-family: Arial;\n"
"font-size: 12px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_9 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(6, 6, 6, 6)
        self.params_tabwidget = QTabWidget(self.centralwidget)
        self.params_tabwidget.setObjectName(u"params_tabwidget")
        self.params_tabwidget.setStyleSheet(u"QTabWidget::pane {\n"
"  border: 1px solid lightgray;\n"
"  top:-1px; \n"
"  background: rgb(245, 245, 245); \n"
"} \n"
"\n"
"QTabBar::tab {\n"
"  background: rgb(230, 230, 230); \n"
"  border: 1px solid lightgray; \n"
"  padding: 3px 15px;\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"  background: white; \n"
"  margin-bottom: -1px; \n"
"}")
        self.page_photos = QWidget()
        self.page_photos.setObjectName(u"page_photos")
        self.page_photos.setStyleSheet(u"border: none;\n"
"background: white;")
        self.verticalLayout_5 = QVBoxLayout(self.page_photos)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_group_id = QLabel(self.page_photos)
        self.label_group_id.setObjectName(u"label_group_id")
        self.label_group_id.setStyleSheet(u"background-color: transparent;\n"
"padding-right: 4px;")

        self.horizontalLayout_2.addWidget(self.label_group_id)

        self.line_edit_group_id = QLineEdit(self.page_photos)
        self.line_edit_group_id.setObjectName(u"line_edit_group_id")
        self.line_edit_group_id.setMinimumSize(QSize(0, 0))
        self.line_edit_group_id.setMaximumSize(QSize(16777215, 16777215))
        self.line_edit_group_id.setStyleSheet(u"QLineEdit {\n"
"background-color: white;\n"
"border: 1px solid #d3d9de;\n"
"border-radius: 3px;\n"
"padding: 1px;\n"
"height: 21px;\n"
"}\n"
"\n"
"QLineEdit::focus {\n"
"border: 1px solid #d3d9de;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.line_edit_group_id)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 5, -1, -1)
        self.label_select_sources = QLabel(self.page_photos)
        self.label_select_sources.setObjectName(u"label_select_sources")
        self.label_select_sources.setMinimumSize(QSize(0, 0))
        self.label_select_sources.setStyleSheet(u"background-color: transparent;\n"
"padding-top: 4px;\n"
"width: 210px;")
        self.label_select_sources.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_6.addWidget(self.label_select_sources)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, -1)
        self.check_box_wall = QCheckBox(self.page_photos)
        self.check_box_wall.setObjectName(u"check_box_wall")
        self.check_box_wall.setMaximumSize(QSize(16777215, 16777215))
        self.check_box_wall.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_box_wall.setStyleSheet(u"QCheckBox{ \n"
" background-color: transparent;\n"
"}\n"
"QCheckBox::indicator {\n"
"border: 1px solid #d3d9de;\n"
"margin-right: 5px;\n"
"border-radius: 3px;\n"
"width: 15px;\n"
"height: 15px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"border: 1px solid #d3d9de;\n"
"color: white;\n"
"background-color: #5181b8;\n"
"image: url(:/icon/icons/check.png);\n"
"}")
        self.check_box_wall.setIconSize(QSize(11, 16))

        self.horizontalLayout_3.addWidget(self.check_box_wall)

        self.button_wall_settings = QPushButton(self.page_photos)
        self.button_wall_settings.setObjectName(u"button_wall_settings")
        self.button_wall_settings.setEnabled(False)
        self.button_wall_settings.setMaximumSize(QSize(24, 24))
        self.button_wall_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_wall_settings.setStyleSheet(u"QPushButton {\n"
"background-color: #ebf2fa;\n"
"color: #3770b1;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding: 3px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #dfeaf6;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #d5e2f1;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_wall_settings.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.button_wall_settings)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.check_box_album = QCheckBox(self.page_photos)
        self.check_box_album.setObjectName(u"check_box_album")
        self.check_box_album.setEnabled(True)
        self.check_box_album.setMaximumSize(QSize(16777215, 16777215))
        self.check_box_album.setSizeIncrement(QSize(0, 0))
        self.check_box_album.setBaseSize(QSize(0, 0))
        self.check_box_album.setCursor(QCursor(Qt.PointingHandCursor))
        self.check_box_album.setStyleSheet(u"QCheckBox{ \n"
" background-color: transparent;\n"
"}\n"
"QCheckBox::indicator {\n"
"border: 1px solid #d3d9de;\n"
"margin-right: 5px;\n"
"border-radius: 3px;\n"
"width: 15px;\n"
"height: 15px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"border: 1px solid #d3d9de;\n"
"color: white;\n"
"background-color: #5181b8;\n"
"image: url(:/icon/icons/check.png);\n"
"}")

        self.horizontalLayout_4.addWidget(self.check_box_album)

        self.button_album_settings = QPushButton(self.page_photos)
        self.button_album_settings.setObjectName(u"button_album_settings")
        self.button_album_settings.setEnabled(False)
        self.button_album_settings.setMaximumSize(QSize(24, 24))
        self.button_album_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_album_settings.setStyleSheet(u"QPushButton {\n"
"background-color: #ebf2fa;\n"
"color: #3770b1;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding: 3px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #dfeaf6;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #d5e2f1;\n"
"}")
        self.button_album_settings.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.button_album_settings)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.label_select_path = QLabel(self.page_photos)
        self.label_select_path.setObjectName(u"label_select_path")
        self.label_select_path.setStyleSheet(u"background-color: transparent;\n"
"padding-right: 2px;\n"
"margin-top: -10px;")
        self.label_select_path.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.label_select_path)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.line_edit_select_path = QLineEdit(self.page_photos)
        self.line_edit_select_path.setObjectName(u"line_edit_select_path")
        self.line_edit_select_path.setEnabled(False)
        self.line_edit_select_path.setMinimumSize(QSize(0, 0))
        self.line_edit_select_path.setStyleSheet(u"QLineEdit {\n"
"background-color: white;\n"
"border: 1px solid #d3d9de;\n"
"border-right: none;\n"
"padding: 1px;\n"
"height: 21px;\n"
"border-radius: 3px;\n"
"border-top-right-radius: none;\n"
"}\n"
"\n"
"QLineEdit::disabled {\n"
"color: black;\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.line_edit_select_path)

        self.button_select_path = QPushButton(self.page_photos)
        self.button_select_path.setObjectName(u"button_select_path")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_select_path.sizePolicy().hasHeightForWidth())
        self.button_select_path.setSizePolicy(sizePolicy)
        self.button_select_path.setMinimumSize(QSize(0, 0))
        self.button_select_path.setBaseSize(QSize(2, 0))
        self.button_select_path.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_select_path.setStyleSheet(u"QPushButton {\n"
"background-color: #ebf2fa;\n"
"color: #3770b1;\n"
"font-weight: bold;\n"
"border: none;\n"
"padding: 1px;\n"
"height: 21px;\n"
"width: 70px;\n"
"padding: 2px;\n"
"border-radius: 3px;\n"
"border-top-left-radius: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #dfeaf6;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #d5e2f1;\n"
"}")

        self.horizontalLayout_5.addWidget(self.button_select_path)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.button_parse = QPushButton(self.page_photos)
        self.button_parse.setObjectName(u"button_parse")
        self.button_parse.setEnabled(True)
        self.button_parse.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_parse.setStyleSheet(u"QPushButton {\n"
"background-color: #0077FF;\n"
"color: white;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding: 3px;\n"
"margin-top: 3px;\n"
"height: 20px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #1a85ff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #5181b8;\n"
"}")

        self.verticalLayout_3.addWidget(self.button_parse)

        self.label_info = QLabel(self.page_photos)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setStyleSheet(u"background-color: transparent;")
        self.label_info.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_info)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.params_tabwidget.addTab(self.page_photos, "")
        self.page_authorization = QWidget()
        self.page_authorization.setObjectName(u"page_authorization")
        self.page_authorization.setStyleSheet(u"border: none;\n"
"background: white;")
        self.verticalLayout_7 = QVBoxLayout(self.page_authorization)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 10, 10, 5)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.line_edit_token = QLineEdit(self.page_authorization)
        self.line_edit_token.setObjectName(u"line_edit_token")
        self.line_edit_token.setMinimumSize(QSize(0, 0))
        self.line_edit_token.setStyleSheet(u"QLineEdit {\n"
"background-color: white;\n"
"border: 1px solid #d3d9de;\n"
"border-right: none;\n"
"padding: 1px;\n"
"height: 21px;\n"
"border-radius: 3px;\n"
"border-top-right-radius: none;\n"
"}\n"
"\n"
"QLineEdit::disabled {\n"
"color: black;\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.line_edit_token)

        self.button_save = QPushButton(self.page_authorization)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_save.setStyleSheet(u"QPushButton {\n"
"background-color: #0077FF;\n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"padding: 1px;\n"
"height: 21px;\n"
"width: 110px;\n"
"padding: 2px;\n"
"border-radius: 3px;\n"
"border-top-left-radius: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #1a85ff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #5181b8;\n"
"}")

        self.horizontalLayout_7.addWidget(self.button_save)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.label_token_info = QLabel(self.page_authorization)
        self.label_token_info.setObjectName(u"label_token_info")
        self.label_token_info.setStyleSheet(u"background-color: transparent;")

        self.verticalLayout_8.addWidget(self.label_token_info)

        self.label = QLabel(self.page_authorization)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-weight: bold;")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 5)
        self.label_step_1 = QLabel(self.page_authorization)
        self.label_step_1.setObjectName(u"label_step_1")
        self.label_step_1.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.label_step_1)

        self.label_step_4 = QLabel(self.page_authorization)
        self.label_step_4.setObjectName(u"label_step_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_step_4.sizePolicy().hasHeightForWidth())
        self.label_step_4.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.label_step_4)

        self.label_2 = QLabel(self.page_authorization)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 3, -1, -1)
        self.line_edit_client_id = QLineEdit(self.page_authorization)
        self.line_edit_client_id.setObjectName(u"line_edit_client_id")
        self.line_edit_client_id.setMinimumSize(QSize(0, 21))
        self.line_edit_client_id.setStyleSheet(u"QLineEdit {\n"
"background-color: white;\n"
"border: 1px solid #d3d9de;\n"
"border-right: none;\n"
"padding: 1px;\n"
"height: 21px;\n"
"border-radius: 3px;\n"
"border-top-right-radius: none;\n"
"}\n"
"\n"
"QLineEdit::disabled {\n"
"color: black;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.line_edit_client_id)

        self.button_get_token = QPushButton(self.page_authorization)
        self.button_get_token.setObjectName(u"button_get_token")
        self.button_get_token.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_get_token.setStyleSheet(u"QPushButton {\n"
"background-color: #ebf2fa;\n"
"color: #3770b1;\n"
"font-weight: bold;\n"
"border: none;\n"
"padding: 1px;\n"
"height: 21px;\n"
"width: 150px;\n"
"padding: 2px;\n"
"border-radius: 3px;\n"
"border-top-left-radius: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #dfeaf6;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #d5e2f1;\n"
"}")

        self.horizontalLayout.addWidget(self.button_get_token)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.label_step_5 = QLabel(self.page_authorization)
        self.label_step_5.setObjectName(u"label_step_5")
        self.label_step_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_step_5)


        self.verticalLayout_7.addLayout(self.verticalLayout_8)

        self.params_tabwidget.addTab(self.page_authorization, "")

        self.verticalLayout_9.addWidget(self.params_tabwidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.params_tabwidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0441\u0438\u043d\u0433 \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0439 \u0412\u043a\u043e\u043d\u0442\u0430\u043a\u0442\u0435", None))
        self.label_group_id.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 ID \u0433\u0440\u0443\u043f\u043f\u044b:", None))
        self.label_select_sources.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u0442\u0435 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0438 \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0439:", None))
        self.check_box_wall.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0435\u043d\u0430", None))
        self.button_wall_settings.setText("")
        self.check_box_album.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043b\u044c\u0431\u043e\u043c\u044b", None))
        self.button_album_settings.setText("")
        self.label_select_path.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0430\u043f\u043a\u0443 \u0434\u043b\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438:", None))
        self.button_select_path.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.button_parse.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c", None))
        self.label_info.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0430: \u0437\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u0435 \u0432\u0441\u0435 \u043f\u043e\u043b\u044f \u0438 \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 \u00ab\u0421\u043a\u0430\u0447\u0430\u0442\u044c\u00bb", None))
        self.params_tabwidget.setTabText(self.params_tabwidget.indexOf(self.page_photos), QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0438", None))
        self.button_save.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0442\u043e\u043a\u0435\u043d", None))
        self.label_token_info.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043a\u0435\u043d \u043d\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u0435\u043d", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u044f \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f \u043d\u043e\u0432\u043e\u0433\u043e \u0442\u043e\u043a\u0435\u043d\u0430:", None))
        self.label_step_1.setText(QCoreApplication.translate("MainWindow", u"1. \u041e\u0442\u043a\u0440\u043e\u0439\u0442\u0435 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f\u043c\u0438.", None))
        self.label_step_4.setText(QCoreApplication.translate("MainWindow", u"2. \u0415\u0441\u043b\u0438 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0435\u0449\u0451 \u043d\u0435 \u0441\u043e\u0437\u0434\u0430\u043d\u043e, \u0442\u043e \u0441\u043e\u0437\u0434\u0430\u0439\u0442\u0435 \u0435\u0433\u043e.", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"3. \u0412\u0432\u0435\u0434\u0438\u0442\u0435 ID \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0432 \u043f\u043e\u043b\u0435 \u043d\u0438\u0436\u0435 \u0438 \u043f\u0435\u0440\u0435\u0439\u0434\u0438\u0442\u0435 \u043f\u043e \u0441\u0441\u044b\u043b\u043a\u0435.", None))
        self.button_get_token.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438 \u043f\u043e \u0441\u0441\u044b\u043b\u043a\u0435", None))
        self.label_step_5.setText(QCoreApplication.translate("MainWindow", u"4. \u0421\u043a\u043e\u043f\u0438\u0440\u0443\u0439\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430 access_token \u0438\u0437 \u0430\u0434\u0440\u0435\u0441\u043d\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0438.", None))
        self.params_tabwidget.setTabText(self.params_tabwidget.indexOf(self.page_authorization), QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
    # retranslateUi

