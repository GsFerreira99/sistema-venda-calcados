from sistema.controller.estoque_controller import EstoqueController
from sistema.view.main_view import MainView
from sistema.controller.login_controller import LoginController
from sistema.controller.vendas_controller import VendasController
from sistema.controller.cliente_controller import ClienteController
from sistema.controller.fornecedor_controller import FornecedorController
from sistema.controller.usuario_controller import UsuarioController

import json


from sistema.view import vendas_view

from sistema.database.banco import DataBase

from PySide2.QtWidgets import QWidget


class MainController:

    def __init__(self, parent=None) -> None:
        self.parent = parent
        self.view = MainView(self.parent)

        credenciais = self.dados_db()
        self.__db = DataBase(credenciais['ip'], credenciais['usuario'], credenciais['senha'], credenciais['porta'])
        #self.__db = DataBase("192.168.75.60", 'admin', '331088', '3306')
        #self.__db = DataBase("localhost", 'gabriel', 'Gabriel151299', '3306')
        self.conectar_db()

        self.login = LoginController(self.__db)
        self.vendas = VendasController(self.__db, vendas_view.VendasView())
        self.estoque = EstoqueController(self.__db)
        self.clientes = ClienteController(self.__db)
        self.fornecedor = FornecedorController(self.__db)
        self.usuario = UsuarioController(self.__db)

        self.__usuario = None

        self.login.view.btn_acessar.clicked.connect(lambda: self.acessar_sistema())
        self.view.btn_menu.clicked.connect(lambda: self.menu_lateral())

        self.view.btn_vendas.clicked.connect(lambda: self.navegacao(1))
        self.view.btn_estoque.clicked.connect(lambda: self.navegacao(2))
        self.view.btn_clientes.clicked.connect(lambda: self.navegacao(3))
        self.view.btn_fornecedores.clicked.connect(lambda: self.navegacao(4))
        self.view.btn_usuarios.clicked.connect(lambda: self.navegacao(5))

    def definir_telas(self):
        self.parent.insertWidget(1, self.login.view)
        self.parent.insertWidget(2, self.view)

        self.parent.setCurrentIndex(0)

    def verificar_admin(self):
        if self.__usuario['tipo'][0] != 1:
            self.view.btn_usuarios.setEnabled(False)

    def dados_db(self):
        with open("dados.json", encoding='utf-8') as meu_json:
            return json.load(meu_json)[0]

    def conectar_db(self):
        self.__db.conectar()

    def navegacao(self, index: int):
        telas = {
            1: [self.view.btn_vendas, "Vendas", self.vendas.view],
            2: [self.view.btn_estoque, "Estoque", self.estoque.view],
            3: [self.view.btn_clientes, "Clientes", self.clientes.view],
            4: [self.view.btn_fornecedores, "Fornecedores", self.fornecedor.view],
            5: [self.view.btn_usuarios, "Usuarios", self.usuario.view],
        }
        self.view.navegacao(index, telas)

    def menu_lateral(self):
        self.view.animacao_menu_lateral(self)

    def definir_telas_sistema(self):
        self.view.content.insertWidget(1, QWidget())
        self.view.content.insertWidget(2, self.vendas.view)
        self.view.content.insertWidget(3, self.estoque.view)
        self.view.content.insertWidget(4, self.clientes.view)
        self.view.content.insertWidget(5, self.fornecedor.view)
        self.view.content.insertWidget(6, self.usuario.view)

        self.view.content.setCurrentIndex(0)

    def acessar_sistema(self):
        self.__usuario = self.login.acessar_sistema()
        try:
            if self.__usuario.empty is False:
                self.vendas.definir_user(self.__usuario)
                self.verificar_admin()
                self.parent.setCurrentIndex(1)
                self.parent.setMinimumSize(1200, 700)
                self.parent.showMaximized()
        except AttributeError:
            return
