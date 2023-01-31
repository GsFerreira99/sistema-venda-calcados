# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'relatorio_geral_vendasGhlloH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RelatorioGeralVendas(object):
    def setupUi(self, RelatorioGeralVendas):
        if not RelatorioGeralVendas.objectName():
            RelatorioGeralVendas.setObjectName(u"RelatorioGeralVendas")
        RelatorioGeralVendas.resize(330, 250)
        RelatorioGeralVendas.setMinimumSize(QSize(330, 250))
        RelatorioGeralVendas.setMaximumSize(QSize(330, 250))
        RelatorioGeralVendas.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(236, 242, 248);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(RelatorioGeralVendas)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, -1, 30, -1)
        self.label_3 = QLabel(RelatorioGeralVendas)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QSize(300, 30))
        font = QFont()
        font.setFamily(u"Raleway")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.label_3)

        self.frame_7 = QFrame(RelatorioGeralVendas)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setMinimumSize(QSize(0, 160))
        self.frame_7.setMaximumSize(QSize(16777215, 160))
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
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 70))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_9)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_9)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        font1 = QFont()
        font1.setFamily(u"Raleway")
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_8.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.input_periodo = QComboBox(self.frame_3)
        self.input_periodo.addItem("")
        self.input_periodo.addItem("")
        self.input_periodo.addItem("")
        self.input_periodo.addItem("")
        self.input_periodo.setObjectName(u"input_periodo")
        sizePolicy1.setHeightForWidth(self.input_periodo.sizePolicy().hasHeightForWidth())
        self.input_periodo.setSizePolicy(sizePolicy1)
        self.input_periodo.setMaximumSize(QSize(16777215, 30))
        self.input_periodo.setStyleSheet(u"QComboBox {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")
        self.input_periodo.setEditable(False)
        self.input_periodo.setMaxVisibleItems(50)

        self.horizontalLayout_4.addWidget(self.input_periodo)


        self.gridLayout_8.addWidget(self.frame_3, 0, 0, 1, 2)

        self.frame_periodo = QFrame(self.frame_9)
        self.frame_periodo.setObjectName(u"frame_periodo")
        sizePolicy1.setHeightForWidth(self.frame_periodo.sizePolicy().hasHeightForWidth())
        self.frame_periodo.setSizePolicy(sizePolicy1)
        self.frame_periodo.setMinimumSize(QSize(0, 0))
        self.frame_periodo.setMaximumSize(QSize(16777215, 0))
        self.frame_periodo.setFrameShape(QFrame.StyledPanel)
        self.frame_periodo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_periodo)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
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

        self.horizontalLayout_2.addWidget(self.input_data_ini)

        self.label_9 = QLabel(self.frame_periodo)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(10, 16777215))
        self.label_9.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_9)

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

        self.horizontalLayout_2.addWidget(self.input_data_fim)


        self.gridLayout_8.addWidget(self.frame_periodo, 2, 0, 1, 2)

        self.btn_gerar = QPushButton(self.frame_9)
        self.btn_gerar.setObjectName(u"btn_gerar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_gerar.sizePolicy().hasHeightForWidth())
        self.btn_gerar.setSizePolicy(sizePolicy2)
        self.btn_gerar.setMinimumSize(QSize(0, 35))
        font2 = QFont()
        font2.setFamily(u"Raleway")
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_gerar.setFont(font2)
        self.btn_gerar.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.btn_gerar, 3, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_9)


        self.verticalLayout.addWidget(self.frame_7)


        self.retranslateUi(RelatorioGeralVendas)

        QMetaObject.connectSlotsByName(RelatorioGeralVendas)
    # setupUi

    def retranslateUi(self, RelatorioGeralVendas):
        RelatorioGeralVendas.setWindowTitle(QCoreApplication.translate("RelatorioGeralVendas", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("RelatorioGeralVendas", u"Relat\u00f3rio Geral de Vendas", None))
        self.label_8.setText(QCoreApplication.translate("RelatorioGeralVendas", u"Periodo", None))
        self.input_periodo.setItemText(0, "")
        self.input_periodo.setItemText(1, QCoreApplication.translate("RelatorioGeralVendas", u"M\u00eas Atual", None))
        self.input_periodo.setItemText(2, QCoreApplication.translate("RelatorioGeralVendas", u"M\u00eas Anterior", None))
        self.input_periodo.setItemText(3, QCoreApplication.translate("RelatorioGeralVendas", u"Selecionar Periodo", None))

        self.label_9.setText(QCoreApplication.translate("RelatorioGeralVendas", u"\u00e0", None))
        self.btn_gerar.setText(QCoreApplication.translate("RelatorioGeralVendas", u"Gerar", None))
    # retranslateUi

