# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_wall_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import ui.icons_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(311, 187)
        Dialog.setMinimumSize(QSize(311, 187))
        Dialog.setMaximumSize(QSize(311, 187))
        icon = QIcon()
        icon.addFile(u":/icon/icons/image.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"background-color: #edeef0;\n"
"font-family: Arial;\n"
"font-size: 12px;")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.wall_frame = QFrame(Dialog)
        self.wall_frame.setObjectName(u"wall_frame")
        self.wall_frame.setStyleSheet(u"background-color: white;\n"
"border-radius: 4px;")
        self.verticalLayout = QVBoxLayout(self.wall_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.label_define_count = QLabel(self.wall_frame)
        self.label_define_count.setObjectName(u"label_define_count")

        self.verticalLayout.addWidget(self.label_define_count)

        self.label_count = QLabel(self.wall_frame)
        self.label_count.setObjectName(u"label_count")
        self.label_count.setStyleSheet(u"font-weight: bold;\n"
"font-size: 11pt;")
        self.label_count.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_count)

        self.label_select_photo = QLabel(self.wall_frame)
        self.label_select_photo.setObjectName(u"label_select_photo")

        self.verticalLayout.addWidget(self.label_select_photo)

        self.combo_box_select_photos = QComboBox(self.wall_frame)
        self.combo_box_select_photos.addItem("")
        self.combo_box_select_photos.addItem("")
        self.combo_box_select_photos.addItem("")
        self.combo_box_select_photos.setObjectName(u"combo_box_select_photos")
        self.combo_box_select_photos.setStyleSheet(u"QComboBox {\n"
"font-size: 10pt;\n"
"padding: 5px;\n"
"selection-background-color: transparent;\n"
"height: 21px;\n"
"border: 1px solid #d3d9de;\n"
"border-radius: 3px;\n"
"padding: 1px 18px 1px 3px;\n"
"min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"padding-top: 3px;\n"
"padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
"width: 20px;\n"
"border-left-width: 1px;\n"
"border-left-color: darkgray;\n"
"border-left-style: solid;\n"
"border-top-right-radius: 3px;\n"
"border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"image: url(:/icon/icons/keyboard_arrow_down.png);\n"
"width: 25px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { \n"
"top: 1px;\n"
"left: 1px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"background-color: rgb(249, 249, 249);\n"
"border: 1px solid #d3d9de;\n"
"border-radius: 3px;\n"
"padding: 3px;\n"
"selection-background-color:#ebf2fa;\n"
"selection-color: black;\n"
"}\n"
"\n"
"QComboBox QAbstractI"
                        "temView::item {\n"
"padding: 5px;\n"
"}")
        self.combo_box_select_photos.setFrame(True)

        self.verticalLayout.addWidget(self.combo_box_select_photos)

        self.line_edit_count = QLineEdit(self.wall_frame)
        self.line_edit_count.setObjectName(u"line_edit_count")
        self.line_edit_count.setEnabled(False)
        self.line_edit_count.setMinimumSize(QSize(0, 0))
        self.line_edit_count.setMaximumSize(QSize(16777215, 658786))
        self.line_edit_count.setStyleSheet(u"QLineEdit {\n"
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
"QLineEdit::disabled {\n"
"background-color: rgb(239, 239, 239);\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout.addWidget(self.line_edit_count)

        self.button_save = QPushButton(self.wall_frame)
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

        self.verticalLayout.addWidget(self.button_save)


        self.verticalLayout_2.addWidget(self.wall_frame)


        self.retranslateUi(Dialog)

        self.combo_box_select_photos.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0439", None))
        self.label_define_count.setText(QCoreApplication.translate("Dialog", u"\u041e\u0431\u0449\u0435\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0439 \u043d\u0430 \u0441\u0442\u0435\u043d\u0435 \u0433\u0440\u0443\u043f\u043f\u044b:", None))
        self.label_count.setText(QCoreApplication.translate("Dialog", u"100", None))
        self.label_select_photo.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0444\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u0439 \u0434\u043b\u044f \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438:", None))
        self.combo_box_select_photos.setItemText(0, QCoreApplication.translate("Dialog", u"\u0412\u0441\u0435", None))
        self.combo_box_select_photos.setItemText(1, QCoreApplication.translate("Dialog", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435", None))
        self.combo_box_select_photos.setItemText(2, QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0432\u044b\u0435", None))

        self.button_save.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

