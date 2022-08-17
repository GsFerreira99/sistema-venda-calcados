# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'estoque_editarXjZMal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import interface.ui.resource_rc

class Ui_EstoqueEdit(object):
    def setupUi(self, EstoqueEdit):
        if not EstoqueEdit.objectName():
            EstoqueEdit.setObjectName(u"EstoqueEdit")
        EstoqueEdit.resize(900, 700)
        EstoqueEdit.setMinimumSize(QSize(900, 700))
        EstoqueEdit.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(236, 242, 248);\n"
"}\n"
"")
        self.gridLayout = QGridLayout(EstoqueEdit)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(30, 30, 30, 30)
        self.frame_5 = QFrame(EstoqueEdit)
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

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)

        self.frame_8 = QFrame(EstoqueEdit)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(9)
        self.gridLayout_8.setVerticalSpacing(20)
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
        self.frame_30 = QFrame(self.frame_27)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(100, 70))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_30)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 9, 0, -1)
        self.input_unidade = QComboBox(self.frame_30)
        self.input_unidade.addItem("")
        self.input_unidade.addItem("")
        self.input_unidade.addItem("")
        self.input_unidade.addItem("")
        self.input_unidade.addItem("")
        self.input_unidade.setObjectName(u"input_unidade")
        sizePolicy.setHeightForWidth(self.input_unidade.sizePolicy().hasHeightForWidth())
        self.input_unidade.setSizePolicy(sizePolicy)
        self.input_unidade.setMaximumSize(QSize(16777215, 30))
        self.input_unidade.setStyleSheet(u"QComboBox {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_27.addWidget(self.input_unidade, 1, 0, 1, 1)

        self.label_23 = QLabel(self.frame_30)
        self.label_23.setObjectName(u"label_23")
        font1 = QFont()
        font1.setFamily(u"Raleway")
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_23.setFont(font1)

        self.gridLayout_27.addWidget(self.label_23, 0, 0, 1, 1)


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
        self.label_24.setFont(font1)

        self.gridLayout_28.addWidget(self.label_24, 0, 0, 1, 1)

        self.input_precoCompra = QLineEdit(self.frame_31)
        self.input_precoCompra.setObjectName(u"input_precoCompra")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.input_precoCompra.sizePolicy().hasHeightForWidth())
        self.input_precoCompra.setSizePolicy(sizePolicy2)
        self.input_precoCompra.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamily(u"Raleway")
        self.input_precoCompra.setFont(font2)
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
        self.label_26.setFont(font1)

        self.gridLayout_30.addWidget(self.label_26, 0, 0, 1, 1)

        self.input_precoVenda = QLineEdit(self.frame_33)
        self.input_precoVenda.setObjectName(u"input_precoVenda")
        sizePolicy2.setHeightForWidth(self.input_precoVenda.sizePolicy().hasHeightForWidth())
        self.input_precoVenda.setSizePolicy(sizePolicy2)
        self.input_precoVenda.setMaximumSize(QSize(16777215, 30))
        self.input_precoVenda.setFont(font2)
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
        self.label_22.setFont(font1)

        self.gridLayout_26.addWidget(self.label_22, 0, 0, 1, 1)

        self.input_lucro = QLineEdit(self.frame_29)
        self.input_lucro.setObjectName(u"input_lucro")
        sizePolicy2.setHeightForWidth(self.input_lucro.sizePolicy().hasHeightForWidth())
        self.input_lucro.setSizePolicy(sizePolicy2)
        self.input_lucro.setMaximumSize(QSize(16777215, 30))
        self.input_lucro.setFont(font2)
        self.input_lucro.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")
        self.input_lucro.setReadOnly(True)

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
        self.label_25.setFont(font1)

        self.gridLayout_29.addWidget(self.label_25, 0, 0, 1, 1)

        self.inputMargem = QLineEdit(self.frame_32)
        self.inputMargem.setObjectName(u"inputMargem")
        sizePolicy2.setHeightForWidth(self.inputMargem.sizePolicy().hasHeightForWidth())
        self.inputMargem.setSizePolicy(sizePolicy2)
        self.inputMargem.setMaximumSize(QSize(16777215, 30))
        self.inputMargem.setFont(font2)
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
        self.label_21.setFont(font1)

        self.gridLayout_25.addWidget(self.label_21, 0, 0, 1, 1)

        self.input_precoAtacado = QLineEdit(self.frame_28)
        self.input_precoAtacado.setObjectName(u"input_precoAtacado")
        sizePolicy2.setHeightForWidth(self.input_precoAtacado.sizePolicy().hasHeightForWidth())
        self.input_precoAtacado.setSizePolicy(sizePolicy2)
        self.input_precoAtacado.setMaximumSize(QSize(16777215, 30))
        self.input_precoAtacado.setFont(font2)
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


        self.gridLayout_8.addWidget(self.frame_27, 1, 0, 1, 3)

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
        self.btn_salvar = QPushButton(self.frame_7)
        self.btn_salvar.setObjectName(u"btn_salvar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_salvar.sizePolicy().hasHeightForWidth())
        self.btn_salvar.setSizePolicy(sizePolicy3)
        self.btn_salvar.setMinimumSize(QSize(0, 35))
        self.btn_salvar.setMaximumSize(QSize(200, 35))
        font3 = QFont()
        font3.setFamily(u"Raleway")
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setWeight(75)
        self.btn_salvar.setFont(font3)
        self.btn_salvar.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.btn_salvar)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout_8.addWidget(self.frame_7, 3, 0, 1, 1)

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
        sizePolicy1.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy1)
        self.frame_38.setMaximumSize(QSize(16777215, 70))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.gridLayout_35 = QGridLayout(self.frame_38)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(0, 9, 0, -1)
        self.label_30 = QLabel(self.frame_38)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font1)

        self.gridLayout_35.addWidget(self.label_30, 0, 0, 1, 1)

        self.input_descricao = QLineEdit(self.frame_38)
        self.input_descricao.setObjectName(u"input_descricao")
        sizePolicy2.setHeightForWidth(self.input_descricao.sizePolicy().hasHeightForWidth())
        self.input_descricao.setSizePolicy(sizePolicy2)
        self.input_descricao.setMaximumSize(QSize(16777215, 30))
        self.input_descricao.setFont(font2)
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
        self.label_29.setFont(font1)

        self.gridLayout_34.addWidget(self.label_29, 0, 0, 1, 1)

        self.input_codBarras = QLineEdit(self.frame_37)
        self.input_codBarras.setObjectName(u"input_codBarras")
        sizePolicy2.setHeightForWidth(self.input_codBarras.sizePolicy().hasHeightForWidth())
        self.input_codBarras.setSizePolicy(sizePolicy2)
        self.input_codBarras.setMaximumSize(QSize(16777215, 30))
        self.input_codBarras.setFont(font2)
        self.input_codBarras.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_34.addWidget(self.input_codBarras, 1, 0, 1, 1)


        self.gridLayout_31.addWidget(self.frame_37, 0, 0, 1, 1)

        self.frame_40 = QFrame(self.frame_34)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy1.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy1)
        self.frame_40.setMinimumSize(QSize(150, 0))
        self.frame_40.setMaximumSize(QSize(150, 16777215))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.gridLayout_36 = QGridLayout(self.frame_40)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.gridLayout_36.setContentsMargins(0, 9, 0, -1)
        self.input_fornecedor = QComboBox(self.frame_40)
        self.input_fornecedor.addItem("")
        self.input_fornecedor.addItem("")
        self.input_fornecedor.addItem("")
        self.input_fornecedor.addItem("")
        self.input_fornecedor.addItem("")
        self.input_fornecedor.setObjectName(u"input_fornecedor")
        sizePolicy.setHeightForWidth(self.input_fornecedor.sizePolicy().hasHeightForWidth())
        self.input_fornecedor.setSizePolicy(sizePolicy)
        self.input_fornecedor.setMaximumSize(QSize(16777215, 30))
        self.input_fornecedor.setStyleSheet(u"QComboBox {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_36.addWidget(self.input_fornecedor, 1, 0, 1, 1)

        self.label_28 = QLabel(self.frame_40)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)

        self.gridLayout_36.addWidget(self.label_28, 0, 0, 1, 1)


        self.gridLayout_31.addWidget(self.frame_40, 0, 2, 1, 1)


        self.gridLayout_8.addWidget(self.frame_34, 0, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_5, 2, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_6, 0, 2, 1, 1)

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
        self.label_33.setFont(font1)

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
        self.label_34.setFont(font1)

        self.gridLayout_40.addWidget(self.label_34, 0, 0, 1, 1)

        self.input_estoqueAtual = QLineEdit(self.frame_43)
        self.input_estoqueAtual.setObjectName(u"input_estoqueAtual")
        sizePolicy2.setHeightForWidth(self.input_estoqueAtual.sizePolicy().hasHeightForWidth())
        self.input_estoqueAtual.setSizePolicy(sizePolicy2)
        self.input_estoqueAtual.setMaximumSize(QSize(16777215, 30))
        self.input_estoqueAtual.setFont(font2)
        self.input_estoqueAtual.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")
        self.input_estoqueAtual.setReadOnly(True)

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
        self.label_27.setFont(font1)

        self.gridLayout_33.addWidget(self.label_27, 0, 0, 1, 1)

        self.input_cor = QComboBox(self.frame_36)
        self.input_cor.addItem("")
        self.input_cor.setObjectName(u"input_cor")
        sizePolicy2.setHeightForWidth(self.input_cor.sizePolicy().hasHeightForWidth())
        self.input_cor.setSizePolicy(sizePolicy2)
        self.input_cor.setMinimumSize(QSize(100, 0))
        self.input_cor.setMaximumSize(QSize(100, 30))
        self.input_cor.setStyleSheet(u"QComboBox {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")
        self.input_cor.setEditable(True)

        self.gridLayout_33.addWidget(self.input_cor, 1, 0, 1, 1)


        self.gridLayout_32.addWidget(self.frame_36, 0, 1, 1, 1)

        self.frame_45 = QFrame(self.frame_35)
        self.frame_45.setObjectName(u"frame_45")
        sizePolicy1.setHeightForWidth(self.frame_45.sizePolicy().hasHeightForWidth())
        self.frame_45.setSizePolicy(sizePolicy1)
        self.frame_45.setMaximumSize(QSize(100, 70))
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.gridLayout_46 = QGridLayout(self.frame_45)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.gridLayout_46.setContentsMargins(0, 9, 0, -1)
        self.label_39 = QLabel(self.frame_45)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font1)

        self.gridLayout_46.addWidget(self.label_39, 0, 0, 1, 1)

        self.input_tamanho = QLineEdit(self.frame_45)
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

        self.gridLayout_46.addWidget(self.input_tamanho, 1, 0, 1, 1)


        self.gridLayout_32.addWidget(self.frame_45, 0, 2, 1, 1)


        self.gridLayout_8.addWidget(self.frame_35, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer, 4, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_8, 1, 0, 1, 1)

        QWidget.setTabOrder(self.input_codBarras, self.input_descricao)
        QWidget.setTabOrder(self.input_descricao, self.input_unidade)
        QWidget.setTabOrder(self.input_unidade, self.input_precoCompra)
        QWidget.setTabOrder(self.input_precoCompra, self.inputMargem)
        QWidget.setTabOrder(self.inputMargem, self.input_lucro)
        QWidget.setTabOrder(self.input_lucro, self.input_precoVenda)
        QWidget.setTabOrder(self.input_precoVenda, self.input_precoAtacado)
        QWidget.setTabOrder(self.input_precoAtacado, self.input_estoqueAtual)
        QWidget.setTabOrder(self.input_estoqueAtual, self.input_observacao)
        QWidget.setTabOrder(self.input_observacao, self.btn_salvar)

        self.retranslateUi(EstoqueEdit)

        QMetaObject.connectSlotsByName(EstoqueEdit)
    # setupUi

    def retranslateUi(self, EstoqueEdit):
        EstoqueEdit.setWindowTitle(QCoreApplication.translate("EstoqueEdit", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("EstoqueEdit", u"Editar Produto", None))
        self.input_unidade.setItemText(0, "")
        self.input_unidade.setItemText(1, QCoreApplication.translate("EstoqueEdit", u"UNI", None))
        self.input_unidade.setItemText(2, QCoreApplication.translate("EstoqueEdit", u"CX", None))
        self.input_unidade.setItemText(3, QCoreApplication.translate("EstoqueEdit", u"KG", None))
        self.input_unidade.setItemText(4, QCoreApplication.translate("EstoqueEdit", u"PC", None))

        self.label_23.setText(QCoreApplication.translate("EstoqueEdit", u"Unidade", None))
        self.label_24.setText(QCoreApplication.translate("EstoqueEdit", u"Pre\u00e7o Compra", None))
        self.input_precoCompra.setPlaceholderText(QCoreApplication.translate("EstoqueEdit", u"Ex.: 45,99", None))
        self.label_26.setText(QCoreApplication.translate("EstoqueEdit", u"Pre\u00e7o Venda", None))
        self.input_precoVenda.setPlaceholderText(QCoreApplication.translate("EstoqueEdit", u"Ex.: 45,99", None))
        self.label_22.setText(QCoreApplication.translate("EstoqueEdit", u"Lucro", None))
        self.input_lucro.setText("")
        self.input_lucro.setPlaceholderText(QCoreApplication.translate("EstoqueEdit", u"Ex.: 45,99", None))
        self.label_25.setText(QCoreApplication.translate("EstoqueEdit", u"Margem/Markup", None))
        self.inputMargem.setPlaceholderText(QCoreApplication.translate("EstoqueEdit", u"Ex.: 13", None))
        self.label_21.setText(QCoreApplication.translate("EstoqueEdit", u"Pre\u00e7o Atacado", None))
        self.input_precoAtacado.setPlaceholderText(QCoreApplication.translate("EstoqueEdit", u"Ex.: 45,99", None))
        self.btn_salvar.setText(QCoreApplication.translate("EstoqueEdit", u"Salvar", None))
        self.label_30.setText(QCoreApplication.translate("EstoqueEdit", u"Descri\u00e7\u00e3o", None))
        self.input_descricao.setPlaceholderText(QCoreApplication.translate("EstoqueEdit", u"Ex.: T\u00caNIS", None))
        self.label_29.setText(QCoreApplication.translate("EstoqueEdit", u"C\u00f3digo/C\u00f3d Barras", None))
        self.input_fornecedor.setItemText(0, "")
        self.input_fornecedor.setItemText(1, QCoreApplication.translate("EstoqueEdit", u"UNI", None))
        self.input_fornecedor.setItemText(2, QCoreApplication.translate("EstoqueEdit", u"CX", None))
        self.input_fornecedor.setItemText(3, QCoreApplication.translate("EstoqueEdit", u"KG", None))
        self.input_fornecedor.setItemText(4, QCoreApplication.translate("EstoqueEdit", u"PC", None))

        self.label_28.setText(QCoreApplication.translate("EstoqueEdit", u"Fornecedor", None))
        self.label_33.setText(QCoreApplication.translate("EstoqueEdit", u"Observa\u00e7\u00e3o", None))
        self.label_34.setText(QCoreApplication.translate("EstoqueEdit", u"Estoque Atual", None))
        self.input_estoqueAtual.setPlaceholderText(QCoreApplication.translate("EstoqueEdit", u"Ex.: 50", None))
        self.label_27.setText(QCoreApplication.translate("EstoqueEdit", u"Cor", None))
        self.input_cor.setItemText(0, "")

        self.label_39.setText(QCoreApplication.translate("EstoqueEdit", u"Tamanho", None))
        self.input_tamanho.setPlaceholderText(QCoreApplication.translate("EstoqueEdit", u"Ex.: VERDE", None))
    # retranslateUi

