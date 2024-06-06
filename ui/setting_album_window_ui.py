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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 202)
        Dialog.setStyleSheet(u"background-color: #edeef0;\n"
"font-family: Arial;\n"
"font-size: 12px;")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.albums_frame = QFrame(Dialog)
        self.albums_frame.setObjectName(u"albums_frame")
        self.albums_frame.setStyleSheet(u"background-color: white;\n"
"border-radius: 4px;")
        self.verticalLayout_3 = QVBoxLayout(self.albums_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_select_albums = QLabel(self.albums_frame)
        self.label_select_albums.setObjectName(u"label_select_albums")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_select_albums.sizePolicy().hasHeightForWidth())
        self.label_select_albums.setSizePolicy(sizePolicy)
        self.label_select_albums.setStyleSheet(u"margin-top: 5px;\n"
"height: 12px;")
        self.label_select_albums.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_2.addWidget(self.label_select_albums)

        self.scrollArea = QScrollArea(self.albums_frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical {              \n"
"    border: none;     \n"
"    background: #f0f0f0;\n"
"    width: 10px;               \n"
"    margin: 5px 0px 5px 0px;\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #cdcdcd;\n"
"    min-height: 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: #a6a6a6;\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: #606060;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0 px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar:horizontal {              \n"
"    border: none;     \n"
"    background: #f0f0f0;\n"
"    height: 10px;               \n"
"    margin: 0px 5px 0px 5px;\n"
"    min-height: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #cdcdcd;\n"
" "
                        "   min-height: 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{	\n"
"	background-color: #a6a6a6;\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {	\n"
"	background-color: #606060;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    height: 0 px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 378, 126))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: transparent;")
        self.verticalLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 381, 502))
        self.layout = QVBoxLayout(self.verticalLayoutWidget)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.button_save = QPushButton(self.albums_frame)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_save.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.button_save)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout.addWidget(self.albums_frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u043e\u0440 \u0430\u043b\u044c\u0431\u043e\u043c\u043e\u0432", None))
        self.label_select_albums.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0430\u043b\u044c\u0431\u043e\u043c\u044b \u0434\u043b\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438:", None))
        self.button_save.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

