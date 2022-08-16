# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clientesnZEAUA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import interface.ui.resource_rc

class Ui_Cliente(object):
    def setupUi(self, Cliente):
        if not Cliente.objectName():
            Cliente.setObjectName(u"Cliente")
        Cliente.resize(900, 724)
        Cliente.setMinimumSize(QSize(900, 700))
        Cliente.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(236, 242, 248);\n"
"}\n"
"")
        self.gridLayout = QGridLayout(Cliente)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(30, 30, 30, 30)
        self.stackedWidget = QStackedWidget(Cliente)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QStackedWidget{\n"
"border:none;\n"
"border: 1px solid rgb(125, 125, 125);\n"
"border-radius: 10px;\n"
"margin: 5px;\n"
"margin-top:0;\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.consulta = QWidget()
        self.consulta.setObjectName(u"consulta")
        self.verticalLayout = QVBoxLayout(self.consulta)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(25, -1, 25, -1)
        self.frame = QFrame(self.consulta)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setFamily(u"Raleway")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.input_pesquisa = QLineEdit(self.frame_3)
        self.input_pesquisa.setObjectName(u"input_pesquisa")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.input_pesquisa.sizePolicy().hasHeightForWidth())
        self.input_pesquisa.setSizePolicy(sizePolicy2)
        self.input_pesquisa.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamily(u"Raleway")
        self.input_pesquisa.setFont(font1)
        self.input_pesquisa.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_3.addWidget(self.input_pesquisa, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamily(u"Raleway")
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.btn_busca = QPushButton(self.frame_3)
        self.btn_busca.setObjectName(u"btn_busca")
        self.btn_busca.setMaximumSize(QSize(40, 40))
        self.btn_busca.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	padding: 3px;\n"
"	image: url(:/icons/lupa.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	padding: 1px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding: 2px;;\n"
"}")

        self.gridLayout_3.addWidget(self.btn_busca, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.table_clientes = QTableWidget(self.consulta)
        if (self.table_clientes.columnCount() < 6):
            self.table_clientes.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_clientes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_clientes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_clientes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_clientes.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_clientes.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_clientes.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.table_clientes.setObjectName(u"table_clientes")
        font3 = QFont()
        font3.setFamily(u"Raleway")
        font3.setBold(True)
        font3.setWeight(75)
        self.table_clientes.setFont(font3)
        self.table_clientes.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	border: 1px solid black;\n"
"}")
        self.table_clientes.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.table_clientes)

        self.frame_4 = QFrame(self.consulta)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMaximumSize(QSize(16777215, 60))
        self.frame_4.setStyleSheet(u"\n"
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
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btn_deletar = QPushButton(self.frame_4)
        self.btn_deletar.setObjectName(u"btn_deletar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_deletar.sizePolicy().hasHeightForWidth())
        self.btn_deletar.setSizePolicy(sizePolicy3)
        self.btn_deletar.setMaximumSize(QSize(100, 35))
        font4 = QFont()
        font4.setFamily(u"Raleway")
        font4.setPointSize(9)
        font4.setBold(True)
        font4.setWeight(75)
        self.btn_deletar.setFont(font4)
        self.btn_deletar.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btn_deletar)

        self.btn_editar = QPushButton(self.frame_4)
        self.btn_editar.setObjectName(u"btn_editar")
        sizePolicy3.setHeightForWidth(self.btn_editar.sizePolicy().hasHeightForWidth())
        self.btn_editar.setSizePolicy(sizePolicy3)
        self.btn_editar.setMaximumSize(QSize(100, 35))
        self.btn_editar.setFont(font4)
        self.btn_editar.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btn_editar)


        self.verticalLayout.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.consulta)
        self.venda = QWidget()
        self.venda.setObjectName(u"venda")
        self.verticalLayout_2 = QVBoxLayout(self.venda)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.frame_5 = QFrame(self.venda)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMaximumSize(QSize(16777215, 100))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMaximumSize(QSize(300, 16777215))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_8 = QFrame(self.venda)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(9)
        self.gridLayout_8.setVerticalSpacing(0)
        self.gridLayout_8.setContentsMargins(0, -1, 0, -1)
        self.frame_27 = QFrame(self.frame_8)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy)
        self.frame_27.setMinimumSize(QSize(0, 70))
        self.frame_27.setMaximumSize(QSize(16777215, 70))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_27)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setHorizontalSpacing(30)
        self.gridLayout_24.setVerticalSpacing(9)
        self.gridLayout_24.setContentsMargins(10, 0, 0, 0)
        self.frame_33 = QFrame(self.frame_27)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMaximumSize(QSize(100, 70))
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_33)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 9, 0, -1)
        self.label_26 = QLabel(self.frame_33)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font2)

        self.gridLayout_30.addWidget(self.label_26, 0, 0, 1, 1)

        self.input_email = QLineEdit(self.frame_33)
        self.input_email.setObjectName(u"input_email")
        sizePolicy2.setHeightForWidth(self.input_email.sizePolicy().hasHeightForWidth())
        self.input_email.setSizePolicy(sizePolicy2)
        self.input_email.setMaximumSize(QSize(16777215, 30))
        self.input_email.setFont(font1)
        self.input_email.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_30.addWidget(self.input_email, 1, 0, 1, 1)


        self.gridLayout_24.addWidget(self.frame_33, 0, 4, 1, 1)

        self.frame_32 = QFrame(self.frame_27)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMaximumSize(QSize(110, 70))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_32)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 9, 0, -1)
        self.label_25 = QLabel(self.frame_32)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font2)

        self.gridLayout_29.addWidget(self.label_25, 0, 0, 1, 1)

        self.input_inscricaoEstadual = QLineEdit(self.frame_32)
        self.input_inscricaoEstadual.setObjectName(u"input_inscricaoEstadual")
        sizePolicy2.setHeightForWidth(self.input_inscricaoEstadual.sizePolicy().hasHeightForWidth())
        self.input_inscricaoEstadual.setSizePolicy(sizePolicy2)
        self.input_inscricaoEstadual.setMaximumSize(QSize(16777215, 30))
        self.input_inscricaoEstadual.setFont(font1)
        self.input_inscricaoEstadual.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_29.addWidget(self.input_inscricaoEstadual, 1, 0, 1, 1)


        self.gridLayout_24.addWidget(self.frame_32, 0, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_7, 0, 5, 1, 1)

        self.frame_31 = QFrame(self.frame_27)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(100, 70))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_31)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, 9, 0, -1)
        self.label_24 = QLabel(self.frame_31)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font2)

        self.gridLayout_28.addWidget(self.label_24, 0, 0, 1, 1)

        self.input_cpf = QLineEdit(self.frame_31)
        self.input_cpf.setObjectName(u"input_cpf")
        sizePolicy2.setHeightForWidth(self.input_cpf.sizePolicy().hasHeightForWidth())
        self.input_cpf.setSizePolicy(sizePolicy2)
        self.input_cpf.setMaximumSize(QSize(16777215, 30))
        self.input_cpf.setFont(font1)
        self.input_cpf.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_28.addWidget(self.input_cpf, 1, 0, 1, 1)


        self.gridLayout_24.addWidget(self.frame_31, 0, 1, 1, 1)

        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(100, 70))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_29)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 9, 0, -1)
        self.label_22 = QLabel(self.frame_29)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)

        self.gridLayout_26.addWidget(self.label_22, 0, 0, 1, 1)

        self.input_nascimento = QLineEdit(self.frame_29)
        self.input_nascimento.setObjectName(u"input_nascimento")
        sizePolicy2.setHeightForWidth(self.input_nascimento.sizePolicy().hasHeightForWidth())
        self.input_nascimento.setSizePolicy(sizePolicy2)
        self.input_nascimento.setMaximumSize(QSize(16777215, 30))
        self.input_nascimento.setFont(font1)
        self.input_nascimento.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_26.addWidget(self.input_nascimento, 1, 0, 1, 1)


        self.gridLayout_24.addWidget(self.frame_29, 0, 3, 1, 1)

        self.frame_30 = QFrame(self.frame_27)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(100, 70))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_30)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 9, 0, -1)
        self.label_23 = QLabel(self.frame_30)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font2)

        self.gridLayout_27.addWidget(self.label_23, 0, 0, 1, 1)

        self.input_tipo = QLineEdit(self.frame_30)
        self.input_tipo.setObjectName(u"input_tipo")
        sizePolicy2.setHeightForWidth(self.input_tipo.sizePolicy().hasHeightForWidth())
        self.input_tipo.setSizePolicy(sizePolicy2)
        self.input_tipo.setMaximumSize(QSize(16777215, 30))
        self.input_tipo.setFont(font1)
        self.input_tipo.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_27.addWidget(self.input_tipo, 1, 0, 1, 1)


        self.gridLayout_24.addWidget(self.frame_30, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_27, 1, 0, 1, 2)

        self.frame_28 = QFrame(self.frame_8)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy)
        self.frame_28.setMinimumSize(QSize(0, 70))
        self.frame_28.setMaximumSize(QSize(16777215, 70))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_28)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setHorizontalSpacing(30)
        self.gridLayout_25.setVerticalSpacing(9)
        self.gridLayout_25.setContentsMargins(10, 0, 0, 0)
        self.frame_48 = QFrame(self.frame_28)
        self.frame_48.setObjectName(u"frame_48")
        sizePolicy1.setHeightForWidth(self.frame_48.sizePolicy().hasHeightForWidth())
        self.frame_48.setSizePolicy(sizePolicy1)
        self.frame_48.setMinimumSize(QSize(300, 0))
        self.frame_48.setMaximumSize(QSize(400, 70))
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.gridLayout_44 = QGridLayout(self.frame_48)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setContentsMargins(0, 9, 0, -1)
        self.label_38 = QLabel(self.frame_48)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font2)

        self.gridLayout_44.addWidget(self.label_38, 0, 0, 1, 1)

        self.input_endereco = QLineEdit(self.frame_48)
        self.input_endereco.setObjectName(u"input_endereco")
        sizePolicy2.setHeightForWidth(self.input_endereco.sizePolicy().hasHeightForWidth())
        self.input_endereco.setSizePolicy(sizePolicy2)
        self.input_endereco.setMaximumSize(QSize(16777215, 30))
        self.input_endereco.setFont(font1)
        self.input_endereco.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_44.addWidget(self.input_endereco, 1, 0, 1, 1)


        self.gridLayout_25.addWidget(self.frame_48, 0, 1, 1, 1)

        self.frame_44 = QFrame(self.frame_28)
        self.frame_44.setObjectName(u"frame_44")
        sizePolicy1.setHeightForWidth(self.frame_44.sizePolicy().hasHeightForWidth())
        self.frame_44.setSizePolicy(sizePolicy1)
        self.frame_44.setMinimumSize(QSize(300, 0))
        self.frame_44.setMaximumSize(QSize(300, 70))
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.gridLayout_39 = QGridLayout(self.frame_44)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(0, 9, 0, -1)
        self.input_complemento = QLineEdit(self.frame_44)
        self.input_complemento.setObjectName(u"input_complemento")
        sizePolicy2.setHeightForWidth(self.input_complemento.sizePolicy().hasHeightForWidth())
        self.input_complemento.setSizePolicy(sizePolicy2)
        self.input_complemento.setMaximumSize(QSize(16777215, 30))
        self.input_complemento.setFont(font1)
        self.input_complemento.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_39.addWidget(self.input_complemento, 1, 0, 1, 1)

        self.label_28 = QLabel(self.frame_44)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)

        self.gridLayout_39.addWidget(self.label_28, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.frame_44, 0, 2, 1, 1)

        self.frame_49 = QFrame(self.frame_28)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(100, 0))
        self.frame_49.setMaximumSize(QSize(100, 70))
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.gridLayout_45 = QGridLayout(self.frame_49)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.gridLayout_45.setContentsMargins(0, 9, 0, -1)
        self.label_40 = QLabel(self.frame_49)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font2)

        self.gridLayout_45.addWidget(self.label_40, 0, 0, 1, 1)

        self.input_cep = QLineEdit(self.frame_49)
        self.input_cep.setObjectName(u"input_cep")
        sizePolicy2.setHeightForWidth(self.input_cep.sizePolicy().hasHeightForWidth())
        self.input_cep.setSizePolicy(sizePolicy2)
        self.input_cep.setMaximumSize(QSize(16777215, 30))
        self.input_cep.setFont(font1)
        self.input_cep.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_45.addWidget(self.input_cep, 1, 0, 1, 1)


        self.gridLayout_25.addWidget(self.frame_49, 0, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_10, 0, 3, 1, 1)


        self.gridLayout_8.addWidget(self.frame_28, 2, 0, 1, 1)

        self.frame_46 = QFrame(self.frame_8)
        self.frame_46.setObjectName(u"frame_46")
        sizePolicy.setHeightForWidth(self.frame_46.sizePolicy().hasHeightForWidth())
        self.frame_46.setSizePolicy(sizePolicy)
        self.frame_46.setMinimumSize(QSize(0, 70))
        self.frame_46.setMaximumSize(QSize(16777215, 70))
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.gridLayout_41 = QGridLayout(self.frame_46)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setHorizontalSpacing(30)
        self.gridLayout_41.setVerticalSpacing(9)
        self.gridLayout_41.setContentsMargins(10, 0, 0, 0)
        self.frame_50 = QFrame(self.frame_46)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMaximumSize(QSize(150, 70))
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.gridLayout_47 = QGridLayout(self.frame_50)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.gridLayout_47.setContentsMargins(0, 9, 0, -1)
        self.label_41 = QLabel(self.frame_50)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font2)

        self.gridLayout_47.addWidget(self.label_41, 0, 0, 1, 1)

        self.input_cidade = QLineEdit(self.frame_50)
        self.input_cidade.setObjectName(u"input_cidade")
        sizePolicy2.setHeightForWidth(self.input_cidade.sizePolicy().hasHeightForWidth())
        self.input_cidade.setSizePolicy(sizePolicy2)
        self.input_cidade.setMaximumSize(QSize(16777215, 30))
        self.input_cidade.setFont(font1)
        self.input_cidade.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_47.addWidget(self.input_cidade, 1, 0, 1, 1)


        self.gridLayout_41.addWidget(self.frame_50, 0, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_41.addItem(self.horizontalSpacer_9, 0, 3, 1, 1)

        self.frame_52 = QFrame(self.frame_46)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMaximumSize(QSize(50, 70))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.gridLayout_49 = QGridLayout(self.frame_52)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.gridLayout_49.setContentsMargins(0, 9, 0, -1)
        self.label_37 = QLabel(self.frame_52)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font2)

        self.gridLayout_49.addWidget(self.label_37, 0, 0, 1, 1)

        self.input_uf = QLineEdit(self.frame_52)
        self.input_uf.setObjectName(u"input_uf")
        sizePolicy2.setHeightForWidth(self.input_uf.sizePolicy().hasHeightForWidth())
        self.input_uf.setSizePolicy(sizePolicy2)
        self.input_uf.setMaximumSize(QSize(16777215, 30))
        self.input_uf.setFont(font1)
        self.input_uf.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_49.addWidget(self.input_uf, 1, 0, 1, 1)


        self.gridLayout_41.addWidget(self.frame_52, 0, 2, 1, 1)

        self.frame_51 = QFrame(self.frame_46)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMaximumSize(QSize(150, 70))
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.gridLayout_48 = QGridLayout(self.frame_51)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_48.setContentsMargins(0, 9, 0, -1)
        self.label_42 = QLabel(self.frame_51)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font2)

        self.gridLayout_48.addWidget(self.label_42, 0, 0, 1, 1)

        self.input_bairro = QLineEdit(self.frame_51)
        self.input_bairro.setObjectName(u"input_bairro")
        sizePolicy2.setHeightForWidth(self.input_bairro.sizePolicy().hasHeightForWidth())
        self.input_bairro.setSizePolicy(sizePolicy2)
        self.input_bairro.setMaximumSize(QSize(16777215, 30))
        self.input_bairro.setFont(font1)
        self.input_bairro.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_48.addWidget(self.input_bairro, 1, 0, 1, 1)


        self.gridLayout_41.addWidget(self.frame_51, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_46, 3, 0, 1, 1)

        self.frame_35 = QFrame(self.frame_8)
        self.frame_35.setObjectName(u"frame_35")
        sizePolicy.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy)
        self.frame_35.setMinimumSize(QSize(0, 70))
        self.frame_35.setMaximumSize(QSize(16777215, 200))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.gridLayout_32 = QGridLayout(self.frame_35)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setHorizontalSpacing(0)
        self.gridLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_39 = QFrame(self.frame_35)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(350, 0))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.gridLayout_42 = QGridLayout(self.frame_39)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setHorizontalSpacing(0)
        self.gridLayout_42.setContentsMargins(0, 9, 0, -1)
        self.label_33 = QLabel(self.frame_39)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(16777215, 20))
        self.label_33.setFont(font2)

        self.gridLayout_42.addWidget(self.label_33, 0, 0, 1, 1)

        self.input_observacao = QTextEdit(self.frame_39)
        self.input_observacao.setObjectName(u"input_observacao")
        self.input_observacao.setMaximumSize(QSize(300, 16777215))
        self.input_observacao.setStyleSheet(u"QTextEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_42.addWidget(self.input_observacao, 1, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_42.addItem(self.horizontalSpacer_5, 1, 1, 1, 1)


        self.gridLayout_32.addWidget(self.frame_39, 0, 0, 2, 1)


        self.gridLayout_8.addWidget(self.frame_35, 4, 0, 1, 1)

        self.frame_34 = QFrame(self.frame_8)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy)
        self.frame_34.setMinimumSize(QSize(0, 70))
        self.frame_34.setMaximumSize(QSize(16777215, 70))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.frame_37 = QFrame(self.frame_34)
        self.frame_37.setObjectName(u"frame_37")
        sizePolicy1.setHeightForWidth(self.frame_37.sizePolicy().hasHeightForWidth())
        self.frame_37.setSizePolicy(sizePolicy1)
        self.frame_37.setMaximumSize(QSize(80, 70))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.gridLayout_34 = QGridLayout(self.frame_37)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setContentsMargins(0, 9, 0, -1)
        self.label_29 = QLabel(self.frame_37)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font2)

        self.gridLayout_34.addWidget(self.label_29, 0, 0, 1, 1)

        self.input_codigo = QLineEdit(self.frame_37)
        self.input_codigo.setObjectName(u"input_codigo")
        sizePolicy2.setHeightForWidth(self.input_codigo.sizePolicy().hasHeightForWidth())
        self.input_codigo.setSizePolicy(sizePolicy2)
        self.input_codigo.setMaximumSize(QSize(16777215, 30))
        self.input_codigo.setFont(font1)
        self.input_codigo.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_34.addWidget(self.input_codigo, 1, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_37)

        self.frame_42 = QFrame(self.frame_34)
        self.frame_42.setObjectName(u"frame_42")
        sizePolicy1.setHeightForWidth(self.frame_42.sizePolicy().hasHeightForWidth())
        self.frame_42.setSizePolicy(sizePolicy1)
        self.frame_42.setMaximumSize(QSize(130, 70))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.gridLayout_38 = QGridLayout(self.frame_42)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setContentsMargins(0, 9, 0, -1)
        self.label_35 = QLabel(self.frame_42)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font2)

        self.gridLayout_38.addWidget(self.label_35, 0, 0, 1, 1)

        self.input_data = QLineEdit(self.frame_42)
        self.input_data.setObjectName(u"input_data")
        sizePolicy2.setHeightForWidth(self.input_data.sizePolicy().hasHeightForWidth())
        self.input_data.setSizePolicy(sizePolicy2)
        self.input_data.setMaximumSize(QSize(100, 30))
        self.input_data.setFont(font1)
        self.input_data.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_38.addWidget(self.input_data, 1, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_42)

        self.frame_41 = QFrame(self.frame_34)
        self.frame_41.setObjectName(u"frame_41")
        sizePolicy1.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy1)
        self.frame_41.setMinimumSize(QSize(300, 0))
        self.frame_41.setMaximumSize(QSize(300, 70))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.gridLayout_37 = QGridLayout(self.frame_41)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(0, 9, 0, -1)
        self.label_32 = QLabel(self.frame_41)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font2)

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


        self.horizontalLayout_4.addWidget(self.frame_41)

        self.frame_40 = QFrame(self.frame_34)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy1.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy1)
        self.frame_40.setMaximumSize(QSize(130, 70))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.gridLayout_36 = QGridLayout(self.frame_40)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(0, 9, 0, -1)
        self.label_31 = QLabel(self.frame_40)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)

        self.gridLayout_36.addWidget(self.label_31, 0, 0, 1, 1)

        self.input_celular = QLineEdit(self.frame_40)
        self.input_celular.setObjectName(u"input_celular")
        sizePolicy2.setHeightForWidth(self.input_celular.sizePolicy().hasHeightForWidth())
        self.input_celular.setSizePolicy(sizePolicy2)
        self.input_celular.setMaximumSize(QSize(100, 30))
        self.input_celular.setFont(font1)
        self.input_celular.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_36.addWidget(self.input_celular, 1, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_40)

        self.frame_38 = QFrame(self.frame_34)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy1.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy1)
        self.frame_38.setMaximumSize(QSize(100, 70))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.gridLayout_35 = QGridLayout(self.frame_38)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(0, 9, 0, -1)
        self.label_30 = QLabel(self.frame_38)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)

        self.gridLayout_35.addWidget(self.label_30, 0, 0, 1, 1)

        self.input_telefone = QLineEdit(self.frame_38)
        self.input_telefone.setObjectName(u"input_telefone")
        sizePolicy2.setHeightForWidth(self.input_telefone.sizePolicy().hasHeightForWidth())
        self.input_telefone.setSizePolicy(sizePolicy2)
        self.input_telefone.setMaximumSize(QSize(100, 30))
        self.input_telefone.setFont(font1)
        self.input_telefone.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_35.addWidget(self.input_telefone, 1, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_38)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)


        self.gridLayout_8.addWidget(self.frame_34, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.venda)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMaximumSize(QSize(16777215, 60))
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
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_salvar = QPushButton(self.frame_7)
        self.btn_salvar.setObjectName(u"btn_salvar")
        sizePolicy3.setHeightForWidth(self.btn_salvar.sizePolicy().hasHeightForWidth())
        self.btn_salvar.setSizePolicy(sizePolicy3)
        self.btn_salvar.setMinimumSize(QSize(0, 35))
        self.btn_salvar.setMaximumSize(QSize(200, 35))
        self.btn_salvar.setFont(font4)
        self.btn_salvar.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.btn_salvar)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.venda)

        self.gridLayout.addWidget(self.stackedWidget, 2, 0, 1, 1)

        self.frame_2 = QFrame(Cliente)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, 0, 0, 0)
        self.btn_consulta = QPushButton(self.frame_2)
        self.btn_consulta.setObjectName(u"btn_consulta")
        sizePolicy3.setHeightForWidth(self.btn_consulta.sizePolicy().hasHeightForWidth())
        self.btn_consulta.setSizePolicy(sizePolicy3)
        self.btn_consulta.setMinimumSize(QSize(0, 40))
        self.btn_consulta.setMaximumSize(QSize(100, 40))
        self.btn_consulta.setFont(font4)
        self.btn_consulta.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 0;\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"	background-color: rgb(74, 121, 184)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(89, 146, 221)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(42, 68, 103)\n"
"}")

        self.horizontalLayout.addWidget(self.btn_consulta)

        self.btn_novo = QPushButton(self.frame_2)
        self.btn_novo.setObjectName(u"btn_novo")
        sizePolicy3.setHeightForWidth(self.btn_novo.sizePolicy().hasHeightForWidth())
        self.btn_novo.setSizePolicy(sizePolicy3)
        self.btn_novo.setMinimumSize(QSize(0, 40))
        self.btn_novo.setMaximumSize(QSize(100, 40))
        self.btn_novo.setFont(font4)
        self.btn_novo.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 0;\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"	background-color: rgb(74, 121, 184)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(89, 146, 221)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(42, 68, 103)\n"
"}")

        self.horizontalLayout.addWidget(self.btn_novo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)


        self.retranslateUi(Cliente)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Cliente)
    # setupUi

    def retranslateUi(self, Cliente):
        Cliente.setWindowTitle(QCoreApplication.translate("Cliente", u"Form", None))
        self.label.setText(QCoreApplication.translate("Cliente", u"Consultar Clientes", None))
        self.label_2.setText(QCoreApplication.translate("Cliente", u"Pesquisar", None))
        self.btn_busca.setText("")
        ___qtablewidgetitem = self.table_clientes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Cliente", u"C\u00f3digo", None));
        ___qtablewidgetitem1 = self.table_clientes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Cliente", u"Nome", None));
        ___qtablewidgetitem2 = self.table_clientes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Cliente", u"Celular", None));
        ___qtablewidgetitem3 = self.table_clientes.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Cliente", u"CPF/CNPJ", None));
        ___qtablewidgetitem4 = self.table_clientes.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Cliente", u"Inscri\u00e7\u00e3o Estadual", None));
        ___qtablewidgetitem5 = self.table_clientes.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Cliente", u"Email", None));
        self.btn_deletar.setText(QCoreApplication.translate("Cliente", u"Deletar", None))
        self.btn_editar.setText(QCoreApplication.translate("Cliente", u"Editar", None))
        self.label_3.setText(QCoreApplication.translate("Cliente", u"Cadastrar Novo Cliente", None))
        self.label_26.setText(QCoreApplication.translate("Cliente", u"Email", None))
        self.label_25.setText(QCoreApplication.translate("Cliente", u"Inscri\u00e7\u00e3o Estadual", None))
        self.label_24.setText(QCoreApplication.translate("Cliente", u"CPF/CNPJ", None))
        self.label_22.setText(QCoreApplication.translate("Cliente", u"Data Nascimento", None))
        self.label_23.setText(QCoreApplication.translate("Cliente", u"Tipo", None))
        self.label_38.setText(QCoreApplication.translate("Cliente", u"Endere\u00e7o", None))
        self.label_28.setText(QCoreApplication.translate("Cliente", u"Complemento", None))
        self.label_40.setText(QCoreApplication.translate("Cliente", u"CEP", None))
        self.label_41.setText(QCoreApplication.translate("Cliente", u"Cidade", None))
        self.label_37.setText(QCoreApplication.translate("Cliente", u"UF", None))
        self.label_42.setText(QCoreApplication.translate("Cliente", u"Bairro", None))
        self.label_33.setText(QCoreApplication.translate("Cliente", u"Observa\u00e7\u00e3o", None))
        self.label_29.setText(QCoreApplication.translate("Cliente", u"C\u00f3digo", None))
        self.label_35.setText(QCoreApplication.translate("Cliente", u"Data Cadastro", None))
        self.label_32.setText(QCoreApplication.translate("Cliente", u"Nome Cliente", None))
        self.label_31.setText(QCoreApplication.translate("Cliente", u"Celular", None))
        self.label_30.setText(QCoreApplication.translate("Cliente", u"Telefone", None))
        self.input_telefone.setText("")
        self.btn_salvar.setText(QCoreApplication.translate("Cliente", u"Salvar", None))
        self.btn_consulta.setText(QCoreApplication.translate("Cliente", u"Consultar", None))
        self.btn_novo.setText(QCoreApplication.translate("Cliente", u"Novo", None))
    # retranslateUi

