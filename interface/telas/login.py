# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginQXhWjN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(450, 600)
        Login.setMinimumSize(QSize(450, 600))
        Login.setStyleSheet(u"QWidget{\n"
"background-color: rgb(236, 242, 248);\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"padding-left: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid black;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(149, 172, 213);\n"
"border: none;\n"
"border-radius: 10px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:rgb(112, 130, 161);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:rgb(142, 165, 204)\n"
"}\n"
"\n"
"")
        self.gridLayout = QGridLayout(Login)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 105)
        self.lb_login = QLabel(Login)
        self.lb_login.setObjectName(u"lb_login")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_login.sizePolicy().hasHeightForWidth())
        self.lb_login.setSizePolicy(sizePolicy)
        self.lb_login.setMaximumSize(QSize(16777215, 200))
        font = QFont()
        font.setFamily(u"Raleway")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.lb_login.setFont(font)
        self.lb_login.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_login, 0, 0, 1, 1)

        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(350, 250))
        self.frame.setMaximumSize(QSize(350, 250))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.input_usuario = QLineEdit(self.frame)
        self.input_usuario.setObjectName(u"input_usuario")
        self.input_usuario.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamily(u"Raleway")
        font1.setPointSize(10)
        self.input_usuario.setFont(font1)
        self.input_usuario.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.input_usuario)

        self.input_senha = QLineEdit(self.frame)
        self.input_senha.setObjectName(u"input_senha")
        self.input_senha.setMinimumSize(QSize(0, 30))
        self.input_senha.setFont(font1)
        self.input_senha.setStyleSheet(u"")
        self.input_senha.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.input_senha)

        self.btn_acessar = QPushButton(self.frame)
        self.btn_acessar.setObjectName(u"btn_acessar")
        self.btn_acessar.setMinimumSize(QSize(0, 30))
        self.btn_acessar.setMaximumSize(QSize(16777215, 35))
        font2 = QFont()
        font2.setFamily(u"Raleway")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_acessar.setFont(font2)

        self.verticalLayout.addWidget(self.btn_acessar)


        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)

        self.lb_mensagem = QLabel(Login)
        self.lb_mensagem.setObjectName(u"lb_mensagem")
        self.lb_mensagem.setMinimumSize(QSize(0, 0))
        self.lb_mensagem.setMaximumSize(QSize(16777215, 0))
        font3 = QFont()
        font3.setFamily(u"Raleway")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.lb_mensagem.setFont(font3)
        self.lb_mensagem.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"background-color: rgb(255, 164, 164)")
        self.lb_mensagem.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_mensagem, 1, 0, 1, 1)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.lb_login.setText(QCoreApplication.translate("Login", u"LOGIN", None))
        self.input_usuario.setPlaceholderText(QCoreApplication.translate("Login", u"USUARIO", None))
        self.input_senha.setPlaceholderText(QCoreApplication.translate("Login", u"SENHA", None))
        self.btn_acessar.setText(QCoreApplication.translate("Login", u"ACESSAR", None))
        self.lb_mensagem.setText(QCoreApplication.translate("Login", u"Usuario ou senha incorretos", None))
    # retranslateUi

