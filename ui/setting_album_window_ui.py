# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting_album_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 158)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(225, 233, 251, 255), stop:1 rgba(220, 220, 220, 255));")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_select_albums = QLabel(Dialog)
        self.label_select_albums.setObjectName(u"label_select_albums")

        self.verticalLayout.addWidget(self.label_select_albums)

        self.list_widgets = QListWidget(Dialog)
        self.list_widgets.setObjectName(u"list_widgets")
        self.list_widgets.setStyleSheet(u"background-color: transparent;\n"
"border: none;")

        self.verticalLayout.addWidget(self.list_widgets)

        self.button_save = QPushButton(Dialog)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(70, 130, 180);\n"
"color: white;\n"
"border: 1px solid black;\n"
"padding: 3px 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(100, 152, 195);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(70, 130, 180 90);\n"
"}")

        self.verticalLayout.addWidget(self.button_save)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_select_albums.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0430\u043b\u044c\u0431\u043e\u043c\u044b \u0434\u043b\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438:", None))
        self.button_save.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

