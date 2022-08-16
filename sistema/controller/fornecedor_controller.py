from sistema.view.fornecedor_view import FornecedorView
from sistema.model.fornecedore_model import FornecedorModel

from sistema.funcoes.poupup import mensagem
from PySide2.QtWidgets import QMessageBox

import pandas as pd


class FornecedorController:

    def __init__(self, db) -> None:
        self.__db = db
        self.view = FornecedorView()

        self.view.btn_consulta.clicked.connect(lambda: self.view.navegacao(1))
        self.view.btn_novo.clicked.connect(lambda: self.view.navegacao(2))

        self.view.btn_salvar.clicked.connect(lambda: self.cadastrar_fornecedor())

    def cadastrar_fornecedor(self):
        fornecedor = FornecedorModel(self.__db, pd.Series(self.view.receber_dados()))
        if fornecedor.salvar() == True:
            texto = "Fornecedor Adicionado com sucesso!"
            self.limpar_tela()
        else:
            texto = "Erro ao inserir fornecedor, verifique os campos."
        mensagem(texto, QMessageBox.Information, 'Info')

    def limpar_tela(self):
        self.view.limpar()