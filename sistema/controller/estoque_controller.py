from sistema.view.estoque_view import EstoqueView
from sistema.model.estoque_model import EstoqueModel, TabelaEstoque
from sistema.funcoes.poupup import mensagem

from PySide2.QtWidgets import QMessageBox

import pandas as pd



class EstoqueController:

    def __init__(self, db) -> None:

        self.__db = db
        self.view = EstoqueView()
        
        self.limpar_tela()

        self.view.btn_consulta.clicked.connect(lambda: self.view.navegacao(1))
        self.view.btn_novo.clicked.connect(lambda: self.view.navegacao(2))

        self.view.btn_salvar.clicked.connect(lambda: self.cadastrar_estoque())


        self.view.btn_busca.clicked.connect(lambda: self.busca())

    def busca(self):
        campo = self.view.btn_busca.text()
        table = TabelaEstoque(self.view.table_produtos, self.__db.select("SELECT * FROM estoque"), self.__db)

        table.preencher_tabela()


    def limpar_tela(self):
        cor = self.__db.select("SELECT DISTINCT cor FROM estoque")['cor'].values.tolist()
        fornecedor = self.__db.select("SELECT DISTINCT nome FROM fornecedor")['nome'].values.tolist()
        self.view.limpar(cor, fornecedor)

    def cadastrar_estoque(self):
        dados = pd.Series(self.view.receber_dados())
        dados['fornecedorId'] = int(self.__db.select(f"SELECT id FROM fornecedor WHERE nome = '{dados['fornecedorId']}'").iloc[0,0])
        estoque = EstoqueModel(self.__db, dados)
        if estoque.salvar() == True:
            texto = "Produto Adicionado com sucesso!"
            self.limpar_tela()
        else:
            texto = "Erro ao inserir produto, verifique os campos."
        mensagem(texto, QMessageBox.Information, 'Info')    