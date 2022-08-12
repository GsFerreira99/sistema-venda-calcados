#PySide2
from PySide2.QtWidgets import QWidget
from funcoes.animacoes import toggle

#Telas
from interface.telas.main import Ui_Home


class MainView(Ui_Home, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

    def animacao_menu_lateral(self, ui):
        toggle.toggle_width(ui, self.left_bar, 150, True)

    def navegacao(self, index:int, telas:dict):
        self.content.setCurrentIndex(index)
        for ind, tela in telas.items():
            if ind == index:
                tela[2].navegacao(1)
                self.lb_titulo.setText(tela[1])
                tela[0].setStyleSheet("""
                    QPushButton{
                        border: none;
                        border-radius: none;
                        border-bottom: 2px solid rgb(42, 68, 103);
                        background-color:rgb(124, 143, 177)
                    }
                """)
            else:
                tela[0].setStyleSheet("""
                    QPushButton{
                        border: none;
                        border-radius: none;
                        border-bottom: 1px solid rgb(42, 68, 103)
                    }
                    QPushButton:hover{
                        border-bottom: 2px solid rgb(42, 68, 103);
                        background-color: rgb(139, 161, 199)
                    }
                    QPushButton:pressed{
                        background-color:rgb(124, 143, 177)
                    }
                """)

