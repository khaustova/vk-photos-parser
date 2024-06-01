# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_token_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(407, 247)
        Dialog.setMinimumSize(QSize(343, 152))
        Dialog.setMaximumSize(QSize(3410, 1550))
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(225, 233, 251, 255), stop:1 rgba(220, 220, 220, 255));")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.token_frame = QFrame(Dialog)
        self.token_frame.setObjectName(u"token_frame")
        self.token_frame.setStyleSheet(u"background-color: transparent;")
        self.verticalLayout = QVBoxLayout(self.token_frame)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_step_1 = QLabel(self.token_frame)
        self.label_step_1.setObjectName(u"label_step_1")
        self.label_step_1.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.label_step_1)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_step_2 = QLabel(self.token_frame)
        self.label_step_2.setObjectName(u"label_step_2")

        self.verticalLayout.addWidget(self.label_step_2)

        self.label_step_3 = QLabel(self.token_frame)
        self.label_step_3.setObjectName(u"label_step_3")

        self.verticalLayout.addWidget(self.label_step_3)

        self.label_step_4 = QLabel(self.token_frame)
        self.label_step_4.setObjectName(u"label_step_4")

        self.verticalLayout.addWidget(self.label_step_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_edit_client_id = QLineEdit(self.token_frame)
        self.line_edit_client_id.setObjectName(u"line_edit_client_id")
        self.line_edit_client_id.setMinimumSize(QSize(0, 21))
        self.line_edit_client_id.setStyleSheet(u"QLineEdit {\n"
"background-color: white;\n"
"border: 1px solid black;\n"
"padding: 1px;\n"
"border-right: none;\n"
"height: 21px;\n"
"}\n"
"\n"
"QLineEdit::focus {\n"
"background-color: white;\n"
"border: 1px solid rgb(21, 148, 194);\n"
"padding: 1px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.line_edit_client_id)

        self.button_get_token = QPushButton(self.token_frame)
        self.button_get_token.setObjectName(u"button_get_token")
        self.button_get_token.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_get_token.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(70, 130, 180);\n"
"color: white;\n"
"border: 1px solid black;\n"
"padding: 3px;\n"
"width: 100px;\n"
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

        self.horizontalLayout_2.addWidget(self.button_get_token)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_step_5 = QLabel(self.token_frame)
        self.label_step_5.setObjectName(u"label_step_5")

        self.verticalLayout.addWidget(self.label_step_5)

        self.label_step_5_1 = QLabel(self.token_frame)
        self.label_step_5_1.setObjectName(u"label_step_5_1")

        self.verticalLayout.addWidget(self.label_step_5_1)

        self.line_edit_token = QLineEdit(self.token_frame)
        self.line_edit_token.setObjectName(u"line_edit_token")
        self.line_edit_token.setMinimumSize(QSize(0, 21))
        self.line_edit_token.setStyleSheet(u"QLineEdit {\n"
"background-color: white;\n"
"border: 1px solid black;\n"
"padding: 1px;\n"
"height: 21px;\n"
"}\n"
"\n"
"QLineEdit::focus {\n"
"background-color: white;\n"
"border: 1px solid rgb(21, 148, 194);\n"
"padding: 1px;\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.line_edit_token)

        self.button_save = QPushButton(self.token_frame)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_save.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(70, 130, 180);\n"
"color: white;\n"
"border: 1px solid black;\n"
"padding: 3px;\n"
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

        self.verticalLayout.addWidget(self.button_save)


        self.verticalLayout_2.addWidget(self.token_frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_step_1.setText(QCoreApplication.translate("Dialog", u"1. \u041e\u0442\u043a\u0440\u043e\u0439\u0442\u0435 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f\u043c\u0438.", None))
        self.label_step_2.setText(QCoreApplication.translate("Dialog", u"2. \u0415\u0441\u043b\u0438 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0435\u0449\u0451 \u043d\u0435 \u0441\u043e\u0437\u0434\u0430\u043d\u043e, \u0442\u043e \u0441\u043e\u0437\u0434\u0430\u0439\u0442\u0435 \u0435\u0433\u043e.", None))
        self.label_step_3.setText(QCoreApplication.translate("Dialog", u"3. \u041f\u0435\u0440\u0435\u0439\u0434\u0438\u0442\u0435 \u0432 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f.", None))
        self.label_step_4.setText(QCoreApplication.translate("Dialog", u"4. \u0421\u043a\u043e\u043f\u0438\u0440\u0443\u0439\u0442\u0435 \u0435\u0433\u043e ID \u0438 \u0432\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u0435\u0433\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0432 \u043f\u043e\u043b\u0435 \u043d\u0438\u0436\u0435:", None))
        self.button_get_token.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0442\u043e\u043a\u0435\u043d", None))
        self.label_step_5.setText(QCoreApplication.translate("Dialog", u"5. \u0421\u043a\u043e\u043f\u0438\u0440\u0443\u0439\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430 access_token \u0438\u0437 \u0430\u0434\u0440\u0435\u0441\u043d\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0438.", None))
        self.label_step_5_1.setText(QCoreApplication.translate("Dialog", u"\u0412\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u043d\u043e\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0432 \u043f\u043e\u043b\u0435 \u043d\u0438\u0436\u0435:", None))
        self.button_save.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

