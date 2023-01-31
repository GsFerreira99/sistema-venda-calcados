# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'usuario_novoghERMt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_UsuarioNovo(object):
    def setupUi(self, UsuarioNovo):
        if not UsuarioNovo.objectName():
            UsuarioNovo.setObjectName(u"UsuarioNovo")
        UsuarioNovo.resize(480, 510)
        UsuarioNovo.setMinimumSize(QSize(480, 510))
        UsuarioNovo.setMaximumSize(QSize(480, 510))
        UsuarioNovo.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(236, 242, 248);\n"
"}\n"
"")
        self.gridLayout = QGridLayout(UsuarioNovo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(30, -1, 30, -1)
        self.frame_7 = QFrame(UsuarioNovo)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet(u"\n"
"QPushButton {\n"
"	border-radius: 10px;\n"
"	border: none;\n"
"	background-color: rgb(42, 68, 103);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(67, 110, 165);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(51, 83, 126);\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_42 = QFrame(self.frame_7)
        self.frame_42.setObjectName(u"frame_42")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_42.sizePolicy().hasHeightForWidth())
        self.frame_42.setSizePolicy(sizePolicy1)
        self.frame_42.setMinimumSize(QSize(300, 70))
        self.frame_42.setMaximumSize(QSize(300, 70))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.gridLayout_38 = QGridLayout(self.frame_42)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setContentsMargins(0, 9, 0, -1)
        self.label_33 = QLabel(self.frame_42)
        self.label_33.setObjectName(u"label_33")
        font = QFont()
        font.setFamily(u"Raleway")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)

        self.gridLayout_38.addWidget(self.label_33, 0, 0, 1, 1)

        self.input_usuario = QLineEdit(self.frame_42)
        self.input_usuario.setObjectName(u"input_usuario")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.input_usuario.sizePolicy().hasHeightForWidth())
        self.input_usuario.setSizePolicy(sizePolicy2)
        self.input_usuario.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamily(u"Raleway")
        self.input_usuario.setFont(font1)
        self.input_usuario.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_38.addWidget(self.input_usuario, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.frame_7)
        self.frame_43.setObjectName(u"frame_43")
        sizePolicy1.setHeightForWidth(self.frame_43.sizePolicy().hasHeightForWidth())
        self.frame_43.setSizePolicy(sizePolicy1)
        self.frame_43.setMinimumSize(QSize(300, 70))
        self.frame_43.setMaximumSize(QSize(300, 70))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.gridLayout_39 = QGridLayout(self.frame_43)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(0, 9, 0, -1)
        self.label_34 = QLabel(self.frame_43)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font)

        self.gridLayout_39.addWidget(self.label_34, 0, 0, 1, 1)

        self.input_senha = QLineEdit(self.frame_43)
        self.input_senha.setObjectName(u"input_senha")
        sizePolicy2.setHeightForWidth(self.input_senha.sizePolicy().hasHeightForWidth())
        self.input_senha.setSizePolicy(sizePolicy2)
        self.input_senha.setMaximumSize(QSize(16777215, 30))
        self.input_senha.setFont(font1)
        self.input_senha.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")
        self.input_senha.setEchoMode(QLineEdit.Password)

        self.gridLayout_39.addWidget(self.input_senha, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_43)

        self.frame_45 = QFrame(self.frame_7)
        self.frame_45.setObjectName(u"frame_45")
        sizePolicy1.setHeightForWidth(self.frame_45.sizePolicy().hasHeightForWidth())
        self.frame_45.setSizePolicy(sizePolicy1)
        self.frame_45.setMinimumSize(QSize(300, 70))
        self.frame_45.setMaximumSize(QSize(300, 70))
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.gridLayout_42 = QGridLayout(self.frame_45)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setContentsMargins(0, 9, 0, -1)
        self.label_37 = QLabel(self.frame_45)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font)

        self.gridLayout_42.addWidget(self.label_37, 0, 0, 1, 1)

        self.input_senhaComfirm = QLineEdit(self.frame_45)
        self.input_senhaComfirm.setObjectName(u"input_senhaComfirm")
        sizePolicy2.setHeightForWidth(self.input_senhaComfirm.sizePolicy().hasHeightForWidth())
        self.input_senhaComfirm.setSizePolicy(sizePolicy2)
        self.input_senhaComfirm.setMaximumSize(QSize(16777215, 30))
        self.input_senhaComfirm.setFont(font1)
        self.input_senhaComfirm.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")
        self.input_senhaComfirm.setEchoMode(QLineEdit.Password)

        self.gridLayout_42.addWidget(self.input_senhaComfirm, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_45)

        self.frame_41 = QFrame(self.frame_7)
        self.frame_41.setObjectName(u"frame_41")
        sizePolicy1.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy1)
        self.frame_41.setMinimumSize(QSize(300, 70))
        self.frame_41.setMaximumSize(QSize(300, 70))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.gridLayout_37 = QGridLayout(self.frame_41)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(0, 9, 0, -1)
        self.label_32 = QLabel(self.frame_41)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font)

        self.gridLayout_37.addWidget(self.label_32, 0, 0, 1, 1)

        self.input_nome = QLineEdit(self.frame_41)
        self.input_nome.setObjectName(u"input_nome")
        sizePolicy2.setHeightForWidth(self.input_nome.sizePolicy().hasHeightForWidth())
        self.input_nome.setSizePolicy(sizePolicy2)
        self.input_nome.setMaximumSize(QSize(16777215, 30))
        self.input_nome.setFont(font1)
        self.input_nome.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_37.addWidget(self.input_nome, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_41)

        self.frame_44 = QFrame(self.frame_7)
        self.frame_44.setObjectName(u"frame_44")
        sizePolicy1.setHeightForWidth(self.frame_44.sizePolicy().hasHeightForWidth())
        self.frame_44.setSizePolicy(sizePolicy1)
        self.frame_44.setMinimumSize(QSize(300, 70))
        self.frame_44.setMaximumSize(QSize(300, 70))
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.gridLayout_40 = QGridLayout(self.frame_44)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(0, 9, 0, -1)
        self.label_35 = QLabel(self.frame_44)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font)

        self.gridLayout_40.addWidget(self.label_35, 0, 0, 1, 1)

        self.input_sobrenome = QLineEdit(self.frame_44)
        self.input_sobrenome.setObjectName(u"input_sobrenome")
        sizePolicy2.setHeightForWidth(self.input_sobrenome.sizePolicy().hasHeightForWidth())
        self.input_sobrenome.setSizePolicy(sizePolicy2)
        self.input_sobrenome.setMaximumSize(QSize(16777215, 30))
        self.input_sobrenome.setFont(font1)
        self.input_sobrenome.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_40.addWidget(self.input_sobrenome, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_44)

        self.frame_14 = QFrame(self.frame_7)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(300, 70))
        self.frame_14.setMaximumSize(QSize(300, 70))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_14)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, -1, 0, -1)
        self.label_10 = QLabel(self.frame_14)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout_12.addWidget(self.label_10, 0, 0, 1, 1)

        self.input_tipo = QComboBox(self.frame_14)
        self.input_tipo.addItem("")
        self.input_tipo.addItem("")
        self.input_tipo.addItem("")
        self.input_tipo.setObjectName(u"input_tipo")
        sizePolicy.setHeightForWidth(self.input_tipo.sizePolicy().hasHeightForWidth())
        self.input_tipo.setSizePolicy(sizePolicy)
        self.input_tipo.setMaximumSize(QSize(300, 30))
        self.input_tipo.setStyleSheet(u"QComboBox {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")
        self.input_tipo.setEditable(True)
        self.input_tipo.setMaxVisibleItems(50)

        self.gridLayout_12.addWidget(self.input_tipo, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_14)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setMaximumSize(QSize(16777215, 60))
        self.frame_8.setStyleSheet(u"\n"
"QPushButton {\n"
"	border-radius: 10px;\n"
"	border: none;\n"
"	background-color: rgb(42, 68, 103);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(67, 110, 165);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(51, 83, 126);\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_salvar = QPushButton(self.frame_8)
        self.btn_salvar.setObjectName(u"btn_salvar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_salvar.sizePolicy().hasHeightForWidth())
        self.btn_salvar.setSizePolicy(sizePolicy3)
        self.btn_salvar.setMinimumSize(QSize(0, 35))
        self.btn_salvar.setMaximumSize(QSize(16777215, 35))
        font2 = QFont()
        font2.setFamily(u"Raleway")
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_salvar.setFont(font2)
        self.btn_salvar.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.btn_salvar)


        self.verticalLayout_2.addWidget(self.frame_8)


        self.gridLayout.addWidget(self.frame_7, 1, 1, 1, 1)

        self.label_3 = QLabel(UsuarioNovo)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMaximumSize(QSize(300, 50))
        font3 = QFont()
        font3.setFamily(u"Raleway")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.retranslateUi(UsuarioNovo)

        QMetaObject.connectSlotsByName(UsuarioNovo)
    # setupUi

    def retranslateUi(self, UsuarioNovo):
        UsuarioNovo.setWindowTitle(QCoreApplication.translate("UsuarioNovo", u"Form", None))
        self.label_33.setText(QCoreApplication.translate("UsuarioNovo", u"Usuario", None))
        self.label_34.setText(QCoreApplication.translate("UsuarioNovo", u"Senha", None))
        self.label_37.setText(QCoreApplication.translate("UsuarioNovo", u"Confirmar Senha", None))
        self.label_32.setText(QCoreApplication.translate("UsuarioNovo", u"Nome", None))
        self.label_35.setText(QCoreApplication.translate("UsuarioNovo", u"Sobrenome", None))
        self.label_10.setText(QCoreApplication.translate("UsuarioNovo", u"Tipo", None))
        self.input_tipo.setItemText(0, "")
        self.input_tipo.setItemText(1, QCoreApplication.translate("UsuarioNovo", u"USUARIO", None))
        self.input_tipo.setItemText(2, QCoreApplication.translate("UsuarioNovo", u"ADMINISTRADOR", None))

        self.btn_salvar.setText(QCoreApplication.translate("UsuarioNovo", u"Salvar", None))
        self.label_3.setText(QCoreApplication.translate("UsuarioNovo", u"Novo Usuario", None))
    # retranslateUi

