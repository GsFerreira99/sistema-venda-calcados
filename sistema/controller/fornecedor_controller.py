from sistema.view.fornecedor_view import FornecedorView
from sistema.view.fornecedor_edit_view import FornecedorEditView
from sistema.model.fornecedore_model import FornecedorModel, TabelaFornecedor

from sistema.funcoes.poupup import mensagem, confirma
from PySide2.QtWidgets import QMessageBox

import pandas as pd


class FornecedorController:

    table: TabelaFornecedor
    modelEdit: FornecedorModel

    def __init__(self, db) -> None:
        self.__db = db
        self.view = FornecedorView()
        self.edit = FornecedorEditView()

        self.view.btn_consulta.clicked.connect(lambda: self.view.navegacao(1))
        self.view.btn_novo.clicked.connect(lambda: self.view.navegacao(2))

        self.view.btn_salvar.clicked.connect(lambda: self.cadastrar_fornecedor())
        self.edit.btn_salvar.clicked.connect(lambda: self.salvar_edicao())

        self.view.btn_editar.clicked.connect(lambda: self.editar())
        self.view.btn_busca.clicked.connect(lambda: self.busca())
        self.view.btn_deletar.clicked.connect(lambda: self.deletar())

    def deletar(self):
        model = FornecedorModel(self.__db, self.table.retorna_objeto(self.view.linha_selecionada()))
        status = confirma(f"Deseja deletar o fornecedor '{model.dados['nome']}'?", QMessageBox.Information,
                          'Confirmação')
        if status is True:
            status = model.deletar()
            if status is False:
                mensagem(f"""O fornecedor '{model.dados['nome']}' possui produtos cadastrados no estoque, 
                delete os produtos para poder exclui-lo.""", QMessageBox.Information, 'Info')
            else:
                mensagem(f"Fornecedor '{model.dados['nome']}' deletado com sucesso.", QMessageBox.Information, 'Info')
                self.busca()

    def cadastrar_fornecedor(self):
        fornecedor = FornecedorModel(self.__db, pd.Series(self.view.receber_dados()))
        if fornecedor.salvar() is True:
            texto = "Fornecedor Adicionado com sucesso!"
            self.limpar_tela()
        else:
            texto = "Erro ao inserir fornecedor, verifique os campos."
        mensagem(texto, QMessageBox.Information, 'Info')

    def limpar_tela(self):
        self.view.limpar()

    def busca(self):
        campo = self.view.input_pesquisa.text()
        if campo == '':
            select = self.__db.select("SELECT * FROM fornecedor")
        else:
            select = self.__db.select(f"""SELECT * FROM fornecedor WHERE nome LIKE '%{campo}%' 
            OR cpf_cnpj = '{campo}' OR inscricao_estadual = '{campo}' OR email = '{campo}' OR celular = '{campo}'""")

        self.table = TabelaFornecedor(self.view.table_fornecedores, select, self.__db)
        self.table.preencher_tabela()

    def editar(self):
        objeto = self.table.retorna_objeto(self.view.linha_selecionada())
        self.modelEdit = FornecedorModel(self.__db, objeto)
        self.limpar_tela()
        self.edit.preencher_campos(self.modelEdit.dados)
        self.edit.show()

    def salvar_edicao(self):
        self.modelEdit.atualizar_dados(self.edit.receber_dados())
        if self.modelEdit.editar():
            texto = "Fornecedor editado com sucesso!"
            self.limpar_tela()
            self.edit.close()
            self.busca()
        else:
            texto = "Erro ao atualizar fornecedor, verifique os campos."
        mensagem(texto, QMessageBox.Information, 'Info')
