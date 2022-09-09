# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vendas_editarVuUxUs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import interface.ui.resource_rc

class Ui_VendasEdit(object):
    def setupUi(self, VendasEdit):
        if not VendasEdit.objectName():
            VendasEdit.setObjectName(u"VendasEdit")
        VendasEdit.resize(1041, 700)
        VendasEdit.setMinimumSize(QSize(900, 700))
        VendasEdit.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(236, 242, 248);\n"
"}\n"
"")
        self.gridLayout = QGridLayout(VendasEdit)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(30, 30, 30, 30)
        self.frame_5 = QFrame(VendasEdit)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMaximumSize(QSize(16777215, 100))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setFamily(u"Raleway")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.frame_13 = QFrame(self.frame_5)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 70))
        self.frame_13.setMaximumSize(QSize(150, 16777215))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_13)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_10 = QLabel(self.frame_13)
        self.label_10.setObjectName(u"label_10")
        font1 = QFont()
        font1.setFamily(u"Raleway")
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_10.setFont(font1)

        self.gridLayout_12.addWidget(self.label_10, 0, 0, 1, 1)

        self.input_data_2 = QDateEdit(self.frame_13)
        self.input_data_2.setObjectName(u"input_data_2")
        self.input_data_2.setMinimumSize(QSize(0, 30))
        self.input_data_2.setMaximumSize(QSize(16777215, 30))
        self.input_data_2.setStyleSheet(u"QDateEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 8px;\n"
"}")
        self.input_data_2.setReadOnly(True)
        self.input_data_2.setCalendarPopup(True)

        self.gridLayout_12.addWidget(self.input_data_2, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_13, 0, 3, 1, 1)

        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(200, 70))
        self.frame_12.setMaximumSize(QSize(200, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_12)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_9 = QLabel(self.frame_12)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout_11.addWidget(self.label_9, 0, 0, 1, 1)

        self.input_cliente = QLineEdit(self.frame_12)
        self.input_cliente.setObjectName(u"input_cliente")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.input_cliente.sizePolicy().hasHeightForWidth())
        self.input_cliente.setSizePolicy(sizePolicy2)
        self.input_cliente.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamily(u"Raleway")
        self.input_cliente.setFont(font2)
        self.input_cliente.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")
        self.input_cliente.setReadOnly(True)

        self.gridLayout_11.addWidget(self.input_cliente, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_12, 0, 5, 1, 1)

        self.frame_14 = QFrame(self.frame_5)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy1.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy1)
        self.frame_14.setMinimumSize(QSize(75, 70))
        self.frame_14.setMaximumSize(QSize(75, 16777215))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_14)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_17 = QLabel(self.frame_14)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.gridLayout_20.addWidget(self.label_17, 0, 0, 1, 1)

        self.input_nrVenda_2 = QLineEdit(self.frame_14)
        self.input_nrVenda_2.setObjectName(u"input_nrVenda_2")
        sizePolicy2.setHeightForWidth(self.input_nrVenda_2.sizePolicy().hasHeightForWidth())
        self.input_nrVenda_2.setSizePolicy(sizePolicy2)
        self.input_nrVenda_2.setMaximumSize(QSize(16777215, 30))
        self.input_nrVenda_2.setFont(font2)
        self.input_nrVenda_2.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")
        self.input_nrVenda_2.setReadOnly(True)

        self.gridLayout_20.addWidget(self.input_nrVenda_2, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_14, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)

        self.frame_8 = QFrame(VendasEdit)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_8)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(9)
        self.gridLayout_9.setVerticalSpacing(8)
        self.gridLayout_9.setContentsMargins(0, -1, 0, -1)
        self.table = QTableWidget(self.frame_8)
        if (self.table.columnCount() < 11):
            self.table.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.table.setObjectName(u"table")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy3)
        self.table.setMinimumSize(QSize(0, 100))
        font3 = QFont()
        font3.setFamily(u"Raleway")
        font3.setBold(True)
        font3.setWeight(75)
        self.table.setFont(font3)
        self.table.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	border: 1px solid black;\n"
"}")
        self.table.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)

        self.gridLayout_9.addWidget(self.table, 0, 0, 1, 2)

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
        self.input_totalPago.setReadOnly(True)

        self.gridLayout_17.addWidget(self.input_totalPago, 1, 0, 1, 1)


        self.gridLayout_19.addWidget(self.frame_20, 0, 4, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_6, 0, 6, 1, 1)


        self.gridLayout_9.addWidget(self.frame_22, 1, 0, 1, 2)

        self.frame_7 = QFrame(self.frame_8)
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
        self.btn_relatorio = QPushButton(self.frame_7)
        self.btn_relatorio.setObjectName(u"btn_relatorio")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_relatorio.sizePolicy().hasHeightForWidth())
        self.btn_relatorio.setSizePolicy(sizePolicy4)
        self.btn_relatorio.setMinimumSize(QSize(0, 35))
        self.btn_relatorio.setMaximumSize(QSize(200, 35))
        font4 = QFont()
        font4.setFamily(u"Raleway")
        font4.setPointSize(9)
        font4.setBold(True)
        font4.setWeight(75)
        self.btn_relatorio.setFont(font4)
        self.btn_relatorio.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.btn_relatorio)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.gridLayout_9.addWidget(self.frame_7, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_8, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)


        self.retranslateUi(VendasEdit)

        QMetaObject.connectSlotsByName(VendasEdit)
    # setupUi

    def retranslateUi(self, VendasEdit):
        VendasEdit.setWindowTitle(QCoreApplication.translate("VendasEdit", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("VendasEdit", u"Consultar Venda", None))
        self.label_10.setText(QCoreApplication.translate("VendasEdit", u"Data", None))
        self.label_9.setText(QCoreApplication.translate("VendasEdit", u"Cliente", None))
        self.label_17.setText(QCoreApplication.translate("VendasEdit", u"Nr. Venda", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VendasEdit", u"C\u00f3digo", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VendasEdit", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VendasEdit", u"Un.", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VendasEdit", u"Qtde.", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("VendasEdit", u"Tam.", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("VendasEdit", u"Cor", None));
        ___qtablewidgetitem6 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("VendasEdit", u"Pc. Unit\u00e1rio", None));
        ___qtablewidgetitem7 = self.table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("VendasEdit", u"Total Bruto", None));
        ___qtablewidgetitem8 = self.table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("VendasEdit", u"% Desc", None));
        ___qtablewidgetitem9 = self.table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("VendasEdit", u"R$ Desc", None));
        ___qtablewidgetitem10 = self.table.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("VendasEdit", u"Total L\u00edquido", None));
        self.label_16.setText(QCoreApplication.translate("VendasEdit", u"TROCO", None))
        self.label_14.setText(QCoreApplication.translate("VendasEdit", u"TOTAL DE ITENS", None))
        self.label_11.setText(QCoreApplication.translate("VendasEdit", u"TOTAL BRUTO", None))
        self.label_12.setText(QCoreApplication.translate("VendasEdit", u"DESCONTO", None))
        self.label_13.setText(QCoreApplication.translate("VendasEdit", u"TOTAL L\u00cdQUIDO", None))
        self.label_15.setText(QCoreApplication.translate("VendasEdit", u"TOTAL PAGO", None))
        self.btn_relatorio.setText(QCoreApplication.translate("VendasEdit", u"Gerar PDF", None))
    # retranslateUi

