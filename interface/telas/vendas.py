# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vendaslbqsLF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import interface.ui.resource_rc

class Ui_Vendas(object):
    def setupUi(self, Vendas):
        if not Vendas.objectName():
            Vendas.setObjectName(u"Vendas")
        Vendas.resize(1237, 813)
        Vendas.setMinimumSize(QSize(900, 700))
        Vendas.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(236, 242, 248);\n"
"}\n"
"")
        self.gridLayout = QGridLayout(Vendas)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(30, 30, 30, 30)
        self.stackedWidget = QStackedWidget(Vendas)
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
        self.frame_periodo = QFrame(self.frame_3)
        self.frame_periodo.setObjectName(u"frame_periodo")
        sizePolicy.setHeightForWidth(self.frame_periodo.sizePolicy().hasHeightForWidth())
        self.frame_periodo.setSizePolicy(sizePolicy)
        self.frame_periodo.setMinimumSize(QSize(0, 0))
        self.frame_periodo.setMaximumSize(QSize(0, 100))
        self.frame_periodo.setFrameShape(QFrame.StyledPanel)
        self.frame_periodo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_periodo)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.input_data_ini = QDateEdit(self.frame_periodo)
        self.input_data_ini.setObjectName(u"input_data_ini")
        self.input_data_ini.setMinimumSize(QSize(0, 30))
        self.input_data_ini.setMaximumSize(QSize(16777215, 30))
        self.input_data_ini.setStyleSheet(u"QDateEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 8px;\n"
"}")
        self.input_data_ini.setCalendarPopup(True)

        self.horizontalLayout_5.addWidget(self.input_data_ini)

        self.label_22 = QLabel(self.frame_periodo)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(10, 16777215))
        font1 = QFont()
        font1.setFamily(u"Raleway")
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_22.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_22)

        self.input_data_fim = QDateEdit(self.frame_periodo)
        self.input_data_fim.setObjectName(u"input_data_fim")
        self.input_data_fim.setMinimumSize(QSize(0, 30))
        self.input_data_fim.setMaximumSize(QSize(16777215, 30))
        self.input_data_fim.setStyleSheet(u"QDateEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 8px;\n"
"}")
        self.input_data_fim.setCalendarPopup(True)

        self.horizontalLayout_5.addWidget(self.input_data_fim)


        self.gridLayout_3.addWidget(self.frame_periodo, 1, 2, 1, 1)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

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

        self.gridLayout_3.addWidget(self.btn_busca, 1, 3, 1, 1)

        self.input_pesquisa = QLineEdit(self.frame_3)
        self.input_pesquisa.setObjectName(u"input_pesquisa")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.input_pesquisa.sizePolicy().hasHeightForWidth())
        self.input_pesquisa.setSizePolicy(sizePolicy2)
        self.input_pesquisa.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamily(u"Raleway")
        self.input_pesquisa.setFont(font2)
        self.input_pesquisa.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_3.addWidget(self.input_pesquisa, 1, 0, 1, 1)

        self.radio_periodo = QRadioButton(self.frame_3)
        self.radio_periodo.setObjectName(u"radio_periodo")

        self.gridLayout_3.addWidget(self.radio_periodo, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.table_vendas = QTableWidget(self.consulta)
        if (self.table_vendas.columnCount() < 6):
            self.table_vendas.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_vendas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_vendas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_vendas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_vendas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_vendas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_vendas.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.table_vendas.setObjectName(u"table_vendas")
        font3 = QFont()
        font3.setFamily(u"Raleway")
        font3.setBold(True)
        font3.setWeight(75)
        self.table_vendas.setFont(font3)
        self.table_vendas.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	border: 1px solid black;\n"
"}")
        self.table_vendas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_vendas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_vendas.horizontalHeader().setStretchLastSection(True)
        self.table_vendas.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.table_vendas)

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

        self.btn_relatorio_geral = QPushButton(self.frame_4)
        self.btn_relatorio_geral.setObjectName(u"btn_relatorio_geral")
        sizePolicy3.setHeightForWidth(self.btn_relatorio_geral.sizePolicy().hasHeightForWidth())
        self.btn_relatorio_geral.setSizePolicy(sizePolicy3)
        self.btn_relatorio_geral.setMaximumSize(QSize(130, 35))
        self.btn_relatorio_geral.setFont(font4)
        self.btn_relatorio_geral.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btn_relatorio_geral)


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

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(200, 70))
        self.frame_6.setMaximumSize(QSize(200, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)

        self.input_cliente = QComboBox(self.frame_6)
        self.input_cliente.addItem("")
        self.input_cliente.addItem("")
        self.input_cliente.addItem("")
        self.input_cliente.addItem("")
        self.input_cliente.addItem("")
        self.input_cliente.setObjectName(u"input_cliente")
        sizePolicy.setHeightForWidth(self.input_cliente.sizePolicy().hasHeightForWidth())
        self.input_cliente.setSizePolicy(sizePolicy)
        self.input_cliente.setMaximumSize(QSize(16777215, 30))
        self.input_cliente.setStyleSheet(u"QComboBox {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_5.addWidget(self.input_cliente, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_6, 0, 4, 1, 1)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 70))
        self.frame_9.setMaximumSize(QSize(150, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_9)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)

        self.input_data = QDateEdit(self.frame_9)
        self.input_data.setObjectName(u"input_data")
        self.input_data.setMinimumSize(QSize(0, 30))
        self.input_data.setMaximumSize(QSize(16777215, 30))
        self.input_data.setStyleSheet(u"QDateEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 8px;\n"
"}")
        self.input_data.setCalendarPopup(True)

        self.gridLayout_6.addWidget(self.input_data, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_9, 0, 3, 1, 1)

        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setMinimumSize(QSize(75, 70))
        self.frame_10.setMaximumSize(QSize(75, 16777215))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_10)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 1)

        self.input_nrVenda = QLineEdit(self.frame_10)
        self.input_nrVenda.setObjectName(u"input_nrVenda")
        sizePolicy2.setHeightForWidth(self.input_nrVenda.sizePolicy().hasHeightForWidth())
        self.input_nrVenda.setSizePolicy(sizePolicy2)
        self.input_nrVenda.setMaximumSize(QSize(16777215, 30))
        self.input_nrVenda.setFont(font2)
        self.input_nrVenda.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_7.addWidget(self.input_nrVenda, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_10, 0, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_8 = QFrame(self.venda)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(9)
        self.gridLayout_8.setVerticalSpacing(8)
        self.gridLayout_8.setContentsMargins(0, -1, 0, -1)
        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 70))
        self.frame_11.setMaximumSize(QSize(75, 70))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_11)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 9, 0, -1)
        self.label_7 = QLabel(self.frame_11)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout_9.addWidget(self.label_7, 0, 0, 1, 1)

        self.input_quantidade = QLineEdit(self.frame_11)
        self.input_quantidade.setObjectName(u"input_quantidade")
        sizePolicy2.setHeightForWidth(self.input_quantidade.sizePolicy().hasHeightForWidth())
        self.input_quantidade.setSizePolicy(sizePolicy2)
        self.input_quantidade.setMaximumSize(QSize(16777215, 30))
        self.input_quantidade.setFont(font2)
        self.input_quantidade.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_9.addWidget(self.input_quantidade, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_11, 0, 0, 1, 1)

        self.frame_12 = QFrame(self.frame_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(100, 70))
        self.frame_12.setMaximumSize(QSize(100, 70))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_12)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, -1, 0, -1)
        self.label_8 = QLabel(self.frame_12)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout_10.addWidget(self.label_8, 0, 0, 1, 1)

        self.input_preco = QLineEdit(self.frame_12)
        self.input_preco.setObjectName(u"input_preco")
        sizePolicy2.setHeightForWidth(self.input_preco.sizePolicy().hasHeightForWidth())
        self.input_preco.setSizePolicy(sizePolicy2)
        self.input_preco.setMaximumSize(QSize(16777215, 30))
        self.input_preco.setFont(font2)
        self.input_preco.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_10.addWidget(self.input_preco, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_12, 0, 5, 1, 1)

        self.btn_add = QPushButton(self.frame_8)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMaximumSize(QSize(40, 40))
        self.btn_add.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	padding: 3px;\n"
"	image: url(:/icons/adicionar.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	padding: 1px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	padding: 2px;\n"
"}")

        self.gridLayout_8.addWidget(self.btn_add, 1, 6, 1, 1)

        self.frame_13 = QFrame(self.frame_8)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(75, 70))
        self.frame_13.setMaximumSize(QSize(500, 70))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_13)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, -1, 0, -1)
        self.label_9 = QLabel(self.frame_13)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout_11.addWidget(self.label_9, 0, 0, 1, 1)

        self.input_tamanho = QLineEdit(self.frame_13)
        self.input_tamanho.setObjectName(u"input_tamanho")
        sizePolicy2.setHeightForWidth(self.input_tamanho.sizePolicy().hasHeightForWidth())
        self.input_tamanho.setSizePolicy(sizePolicy2)
        self.input_tamanho.setMaximumSize(QSize(16777215, 30))
        self.input_tamanho.setFont(font2)
        self.input_tamanho.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_11.addWidget(self.input_tamanho, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_13, 0, 4, 1, 1)

        self.frame_22 = QFrame(self.frame_8)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setMinimumSize(QSize(0, 70))
        self.frame_22.setMaximumSize(QSize(16777215, 70))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_22)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_22)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(100, 70))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_18)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 9, 0, -1)
        self.label_13 = QLabel(self.frame_18)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.gridLayout_15.addWidget(self.label_13, 0, 0, 1, 1)

        self.input_totalLiquido = QLineEdit(self.frame_18)
        self.input_totalLiquido.setObjectName(u"input_totalLiquido")
        sizePolicy2.setHeightForWidth(self.input_totalLiquido.sizePolicy().hasHeightForWidth())
        self.input_totalLiquido.setSizePolicy(sizePolicy2)
        self.input_totalLiquido.setMaximumSize(QSize(16777215, 30))
        self.input_totalLiquido.setFont(font2)
        self.input_totalLiquido.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")
        self.input_totalLiquido.setReadOnly(True)

        self.gridLayout_15.addWidget(self.input_totalLiquido, 1, 0, 1, 1)


        self.gridLayout_19.addWidget(self.frame_18, 0, 2, 1, 1)

        self.frame_21 = QFrame(self.frame_22)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(100, 70))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_21)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 9, 0, -1)
        self.label_16 = QLabel(self.frame_21)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.gridLayout_18.addWidget(self.label_16, 0, 0, 1, 1)

        self.input_troco = QLineEdit(self.frame_21)
        self.input_troco.setObjectName(u"input_troco")
        sizePolicy2.setHeightForWidth(self.input_troco.sizePolicy().hasHeightForWidth())
        self.input_troco.setSizePolicy(sizePolicy2)
        self.input_troco.setMaximumSize(QSize(16777215, 30))
        self.input_troco.setFont(font2)
        self.input_troco.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")
        self.input_troco.setReadOnly(True)

        self.gridLayout_18.addWidget(self.input_troco, 1, 0, 1, 1)


        self.gridLayout_19.addWidget(self.frame_21, 0, 5, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_5, 0, 6, 1, 1)

        self.frame_20 = QFrame(self.frame_22)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(100, 70))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_20)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 9, 0, -1)
        self.label_15 = QLabel(self.frame_20)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.gridLayout_17.addWidget(self.label_15, 0, 0, 1, 1)

        self.input_totalPago = QLineEdit(self.frame_20)
        self.input_totalPago.setObjectName(u"input_totalPago")
        sizePolicy2.setHeightForWidth(self.input_totalPago.sizePolicy().hasHeightForWidth())
        self.input_totalPago.setSizePolicy(sizePolicy2)
        self.input_totalPago.setMaximumSize(QSize(16777215, 30))
        self.input_totalPago.setFont(font2)
        self.input_totalPago.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_17.addWidget(self.input_totalPago, 1, 0, 1, 1)


        self.gridLayout_19.addWidget(self.frame_20, 0, 4, 1, 1)

        self.frame_16 = QFrame(self.frame_22)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(100, 70))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_16)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 9, 0, -1)
        self.label_11 = QLabel(self.frame_16)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.gridLayout_13.addWidget(self.label_11, 0, 0, 1, 1)

        self.input_totalBruto = QLineEdit(self.frame_16)
        self.input_totalBruto.setObjectName(u"input_totalBruto")
        sizePolicy2.setHeightForWidth(self.input_totalBruto.sizePolicy().hasHeightForWidth())
        self.input_totalBruto.setSizePolicy(sizePolicy2)
        self.input_totalBruto.setMaximumSize(QSize(16777215, 30))
        self.input_totalBruto.setFont(font2)
        self.input_totalBruto.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")
        self.input_totalBruto.setReadOnly(True)

        self.gridLayout_13.addWidget(self.input_totalBruto, 1, 0, 1, 1)


        self.gridLayout_19.addWidget(self.frame_16, 0, 0, 1, 1)

        self.frame_19 = QFrame(self.frame_22)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(100, 70))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_19)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 9, 0, -1)
        self.label_14 = QLabel(self.frame_19)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.gridLayout_16.addWidget(self.label_14, 0, 0, 1, 1)

        self.input_totalItem = QLineEdit(self.frame_19)
        self.input_totalItem.setObjectName(u"input_totalItem")
        sizePolicy2.setHeightForWidth(self.input_totalItem.sizePolicy().hasHeightForWidth())
        self.input_totalItem.setSizePolicy(sizePolicy2)
        self.input_totalItem.setMaximumSize(QSize(16777215, 30))
        self.input_totalItem.setFont(font2)
        self.input_totalItem.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")
        self.input_totalItem.setReadOnly(True)

        self.gridLayout_16.addWidget(self.input_totalItem, 1, 0, 1, 1)


        self.gridLayout_19.addWidget(self.frame_19, 0, 3, 1, 1)

        self.frame_17 = QFrame(self.frame_22)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(100, 70))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_17)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 9, 0, -1)
        self.label_12 = QLabel(self.frame_17)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.gridLayout_14.addWidget(self.label_12, 0, 0, 1, 1)

        self.input_desconto = QLineEdit(self.frame_17)
        self.input_desconto.setObjectName(u"input_desconto")
        sizePolicy2.setHeightForWidth(self.input_desconto.sizePolicy().hasHeightForWidth())
        self.input_desconto.setSizePolicy(sizePolicy2)
        self.input_desconto.setMaximumSize(QSize(16777215, 30))
        self.input_desconto.setFont(font2)
        self.input_desconto.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")
        self.input_desconto.setReadOnly(True)

        self.gridLayout_14.addWidget(self.input_desconto, 1, 0, 1, 1)


        self.gridLayout_19.addWidget(self.frame_17, 0, 1, 1, 1)


        self.gridLayout_8.addWidget(self.frame_22, 4, 0, 1, 8)

        self.frame_14 = QFrame(self.frame_8)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(400, 70))
        self.frame_14.setMaximumSize(QSize(500, 70))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_14)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, -1, 0, -1)
        self.label_10 = QLabel(self.frame_14)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.gridLayout_12.addWidget(self.label_10, 0, 0, 1, 1)

        self.input_descricao = QComboBox(self.frame_14)
        self.input_descricao.addItem("")
        self.input_descricao.addItem("")
        self.input_descricao.addItem("")
        self.input_descricao.addItem("")
        self.input_descricao.addItem("")
        self.input_descricao.setObjectName(u"input_descricao")
        sizePolicy.setHeightForWidth(self.input_descricao.sizePolicy().hasHeightForWidth())
        self.input_descricao.setSizePolicy(sizePolicy)
        self.input_descricao.setMaximumSize(QSize(16777215, 30))
        self.input_descricao.setStyleSheet(u"QComboBox {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")
        self.input_descricao.setEditable(True)
        self.input_descricao.setMaxVisibleItems(50)

        self.gridLayout_12.addWidget(self.input_descricao, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_14, 0, 1, 1, 2)

        self.frame_25 = QFrame(self.frame_8)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy)
        self.frame_25.setMinimumSize(QSize(100, 70))
        self.frame_25.setMaximumSize(QSize(100, 70))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_25)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, -1, 0, -1)
        self.label_19 = QLabel(self.frame_25)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.gridLayout_22.addWidget(self.label_19, 0, 0, 1, 1)

        self.input_valDesc = QLineEdit(self.frame_25)
        self.input_valDesc.setObjectName(u"input_valDesc")
        sizePolicy2.setHeightForWidth(self.input_valDesc.sizePolicy().hasHeightForWidth())
        self.input_valDesc.setSizePolicy(sizePolicy2)
        self.input_valDesc.setMaximumSize(QSize(16777215, 30))
        self.input_valDesc.setFont(font2)
        self.input_valDesc.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_22.addWidget(self.input_valDesc, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_25, 1, 4, 1, 1)

        self.frame_15 = QFrame(self.frame_8)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_15)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 20, 0, 0)

        self.gridLayout_8.addWidget(self.frame_15, 0, 6, 1, 1)

        self.frame_26 = QFrame(self.frame_8)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setMinimumSize(QSize(100, 70))
        self.frame_26.setMaximumSize(QSize(100, 70))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_26)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, -1, 0, -1)
        self.label_20 = QLabel(self.frame_26)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.gridLayout_23.addWidget(self.label_20, 0, 0, 1, 1)

        self.input_percDesc = QLineEdit(self.frame_26)
        self.input_percDesc.setObjectName(u"input_percDesc")
        sizePolicy2.setHeightForWidth(self.input_percDesc.sizePolicy().hasHeightForWidth())
        self.input_percDesc.setSizePolicy(sizePolicy2)
        self.input_percDesc.setMaximumSize(QSize(16777215, 30))
        self.input_percDesc.setFont(font2)
        self.input_percDesc.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_23.addWidget(self.input_percDesc, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_26, 1, 3, 1, 1)

        self.frame_23 = QFrame(self.frame_8)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(125, 70))
        self.frame_23.setMaximumSize(QSize(125, 70))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_23)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, -1, 0, -1)
        self.label_17 = QLabel(self.frame_23)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.gridLayout_20.addWidget(self.label_17, 0, 0, 1, 1)

        self.input_cor = QLineEdit(self.frame_23)
        self.input_cor.setObjectName(u"input_cor")
        sizePolicy2.setHeightForWidth(self.input_cor.sizePolicy().hasHeightForWidth())
        self.input_cor.setSizePolicy(sizePolicy2)
        self.input_cor.setMaximumSize(QSize(16777215, 30))
        self.input_cor.setFont(font2)
        self.input_cor.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_20.addWidget(self.input_cor, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_23, 0, 3, 1, 1)

        self.table = QTableWidget(self.frame_8)
        if (self.table.columnCount() < 11):
            self.table.setColumnCount(11)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(8, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(9, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(10, __qtablewidgetitem16)
        self.table.setObjectName(u"table")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy4)
        self.table.setMinimumSize(QSize(0, 100))
        self.table.setFont(font3)
        self.table.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	border: 1px solid black;\n"
"}")
        self.table.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.table.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.table.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)

        self.gridLayout_8.addWidget(self.table, 2, 0, 1, 8)

        self.frame_24 = QFrame(self.frame_8)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy)
        self.frame_24.setMinimumSize(QSize(100, 70))
        self.frame_24.setMaximumSize(QSize(100, 70))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_24)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, -1, 0, -1)
        self.label_18 = QLabel(self.frame_24)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.gridLayout_21.addWidget(self.label_18, 0, 0, 1, 1)

        self.input_total = QLineEdit(self.frame_24)
        self.input_total.setObjectName(u"input_total")
        sizePolicy2.setHeightForWidth(self.input_total.sizePolicy().hasHeightForWidth())
        self.input_total.setSizePolicy(sizePolicy2)
        self.input_total.setMaximumSize(QSize(16777215, 30))
        self.input_total.setFont(font2)
        self.input_total.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_21.addWidget(self.input_total, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_24, 1, 5, 1, 1)

        self.frame_27 = QFrame(self.frame_8)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy)
        self.frame_27.setMaximumSize(QSize(16777215, 60))
        self.frame_27.setStyleSheet(u"\n"
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
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.btn_remover = QPushButton(self.frame_27)
        self.btn_remover.setObjectName(u"btn_remover")
        sizePolicy3.setHeightForWidth(self.btn_remover.sizePolicy().hasHeightForWidth())
        self.btn_remover.setSizePolicy(sizePolicy3)
        self.btn_remover.setMinimumSize(QSize(100, 35))
        self.btn_remover.setMaximumSize(QSize(100, 35))
        self.btn_remover.setFont(font4)
        self.btn_remover.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.btn_remover)


        self.gridLayout_8.addWidget(self.frame_27, 3, 0, 1, 8)


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

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.venda)

        self.gridLayout.addWidget(self.stackedWidget, 2, 0, 1, 1)

        self.frame_2 = QFrame(Vendas)
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


        self.retranslateUi(Vendas)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Vendas)
    # setupUi

    def retranslateUi(self, Vendas):
        Vendas.setWindowTitle(QCoreApplication.translate("Vendas", u"Form", None))
        self.label.setText(QCoreApplication.translate("Vendas", u"Consultar Vendas", None))
        self.label_22.setText(QCoreApplication.translate("Vendas", u"\u00e0", None))
        self.label_2.setText(QCoreApplication.translate("Vendas", u"Pesquisar", None))
        self.btn_busca.setText("")
        self.radio_periodo.setText(QCoreApplication.translate("Vendas", u"Periodo:", None))
        ___qtablewidgetitem = self.table_vendas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Vendas", u"C\u00f3digo", None));
        ___qtablewidgetitem1 = self.table_vendas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Vendas", u"Data", None));
        ___qtablewidgetitem2 = self.table_vendas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Vendas", u"Cliente", None));
        ___qtablewidgetitem3 = self.table_vendas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Vendas", u"Valor", None));
        ___qtablewidgetitem4 = self.table_vendas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Vendas", u"Qnt. Produtos", None));
        ___qtablewidgetitem5 = self.table_vendas.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Vendas", u"Vendedor", None));
        self.btn_deletar.setText(QCoreApplication.translate("Vendas", u"Deletar", None))
        self.btn_editar.setText(QCoreApplication.translate("Vendas", u"Consultar", None))
        self.btn_relatorio_geral.setText(QCoreApplication.translate("Vendas", u"Relat\u00f3rio geral", None))
        self.label_3.setText(QCoreApplication.translate("Vendas", u"Nova Venda", None))
        self.label_4.setText(QCoreApplication.translate("Vendas", u"Cliente", None))
        self.input_cliente.setItemText(0, "")
        self.input_cliente.setItemText(1, QCoreApplication.translate("Vendas", u"UNI", None))
        self.input_cliente.setItemText(2, QCoreApplication.translate("Vendas", u"CX", None))
        self.input_cliente.setItemText(3, QCoreApplication.translate("Vendas", u"KG", None))
        self.input_cliente.setItemText(4, QCoreApplication.translate("Vendas", u"PC", None))

        self.label_5.setText(QCoreApplication.translate("Vendas", u"Data", None))
        self.label_6.setText(QCoreApplication.translate("Vendas", u"Nr. Venda", None))
        self.label_7.setText(QCoreApplication.translate("Vendas", u"Quantidade", None))
        self.label_8.setText(QCoreApplication.translate("Vendas", u"Pre\u00e7o Uni.", None))
        self.btn_add.setText("")
        self.label_9.setText(QCoreApplication.translate("Vendas", u"Tamanho", None))
        self.label_13.setText(QCoreApplication.translate("Vendas", u"TOTAL L\u00cdQUIDO", None))
        self.label_16.setText(QCoreApplication.translate("Vendas", u"TROCO", None))
        self.label_15.setText(QCoreApplication.translate("Vendas", u"TOTAL PAGO", None))
        self.label_11.setText(QCoreApplication.translate("Vendas", u"TOTAL BRUTO", None))
        self.label_14.setText(QCoreApplication.translate("Vendas", u"TOTAL DE ITENS", None))
        self.label_12.setText(QCoreApplication.translate("Vendas", u"DESCONTO", None))
        self.label_10.setText(QCoreApplication.translate("Vendas", u"Descri\u00e7\u00e3o/C\u00f3digo", None))
        self.input_descricao.setItemText(0, "")
        self.input_descricao.setItemText(1, QCoreApplication.translate("Vendas", u"UNI", None))
        self.input_descricao.setItemText(2, QCoreApplication.translate("Vendas", u"CX", None))
        self.input_descricao.setItemText(3, QCoreApplication.translate("Vendas", u"KG", None))
        self.input_descricao.setItemText(4, QCoreApplication.translate("Vendas", u"PC", None))

        self.label_19.setText(QCoreApplication.translate("Vendas", u"R$ Desconto", None))
        self.label_20.setText(QCoreApplication.translate("Vendas", u"% Desconto", None))
        self.label_17.setText(QCoreApplication.translate("Vendas", u"Cor", None))
        ___qtablewidgetitem6 = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Vendas", u"C\u00f3digo", None));
        ___qtablewidgetitem7 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Vendas", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem8 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Vendas", u"Un.", None));
        ___qtablewidgetitem9 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Vendas", u"Qtde.", None));
        ___qtablewidgetitem10 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Vendas", u"Tam.", None));
        ___qtablewidgetitem11 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Vendas", u"Cor", None));
        ___qtablewidgetitem12 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Vendas", u"Pc. Unit\u00e1rio", None));
        ___qtablewidgetitem13 = self.table.horizontalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Vendas", u"Total Bruto", None));
        ___qtablewidgetitem14 = self.table.horizontalHeaderItem(8)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Vendas", u"% Desc", None));
        ___qtablewidgetitem15 = self.table.horizontalHeaderItem(9)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Vendas", u"R$ Desc", None));
        ___qtablewidgetitem16 = self.table.horizontalHeaderItem(10)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Vendas", u"Total L\u00edquido", None));
        self.label_18.setText(QCoreApplication.translate("Vendas", u"Total", None))
        self.btn_remover.setText(QCoreApplication.translate("Vendas", u"Remover Item", None))
        self.btn_salvar.setText(QCoreApplication.translate("Vendas", u"Salvar", None))
        self.btn_consulta.setText(QCoreApplication.translate("Vendas", u"Consultar", None))
        self.btn_novo.setText(QCoreApplication.translate("Vendas", u"Novo", None))
    # retranslateUi

