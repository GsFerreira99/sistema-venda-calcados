# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homejZoPvD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import interface.ui.resource_rc

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(1034, 661)
        Home.setStyleSheet(u"QWidget{\n"
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
        self.gridLayout = QGridLayout(Home)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.left_bar = QFrame(Home)
        self.left_bar.setObjectName(u"left_bar")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_bar.sizePolicy().hasHeightForWidth())
        self.left_bar.setSizePolicy(sizePolicy)
        self.left_bar.setMinimumSize(QSize(0, 0))
        self.left_bar.setMaximumSize(QSize(150, 16777215))
        self.left_bar.setStyleSheet(u"background-color: rgb(149, 172, 213);\n"
"border-right: 3px solid rgb(125, 133, 147)")
        self.left_bar.setFrameShape(QFrame.StyledPanel)
        self.left_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.left_bar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 2, 0)
        self.btn_vendas = QPushButton(self.left_bar)
        self.btn_vendas.setObjectName(u"btn_vendas")
        self.btn_vendas.setMinimumSize(QSize(0, 40))
        self.btn_vendas.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamily(u"Raleway")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_vendas.setFont(font)
        self.btn_vendas.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: none;\n"
"	border-bottom: 1px solid rgb(42, 68, 103)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-bottom: 2px solid rgb(42, 68, 103);\n"
"	background-color: rgb(139, 161, 199)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:rgb(124, 143, 177)\n"
"}")

        self.verticalLayout.addWidget(self.btn_vendas)

        self.btn_estoque = QPushButton(self.left_bar)
        self.btn_estoque.setObjectName(u"btn_estoque")
        self.btn_estoque.setMinimumSize(QSize(0, 40))
        self.btn_estoque.setMaximumSize(QSize(16777215, 40))
        self.btn_estoque.setFont(font)
        self.btn_estoque.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: none;\n"
"	border-bottom: 1px solid rgb(42, 68, 103)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-bottom: 2px solid rgb(42, 68, 103);\n"
"	background-color: rgb(139, 161, 199)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:rgb(124, 143, 177)\n"
"}")

        self.verticalLayout.addWidget(self.btn_estoque)

        self.btn_clientes = QPushButton(self.left_bar)
        self.btn_clientes.setObjectName(u"btn_clientes")
        self.btn_clientes.setMinimumSize(QSize(0, 40))
        self.btn_clientes.setMaximumSize(QSize(16777215, 40))
        self.btn_clientes.setFont(font)
        self.btn_clientes.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: none;\n"
"	border-bottom: 1px solid rgb(42, 68, 103)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-bottom: 2px solid rgb(42, 68, 103);\n"
"	background-color: rgb(139, 161, 199)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:rgb(124, 143, 177)\n"
"}")

        self.verticalLayout.addWidget(self.btn_clientes)

        self.btn_fornecedores = QPushButton(self.left_bar)
        self.btn_fornecedores.setObjectName(u"btn_fornecedores")
        self.btn_fornecedores.setMinimumSize(QSize(0, 40))
        self.btn_fornecedores.setMaximumSize(QSize(16777215, 40))
        self.btn_fornecedores.setFont(font)
        self.btn_fornecedores.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: none;\n"
"	border-bottom: 1px solid rgb(42, 68, 103)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-bottom: 2px solid rgb(42, 68, 103);\n"
"	background-color: rgb(139, 161, 199)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:rgb(124, 143, 177)\n"
"}")

        self.verticalLayout.addWidget(self.btn_fornecedores)

        self.btn_relatorios = QPushButton(self.left_bar)
        self.btn_relatorios.setObjectName(u"btn_relatorios")
        self.btn_relatorios.setMinimumSize(QSize(0, 40))
        self.btn_relatorios.setMaximumSize(QSize(16777215, 40))
        self.btn_relatorios.setFont(font)
        self.btn_relatorios.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: none;\n"
"	border-bottom: 1px solid rgb(42, 68, 103)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-bottom: 2px solid rgb(42, 68, 103);\n"
"	background-color: rgb(139, 161, 199)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:rgb(124, 143, 177)\n"
"}")

        self.verticalLayout.addWidget(self.btn_relatorios)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.left_bar, 1, 0, 2, 1)

        self.top_bar = QFrame(Home)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMinimumSize(QSize(0, 40))
        self.top_bar.setMaximumSize(QSize(16777215, 40))
        self.top_bar.setStyleSheet(u"background-color: rgb(42, 68, 103);\n"
"border-bottom: 3px solid rgb(115, 128, 149)")
        self.top_bar.setFrameShape(QFrame.StyledPanel)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_menu = QPushButton(self.top_bar)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setMaximumSize(QSize(150, 40))
        self.btn_menu.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: none;\n"
"	image: url(:/icons/hamb.png);\n"
"	padding: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	padding: 1px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"		padding: 2px;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_menu)

        self.lb_titulo = QLabel(self.top_bar)
        self.lb_titulo.setObjectName(u"lb_titulo")
        font1 = QFont()
        font1.setFamily(u"Raleway")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.lb_titulo.setFont(font1)
        self.lb_titulo.setStyleSheet(u"color: white")
        self.lb_titulo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_titulo)


        self.gridLayout.addWidget(self.top_bar, 0, 0, 1, 2)

        self.content = QStackedWidget(Home)
        self.content.setObjectName(u"content")
        sizePolicy.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.content, 1, 1, 1, 1)


        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"Form", None))
        self.btn_vendas.setText(QCoreApplication.translate("Home", u"Vendas", None))
        self.btn_estoque.setText(QCoreApplication.translate("Home", u"Estoque", None))
        self.btn_clientes.setText(QCoreApplication.translate("Home", u"Clientes", None))
        self.btn_fornecedores.setText(QCoreApplication.translate("Home", u"Fornecedores", None))
        self.btn_relatorios.setText(QCoreApplication.translate("Home", u"Relat\u00f3rios", None))
        self.btn_menu.setText("")
        self.lb_titulo.setText(QCoreApplication.translate("Home", u"HOME", None))
    # retranslateUi

