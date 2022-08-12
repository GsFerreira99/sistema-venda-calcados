# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'estoquefPRKbH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import interface.ui.resource_rc

class Ui_Estoque(object):
    def setupUi(self, Estoque):
        if not Estoque.objectName():
            Estoque.setObjectName(u"Estoque")
        Estoque.resize(900, 700)
        Estoque.setMinimumSize(QSize(900, 700))
        Estoque.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(236, 242, 248);\n"
"}\n"
"")
        self.gridLayout = QGridLayout(Estoque)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(30, 30, 30, 30)
        self.stackedWidget = QStackedWidget(Estoque)
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

        self.table_produtos = QTableWidget(self.consulta)
        if (self.table_produtos.columnCount() < 7):
            self.table_produtos.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_produtos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_produtos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_produtos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_produtos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_produtos.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_produtos.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_produtos.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.table_produtos.setObjectName(u"table_produtos")
        font3 = QFont()
        font3.setFamily(u"Raleway")
        font3.setBold(True)
        font3.setWeight(75)
        self.table_produtos.setFont(font3)
        self.table_produtos.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	border: 1px solid black;\n"
"}")
        self.table_produtos.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.table_produtos)

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

        self.btn_adcEstoque = QPushButton(self.frame_4)
        self.btn_adcEstoque.setObjectName(u"btn_adcEstoque")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_adcEstoque.sizePolicy().hasHeightForWidth())
        self.btn_adcEstoque.setSizePolicy(sizePolicy3)
        self.btn_adcEstoque.setMaximumSize(QSize(150, 35))
        font4 = QFont()
        font4.setFamily(u"Raleway")
        font4.setPointSize(9)
        font4.setBold(True)
        font4.setWeight(75)
        self.btn_adcEstoque.setFont(font4)
        self.btn_adcEstoque.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.btn_adcEstoque)

        self.btn_deletar = QPushButton(self.frame_4)
        self.btn_deletar.setObjectName(u"btn_deletar")
        sizePolicy3.setHeightForWidth(self.btn_deletar.sizePolicy().hasHeightForWidth())
        self.btn_deletar.setSizePolicy(sizePolicy3)
        self.btn_deletar.setMaximumSize(QSize(100, 35))
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
        self.gridLayout_8.setVerticalSpacing(20)
        self.gridLayout_8.setContentsMargins(0, -1, 0, -1)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_5, 2, 1, 1, 1)

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
        self.gridLayout_32.setHorizontalSpacing(27)
        self.gridLayout_32.setContentsMargins(10, 0, 0, 0)
        self.frame_39 = QFrame(self.frame_35)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(350, 0))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.gridLayout_42 = QGridLayout(self.frame_39)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setContentsMargins(0, 9, 0, -1)
        self.label_33 = QLabel(self.frame_39)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(16777215, 20))
        self.label_33.setFont(font2)

        self.gridLayout_42.addWidget(self.label_33, 0, 0, 1, 1)

        self.input_observacao = QTextEdit(self.frame_39)
        self.input_observacao.setObjectName(u"input_observacao")
        self.input_observacao.setStyleSheet(u"QTextEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_42.addWidget(self.input_observacao, 1, 0, 1, 1)


        self.gridLayout_32.addWidget(self.frame_39, 0, 0, 2, 1)

        self.frame_43 = QFrame(self.frame_35)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMaximumSize(QSize(100, 70))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.gridLayout_40 = QGridLayout(self.frame_43)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(0, 9, 0, -1)
        self.label_34 = QLabel(self.frame_43)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font2)

        self.gridLayout_40.addWidget(self.label_34, 0, 0, 1, 1)

        self.input_estoqueAtual = QLineEdit(self.frame_43)
        self.input_estoqueAtual.setObjectName(u"input_estoqueAtual")
        sizePolicy2.setHeightForWidth(self.input_estoqueAtual.sizePolicy().hasHeightForWidth())
        self.input_estoqueAtual.setSizePolicy(sizePolicy2)
        self.input_estoqueAtual.setMaximumSize(QSize(16777215, 30))
        self.input_estoqueAtual.setFont(font1)
        self.input_estoqueAtual.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_40.addWidget(self.input_estoqueAtual, 1, 0, 1, 1)


        self.gridLayout_32.addWidget(self.frame_43, 0, 3, 1, 1)

        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(100, 70))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.gridLayout_33 = QGridLayout(self.frame_36)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setContentsMargins(0, 9, 0, -1)
        self.label_27 = QLabel(self.frame_36)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)

        self.gridLayout_33.addWidget(self.label_27, 0, 0, 1, 1)

        self.input_cor = QLineEdit(self.frame_36)
        self.input_cor.setObjectName(u"input_cor")
        sizePolicy2.setHeightForWidth(self.input_cor.sizePolicy().hasHeightForWidth())
        self.input_cor.setSizePolicy(sizePolicy2)
        self.input_cor.setMaximumSize(QSize(16777215, 30))
        self.input_cor.setFont(font1)
        self.input_cor.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_33.addWidget(self.input_cor, 1, 0, 1, 1)


        self.gridLayout_32.addWidget(self.frame_36, 0, 1, 1, 1)

        self.frame_45 = QFrame(self.frame_35)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMaximumSize(QSize(100, 70))
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.gridLayout_46 = QGridLayout(self.frame_45)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_46.setContentsMargins(0, 9, 0, -1)
        self.label_39 = QLabel(self.frame_45)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font2)

        self.gridLayout_46.addWidget(self.label_39, 0, 0, 1, 1)

        self.input_tamanho = QLineEdit(self.frame_45)
        self.input_tamanho.setObjectName(u"input_tamanho")
        sizePolicy2.setHeightForWidth(self.input_tamanho.sizePolicy().hasHeightForWidth())
        self.input_tamanho.setSizePolicy(sizePolicy2)
        self.input_tamanho.setMaximumSize(QSize(16777215, 30))
        self.input_tamanho.setFont(font1)
        self.input_tamanho.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_46.addWidget(self.input_tamanho, 1, 0, 1, 1)


        self.gridLayout_32.addWidget(self.frame_45, 0, 2, 1, 1)


        self.gridLayout_8.addWidget(self.frame_35, 2, 0, 1, 1)

        self.frame_34 = QFrame(self.frame_8)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy)
        self.frame_34.setMinimumSize(QSize(0, 70))
        self.frame_34.setMaximumSize(QSize(16777215, 70))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_34)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setHorizontalSpacing(30)
        self.gridLayout_31.setVerticalSpacing(9)
        self.gridLayout_31.setContentsMargins(10, 0, 0, 0)
        self.frame_38 = QFrame(self.frame_34)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMaximumSize(QSize(16777215, 70))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.gridLayout_35 = QGridLayout(self.frame_38)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(0, 9, 0, -1)
        self.label_30 = QLabel(self.frame_38)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)

        self.gridLayout_35.addWidget(self.label_30, 0, 0, 1, 1)

        self.input_descricao = QLineEdit(self.frame_38)
        self.input_descricao.setObjectName(u"input_descricao")
        sizePolicy2.setHeightForWidth(self.input_descricao.sizePolicy().hasHeightForWidth())
        self.input_descricao.setSizePolicy(sizePolicy2)
        self.input_descricao.setMaximumSize(QSize(16777215, 30))
        self.input_descricao.setFont(font1)
        self.input_descricao.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_35.addWidget(self.input_descricao, 1, 0, 1, 1)


        self.gridLayout_31.addWidget(self.frame_38, 0, 1, 1, 1)

        self.frame_37 = QFrame(self.frame_34)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMaximumSize(QSize(130, 70))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.gridLayout_34 = QGridLayout(self.frame_37)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setContentsMargins(0, 9, 0, -1)
        self.label_29 = QLabel(self.frame_37)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font2)

        self.gridLayout_34.addWidget(self.label_29, 0, 0, 1, 1)

        self.input_codBarras = QLineEdit(self.frame_37)
        self.input_codBarras.setObjectName(u"input_codBarras")
        sizePolicy2.setHeightForWidth(self.input_codBarras.sizePolicy().hasHeightForWidth())
        self.input_codBarras.setSizePolicy(sizePolicy2)
        self.input_codBarras.setMaximumSize(QSize(16777215, 30))
        self.input_codBarras.setFont(font1)
        self.input_codBarras.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_34.addWidget(self.input_codBarras, 1, 0, 1, 1)


        self.gridLayout_31.addWidget(self.frame_37, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_34, 0, 0, 1, 1)

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

        self.input_unidade = QLineEdit(self.frame_30)
        self.input_unidade.setObjectName(u"input_unidade")
        sizePolicy2.setHeightForWidth(self.input_unidade.sizePolicy().hasHeightForWidth())
        self.input_unidade.setSizePolicy(sizePolicy2)
        self.input_unidade.setMaximumSize(QSize(16777215, 30))
        self.input_unidade.setFont(font1)
        self.input_unidade.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_27.addWidget(self.input_unidade, 1, 0, 1, 1)


        self.gridLayout_24.addWidget(self.frame_30, 0, 0, 1, 1)

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

        self.input_precoCompra = QLineEdit(self.frame_31)
        self.input_precoCompra.setObjectName(u"input_precoCompra")
        sizePolicy2.setHeightForWidth(self.input_precoCompra.sizePolicy().hasHeightForWidth())
        self.input_precoCompra.setSizePolicy(sizePolicy2)
        self.input_precoCompra.setMaximumSize(QSize(16777215, 30))
        self.input_precoCompra.setFont(font1)
        self.input_precoCompra.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_28.addWidget(self.input_precoCompra, 1, 0, 1, 1)


        self.gridLayout_24.addWidget(self.frame_31, 0, 1, 1, 1)

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

        self.input_precoVenda = QLineEdit(self.frame_33)
        self.input_precoVenda.setObjectName(u"input_precoVenda")
        sizePolicy2.setHeightForWidth(self.input_precoVenda.sizePolicy().hasHeightForWidth())
        self.input_precoVenda.setSizePolicy(sizePolicy2)
        self.input_precoVenda.setMaximumSize(QSize(16777215, 30))
        self.input_precoVenda.setFont(font1)
        self.input_precoVenda.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_30.addWidget(self.input_precoVenda, 1, 0, 1, 1)


        self.gridLayout_24.addWidget(self.frame_33, 0, 4, 1, 1)

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

        self.input_lucro = QLineEdit(self.frame_29)
        self.input_lucro.setObjectName(u"input_lucro")
        sizePolicy2.setHeightForWidth(self.input_lucro.sizePolicy().hasHeightForWidth())
        self.input_lucro.setSizePolicy(sizePolicy2)
        self.input_lucro.setMaximumSize(QSize(16777215, 30))
        self.input_lucro.setFont(font1)
        self.input_lucro.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_26.addWidget(self.input_lucro, 1, 0, 1, 1)


        self.gridLayout_24.addWidget(self.frame_29, 0, 3, 1, 1)

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

        self.inputMargem = QLineEdit(self.frame_32)
        self.inputMargem.setObjectName(u"inputMargem")
        sizePolicy2.setHeightForWidth(self.inputMargem.sizePolicy().hasHeightForWidth())
        self.inputMargem.setSizePolicy(sizePolicy2)
        self.inputMargem.setMaximumSize(QSize(16777215, 30))
        self.inputMargem.setFont(font1)
        self.inputMargem.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_29.addWidget(self.inputMargem, 1, 0, 1, 1)


        self.gridLayout_24.addWidget(self.frame_32, 0, 2, 1, 1)

        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(100, 70))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_28)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, 9, 0, -1)
        self.label_21 = QLabel(self.frame_28)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)

        self.gridLayout_25.addWidget(self.label_21, 0, 0, 1, 1)

        self.input_precoAtacado = QLineEdit(self.frame_28)
        self.input_precoAtacado.setObjectName(u"input_precoAtacado")
        sizePolicy2.setHeightForWidth(self.input_precoAtacado.sizePolicy().hasHeightForWidth())
        self.input_precoAtacado.setSizePolicy(sizePolicy2)
        self.input_precoAtacado.setMaximumSize(QSize(16777215, 30))
        self.input_precoAtacado.setFont(font1)
        self.input_precoAtacado.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_25.addWidget(self.input_precoAtacado, 1, 0, 1, 1)


        self.gridLayout_24.addWidget(self.frame_28, 0, 5, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_7, 0, 6, 1, 1)


        self.gridLayout_8.addWidget(self.frame_27, 1, 0, 1, 2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_6, 0, 1, 1, 1)


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

        self.frame_2 = QFrame(Estoque)
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


        self.retranslateUi(Estoque)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Estoque)
    # setupUi

    def retranslateUi(self, Estoque):
        Estoque.setWindowTitle(QCoreApplication.translate("Estoque", u"Form", None))
        self.label.setText(QCoreApplication.translate("Estoque", u"Consultar Produtos", None))
        self.label_2.setText(QCoreApplication.translate("Estoque", u"Pesquisar", None))
        self.btn_busca.setText("")
        ___qtablewidgetitem = self.table_produtos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Estoque", u"C\u00f3digo/C\u00f3d. Barras", None));
        ___qtablewidgetitem1 = self.table_produtos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Estoque", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem2 = self.table_produtos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Estoque", u"Uni.", None));
        ___qtablewidgetitem3 = self.table_produtos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Estoque", u"Qnt", None));
        ___qtablewidgetitem4 = self.table_produtos.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Estoque", u"Pre\u00e7o Compra", None));
        ___qtablewidgetitem5 = self.table_produtos.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Estoque", u"Pre\u00e7o Venda", None));
        ___qtablewidgetitem6 = self.table_produtos.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Estoque", u"Fornecedor", None));
        self.btn_adcEstoque.setText(QCoreApplication.translate("Estoque", u"Adicionar Estoque", None))
        self.btn_deletar.setText(QCoreApplication.translate("Estoque", u"Deletar", None))
        self.btn_editar.setText(QCoreApplication.translate("Estoque", u"Editar", None))
        self.label_3.setText(QCoreApplication.translate("Estoque", u"Cadastrar Novo Produto", None))
        self.label_33.setText(QCoreApplication.translate("Estoque", u"Observa\u00e7\u00e3o", None))
        self.label_34.setText(QCoreApplication.translate("Estoque", u"Estoque Atual", None))
        self.label_27.setText(QCoreApplication.translate("Estoque", u"Cor", None))
        self.label_39.setText(QCoreApplication.translate("Estoque", u"Tamanho", None))
        self.label_30.setText(QCoreApplication.translate("Estoque", u"Descri\u00e7\u00e3o", None))
        self.label_29.setText(QCoreApplication.translate("Estoque", u"C\u00f3digo/C\u00f3d Barras", None))
        self.label_23.setText(QCoreApplication.translate("Estoque", u"Unidade", None))
        self.label_24.setText(QCoreApplication.translate("Estoque", u"Pre\u00e7o Compra", None))
        self.label_26.setText(QCoreApplication.translate("Estoque", u"Pre\u00e7o Venda", None))
        self.label_22.setText(QCoreApplication.translate("Estoque", u"Lucro", None))
        self.label_25.setText(QCoreApplication.translate("Estoque", u"Margem/Markup", None))
        self.label_21.setText(QCoreApplication.translate("Estoque", u"Pre\u00e7o Atacado", None))
        self.btn_salvar.setText(QCoreApplication.translate("Estoque", u"Salvar", None))
        self.btn_consulta.setText(QCoreApplication.translate("Estoque", u"Consultar", None))
        self.btn_novo.setText(QCoreApplication.translate("Estoque", u"Novo", None))
    # retranslateUi

