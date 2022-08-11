from sistema.view.main_view import MainView
from sistema.controller.login_controller import LoginController
from sistema.controller.vendas_controller import VendasController

from PySide2.QtWidgets import QWidget

class MainController:

    def __init__(self, parent=None) -> None:
        self.parent = parent
        
        self.view = MainView()
        
        #Controllers
        self.login = LoginController()
        self.vendas = VendasController()

        self.login.view.btn_acessar.clicked.connect(lambda: self.acessar_sistema())
        self.view.btn_menu.clicked.connect(lambda: self.menu_lateral())

        self.view.btn_vendas.clicked.connect(lambda: self.navegacao(1))

    def definir_telas(self):
        self.parent.insertWidget(1, self.login.view)
        self.parent.insertWidget(2, self.view)

        self.parent.setCurrentIndex(0)

    def navegacao(self, index:int):
        botoes = {
            1 : self.view.btn_vendas
        }

        self.view.content.setCurrentIndex(index)

        for ind, botao in botoes.items():
            if ind == index:
                botao.setStyleSheet("""
                    QPushButton{
                        border: none;
                        border-radius: none;
                        border-bottom: 2px solid rgb(42, 68, 103);
                        background-color:rgb(124, 143, 177)
                    }
                """)
            else:
                botao.setStyleSheet("""
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

    def menu_lateral(self):
        self.view.animacao_menu_lateral(self)

    def definir_telas_sistema(self):
        self.view.content.insertWidget(1, QWidget())
        self.view.content.insertWidget(2, self.vendas.view)

        self.view.content.setCurrentIndex(0)

    def acessar_sistema(self):
        if self.login.acessar_sistema() == True:
            self.parent.setCurrentIndex(1)
            self.parent.showMaximized()