from datetime import datetime
from sistema.view.cliente_view import ClienteView
from sistema.model.cliente_model import ClienteModel, TabelaCliente

from sistema.funcoes.poupup import mensagem, confirma
from PySide2.QtWidgets import QMessageBox

import pandas as pd

class ClienteController:

    def __init__(self, db) -> None:
        self.__db = db
        self.view = ClienteView()

        self.view.btn_consulta.clicked.connect(lambda: self.view.navegacao(1))
        self.view.btn_novo.clicked.connect(lambda: self.view.navegacao(2))
    
        self.view.btn_salvar.clicked.connect(lambda: self.cadastrar_fornecedor())

        self.view.btn_busca.clicked.connect(lambda: self.busca())
        self.view.btn_deletar.clicked.connect(lambda: self.deletar())

    def deletar(self):
        model = ClienteModel(self.__db, self.table.retorna_objeto(self.view.linha_selecionada()))
        status = confirma(f"Deseja deletar o produto '{model.dados['nome']}'?", QMessageBox.Information, 'Confirmação')
        if status == True:
            status = model.deletar()
            mensagem(f"Cliente '{model.dados['nome']}' deletado com sucesso.", QMessageBox.Information, 'Info')
            self.busca()

    def cadastrar_fornecedor(self):
        cliente = ClienteModel(self.__db, pd.Series(self.view.receber_dados()))
        cliente.dados['criado_em'] = datetime.now().strftime('%Y-%m-%d')
        if cliente.salvar() == True:
            texto = "Fornecedor Adicionado com sucesso!"
            self.limpar_tela()
        else:
            texto = "Erro ao inserir fornecedor, verifique os campos."
        mensagem(texto, QMessageBox.Information, 'Info')

    def limpar_tela(self):
        self.view.limpar()

    def busca(self):
        campo = self.view.btn_busca.text()
        self.table = TabelaCliente(self.view.table_clientes, self.__db.select("SELECT * FROM cliente"), self.__db)

        self.table.preencher_tabela()