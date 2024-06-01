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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import ui.icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(390, 232)
        MainWindow.setMinimumSize(QSize(390, 215))
        MainWindow.setMaximumSize(QSize(390, 232))
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(225, 233, 251, 255), stop:1 rgba(220, 220, 220, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 4)
        self.params_frame = QFrame(self.centralwidget)
        self.params_frame.setObjectName(u"params_frame")
        self.verticalLayout_4 = QVBoxLayout(self.params_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_add_token = QPushButton(self.params_frame)
        self.button_add_token.setObjectName(u"button_add_token")
        self.button_add_token.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_add_token.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(255, 255, 255, 80);\n"
"border: 1px solid black;\n"
"padding: 3px 3px;\n"
"height: 17px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.horizontalLayout.addWidget(self.button_add_token)

        self.label_token_info = QLabel(self.params_frame)
        self.label_token_info.setObjectName(u"label_token_info")
        self.label_token_info.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout.addWidget(self.label_token_info)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_group_id = QLabel(self.params_frame)
        self.label_group_id.setObjectName(u"label_group_id")
        self.label_group_id.setStyleSheet(u"background-color: transparent;\n"
"padding-right: 2px;")

        self.horizontalLayout_2.addWidget(self.label_group_id)

        self.line_edit_group_id = QLineEdit(self.params_frame)
        self.line_edit_group_id.setObjectName(u"line_edit_group_id")
        self.line_edit_group_id.setMinimumSize(QSize(0, 21))
        self.line_edit_group_id.setStyleSheet(u"QLineEdit {\n"
"background-color: white;\n"
"border: 1px solid black;\n"
"padding: 1px;\n"
"}\n"
"\n"
"QLineEdit::focus {\n"
"background-color: white;\n"
"border: 1px solid rgb(21, 148, 194);\n"
"padding: 1px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.line_edit_group_id)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_select_sources = QLabel(self.params_frame)
        self.label_select_sources.setObjectName(u"label_select_sources")
        self.label_select_sources.setMinimumSize(QSize(0, 0))
        self.label_select_sources.setStyleSheet(u"background-color: transparent;\n"
"padding-top: 1px;\n"
"width: 210px;")
        self.label_select_sources.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_6.addWidget(self.label_select_sources)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.check_box_wall = QCheckBox(self.params_frame)
        self.check_box_wall.setObjectName(u"check_box_wall")
        self.check_box_wall.setMaximumSize(QSize(16777215, 16777215))
        self.check_box_wall.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_3.addWidget(self.check_box_wall)

        self.button_setting_wall = QPushButton(self.params_frame)
        self.button_setting_wall.setObjectName(u"button_setting_wall")
        self.button_setting_wall.setMaximumSize(QSize(24, 24))
        self.button_setting_wall.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_setting_wall.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(255, 255, 255, 80);\n"
"border: 1px solid black;\n"
"padding: 3px 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icons/settings_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_setting_wall.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.button_setting_wall)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.check_box_album = QCheckBox(self.params_frame)
        self.check_box_album.setObjectName(u"check_box_album")
        self.check_box_album.setEnabled(True)
        self.check_box_album.setMaximumSize(QSize(16777215, 16777215))
        self.check_box_album.setSizeIncrement(QSize(0, 0))
        self.check_box_album.setBaseSize(QSize(0, 0))
        self.check_box_album.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout_4.addWidget(self.check_box_album)

        self.button_setting_album = QPushButton(self.params_frame)
        self.button_setting_album.setObjectName(u"button_setting_album")
        self.button_setting_album.setMaximumSize(QSize(24, 24))
        self.button_setting_album.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_setting_album.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(255, 255, 255, 80);\n"
"border: 1px solid black;\n"
"padding: 3px 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.button_setting_album.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.button_setting_album)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_select_path = QLabel(self.params_frame)
        self.label_select_path.setObjectName(u"label_select_path")
        self.label_select_path.setStyleSheet(u"background-color: transparent;\n"
"padding-right: 2px;")

        self.verticalLayout.addWidget(self.label_select_path)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.line_edit_select_path = QLineEdit(self.params_frame)
        self.line_edit_select_path.setObjectName(u"line_edit_select_path")
        self.line_edit_select_path.setEnabled(False)
        self.line_edit_select_path.setMinimumSize(QSize(0, 21))
        self.line_edit_select_path.setStyleSheet(u"QLineEdit {\n"
"background-color: white;\n"
"border: 1px solid black;\n"
"border-right: none;\n"
"padding: 1px;\n"
"height: 21px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.line_edit_select_path)

        self.button_select_path = QPushButton(self.params_frame)
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
"background-color: rgba(255, 255, 255, 80);\n"
"border: 1px solid black;\n"
"padding: 3px;\n"
"height: 17px;\n"
"width: 55px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.horizontalLayout_5.addWidget(self.button_select_path)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.button_parse = QPushButton(self.params_frame)
        self.button_parse.setObjectName(u"button_parse")
        self.button_parse.setEnabled(True)
        self.button_parse.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_parse.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(70, 130, 180);\n"
"color: white;\n"
"border: 1px solid black;\n"
"padding: 3px 3px;\n"
"height: 17px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(100, 152, 195);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(70, 130, 180, 90);\n"
"}")

        self.verticalLayout_3.addWidget(self.button_parse)

        self.label_info = QLabel(self.params_frame)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setStyleSheet(u"background-color: transparent;")
        self.label_info.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_info)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addWidget(self.params_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_add_token.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u043e\u043a\u0435\u043d", None))
        self.label_token_info.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043a\u0435\u043d \u043d\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u0435\u043d", None))
        self.label_group_id.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 ID \u0433\u0440\u0443\u043f\u043f\u044b:", None))
        self.label_select_sources.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u0442\u0435 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0438 \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0439:", None))
        self.check_box_wall.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0435\u043d\u0430", None))
        self.button_setting_wall.setText("")
        self.check_box_album.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043b\u044c\u0431\u043e\u043c\u044b", None))
        self.button_setting_album.setText("")
        self.label_select_path.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0430\u043f\u043a\u0443 \u0434\u043b\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438:", None))
        self.button_select_path.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.button_parse.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u0447\u0430\u0442\u044c", None))
        self.label_info.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u0435 \u0432\u0441\u0435 \u043f\u043e\u043b\u044f \u0438 \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 \u00ab\u0421\u043a\u0430\u0447\u0430\u0442\u044c\u00bb", None))
    # retranslateUi

