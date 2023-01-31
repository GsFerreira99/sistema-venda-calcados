# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'valor_editsinegX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_EditValor(object):
    def setupUi(self, EditValor):
        if not EditValor.objectName():
            EditValor.setObjectName(u"EditValor")
        EditValor.resize(330, 165)
        EditValor.setMinimumSize(QSize(330, 165))
        EditValor.setMaximumSize(QSize(330, 165))
        EditValor.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(236, 242, 248);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(EditValor)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, -1, 30, -1)
        self.texto = QLabel(EditValor)
        self.texto.setObjectName(u"texto")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.texto.sizePolicy().hasHeightForWidth())
        self.texto.setSizePolicy(sizePolicy)
        self.texto.setMaximumSize(QSize(300, 30))
        font = QFont()
        font.setFamily(u"Raleway")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.texto.setFont(font)
        self.texto.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.texto)

        self.frame_7 = QFrame(EditValor)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setMaximumSize(QSize(16777215, 100))
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
        self.frame_38 = QFrame(self.frame_7)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy1.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy1)
        self.frame_38.setMinimumSize(QSize(0, 70))
        self.frame_38.setMaximumSize(QSize(130, 70))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.gridLayout_35 = QGridLayout(self.frame_38)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(0, 9, 0, -1)
        self.input = QLineEdit(self.frame_38)
        self.input.setObjectName(u"input")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy2)
        self.input.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamily(u"Raleway")
        self.input.setFont(font1)
        self.input.setStyleSheet(u"QLineEdit {\n"
"	background-color:white;\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgb(158, 162, 166);\n"
"	padding-left: 20px;\n"
"}")

        self.gridLayout_35.addWidget(self.input, 1, 0, 1, 1)

        self.label_30 = QLabel(self.frame_38)
        self.label_30.setObjectName(u"label_30")
        font2 = QFont()
        font2.setFamily(u"Raleway")
        font2.setPointSize(8)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_30.setFont(font2)

        self.gridLayout_35.addWidget(self.label_30, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_38)

        self.frame = QFrame(self.frame_7)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 16, 0, 0)
        self.btn_salvar = QPushButton(self.frame)
        self.btn_salvar.setObjectName(u"btn_salvar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_salvar.sizePolicy().hasHeightForWidth())
        self.btn_salvar.setSizePolicy(sizePolicy3)
        self.btn_salvar.setMinimumSize(QSize(0, 35))
        self.btn_salvar.setMaximumSize(QSize(100, 35))
        font3 = QFont()
        font3.setFamily(u"Raleway")
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setWeight(75)
        self.btn_salvar.setFont(font3)
        self.btn_salvar.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_salvar)


        self.horizontalLayout_3.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_7)


        self.retranslateUi(EditValor)

        QMetaObject.connectSlotsByName(EditValor)
    # setupUi

    def retranslateUi(self, EditValor):
        EditValor.setWindowTitle(QCoreApplication.translate("EditValor", u"Form", None))
        self.texto.setText(QCoreApplication.translate("EditValor", u"TEXTO", None))
        self.label_30.setText("")
        self.btn_salvar.setText(QCoreApplication.translate("EditValor", u"Salvar", None))
    # retranslateUi

