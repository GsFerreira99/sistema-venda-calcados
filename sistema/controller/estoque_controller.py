from sistema.view.estoque_view import EstoqueView
from sistema.model.estoque_model import EstoqueModel, TabelaEstoque
from sistema.funcoes.poupup import mensagem, confirma
from sistema.view.estoque_edit_view import EstoqueEditView

from PySide2.QtWidgets import QMessageBox

import pandas as pd



class EstoqueController:

    def __init__(self, db) -> None:

        self.__db = db
        self.view = EstoqueView()
        self.edit = EstoqueEditView()
        
        self.limpar_tela(self.view)

        self.view.btn_consulta.clicked.connect(lambda: self.view.navegacao(1))
        self.view.btn_novo.clicked.connect(lambda: self.view.navegacao(2))

        self.view.btn_salvar.clicked.connect(lambda: self.cadastrar_estoque())
        self.edit.btn_salvar.clicked.connect(lambda: self.salvar_edicao())

        self.view.btn_editar.clicked.connect(lambda: self.editar())
        self.view.btn_busca.clicked.connect(lambda: self.busca())
        self.view.btn_deletar.clicked.connect(lambda: self.deletar())

    def deletar(self):
        model = EstoqueModel(self.__db, self.table.retorna_objeto(self.view.linha_selecionada()))
        status = confirma(f"Deseja deletar o produto '{model.dados['descricao']}'?", QMessageBox.Information, 'Confirmação')
        if status == True:
            status = model.deletar()
            mensagem(f"Produto '{model.dados['descricao']}' deletado com sucesso.", QMessageBox.Information, 'Info')
            self.busca()

    def busca(self):
        campo = self.view.btn_busca.text()
        self.table = TabelaEstoque(self.view.table_produtos, self.__db.select("SELECT * FROM estoque"), self.__db)

        self.table.preencher_tabela()

    def editar(self):
        objeto = self.table.retorna_objeto(self.view.linha_selecionada())
        objeto['fornecedorId'] = self.__db.select(f"SELECT nome FROM fornecedor WHERE id = '{objeto['fornecedorId']}'").iloc[0,0]
        self.modelEdit = EstoqueModel(self.__db, objeto)
        self.limpar_tela(self.edit)
        self.edit.preencher_campos(self.modelEdit.dados)
        self.edit.show()

    def salvar_edicao(self):
        self.modelEdit.atualizar_dados(self.edit.receber_dados())
        self.modelEdit.dados['fornecedorId'] = int(self.__db.select(f"SELECT id FROM fornecedor WHERE nome = '{self.modelEdit.dados['fornecedorId']}'").iloc[0,0])
        if self.modelEdit.editar() == True:
            texto = "Produto atualizado com sucesso!"
            self.limpar_tela(self.edit)
            self.edit.close()
            self.busca()
        else:
            texto = "Erro ao atualizar produto, verifique os campos."
        mensagem(texto, QMessageBox.Information, 'Info')  

    def limpar_tela(self, view):
        cor = self.__db.select("SELECT DISTINCT cor FROM estoque")['cor'].values.tolist()
        fornecedor = self.__db.select("SELECT DISTINCT nome FROM fornecedor")['nome'].values.tolist()
        view.limpar(cor, fornecedor)

    def cadastrar_estoque(self):
        dados = pd.Series(self.view.receber_dados())
        dados['fornecedorId'] = int(self.__db.select(f"SELECT id FROM fornecedor WHERE nome = '{dados['fornecedorId']}'").iloc[0,0])
        estoque = EstoqueModel(self.__db, dados)
        if estoque.salvar() == True:
            texto = "Produto Adicionado com sucesso!"
            self.limpar_tela(self.view)
        else:
            texto = "Erro ao inserir produto, verifique os campos."
        mensagem(texto, QMessageBox.Information, 'Info')    