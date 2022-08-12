#PySide2
from PySide2.QtWidgets import QWidget

#Telas
from interface.telas.estoque import Ui_Estoque

class EstoqueView(Ui_Estoque, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

    def navegacao(self, index:int):
        botoes = {
            1 : self.btn_consulta,
            2 : self.btn_novo
        }
 
        self.stackedWidget.setCurrentIndex(index)

        for ind, botao in botoes.items():
            if ind == index:
                botao.setStyleSheet("""
                    QPushButton{
                        color: white;
                        border: none;
                        border-radius: 0;
                        border-top-left-radius: 10px;
                        border-top-right-radius: 10px;
                        background-color: rgb(56, 91, 138)
                    }
                """)
            else:
                botao.setStyleSheet("""
                    QPushButton{
                        color: white;
                        border: none;
                        border-radius: 0;
                        border-top-left-radius: 10px;
                        border-top-right-radius: 10px;
                        background-color: rgb(74, 121, 184)
                    }

                    QPushButton:hover{
                        background-color: rgb(89, 146, 221)
                    }

                    QPushButton:pressed{
                        background-color: rgb(42, 68, 103)
                    }
                """)
