# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting_wall_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(333, 165)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(225, 233, 251, 255), stop:1 rgba(220, 220, 220, 255));")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_define_count = QLabel(Dialog)
        self.label_define_count.setObjectName(u"label_define_count")

        self.verticalLayout.addWidget(self.label_define_count)

        self.label_count = QLabel(Dialog)
        self.label_count.setObjectName(u"label_count")
        self.label_count.setStyleSheet(u"font-weight: bold;\n"
"font-size: 11pt;")
        self.label_count.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_count)

        self.label_select_photo = QLabel(Dialog)
        self.label_select_photo.setObjectName(u"label_select_photo")

        self.verticalLayout.addWidget(self.label_select_photo)

        self.combo_box_select_photos = QComboBox(Dialog)
        self.combo_box_select_photos.addItem("")
        self.combo_box_select_photos.addItem("")
        self.combo_box_select_photos.addItem("")
        self.combo_box_select_photos.setObjectName(u"combo_box_select_photos")
        self.combo_box_select_photos.setStyleSheet(u"QComboBox {\n"
"font-size: 10pt;\n"
"padding: 5px;\n"
"selection-background-color: transparent;\n"
"}\n"
"")
        self.combo_box_select_photos.setFrame(True)

        self.verticalLayout.addWidget(self.combo_box_select_photos)

        self.line_edit_count = QLineEdit(Dialog)
        self.line_edit_count.setObjectName(u"line_edit_count")
        self.line_edit_count.setEnabled(False)
        self.line_edit_count.setMinimumSize(QSize(0, 21))
        self.line_edit_count.setMaximumSize(QSize(16777215, 21))
        self.line_edit_count.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit::disabled {\n"
"background-color: transparent;\n"
"border: 1px solid rgba(0, 0, 0, 60)\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout.addWidget(self.line_edit_count)

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

        self.combo_box_select_photos.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_define_count.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u0449\u0435\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0439 \u043d\u0430 \u0441\u0442\u0435\u043d\u0435 \u0433\u0440\u0443\u043f\u043f\u044b:", None))
        self.label_count.setText(QCoreApplication.translate("Dialog", u"100", None))
        self.label_select_photo.setText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0438\u0442\u0435  \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0437\u0430\u0433\u0440\u0443\u0436\u0430\u0435\u043c\u044b\u0445 \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0439:", None))
        self.combo_box_select_photos.setItemText(0, QCoreApplication.translate("Dialog", u"\u0412\u0441\u0435", None))
        self.combo_box_select_photos.setItemText(1, QCoreApplication.translate("Dialog", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435", None))
        self.combo_box_select_photos.setItemText(2, QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0432\u044b\u0435", None))

        self.button_save.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

