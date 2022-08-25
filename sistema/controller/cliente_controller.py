from datetime import datetime
from sistema.view.cliente_view import ClienteView
from sistema.view.cliente_edit_view import ClienteEditView
from sistema.model.cliente_model import ClienteModel, TabelaCliente

from sistema.funcoes.poupup import mensagem, confirma
from PySide2.QtWidgets import QMessageBox

import pandas as pd


class ClienteController:

    table: TabelaCliente
    modelEdit: ClienteModel

    def __init__(self, db) -> None:
        self.__db = db
        self.view = ClienteView()
        self.edit = ClienteEditView()

        self.view.btn_consulta.clicked.connect(lambda: self.view.navegacao(1))
        self.view.btn_novo.clicked.connect(lambda: self.view.navegacao(2))
    
        self.view.btn_salvar.clicked.connect(lambda: self.cadastrar_fornecedor())
        self.edit.btn_salvar.clicked.connect(lambda: self.salvar_edicao())

        self.view.btn_editar.clicked.connect(lambda: self.editar())
        self.view.btn_busca.clicked.connect(lambda: self.busca())
        self.view.btn_deletar.clicked.connect(lambda: self.deletar())

    def deletar(self):
        model = ClienteModel(self.__db, self.table.retorna_objeto(self.view.linha_selecionada()))
        status = confirma(f"Deseja deletar o produto '{model.dados['nome']}'?", QMessageBox.Information, 'Confirmação')
        if status is True:
            model.deletar()
            mensagem(f"Cliente '{model.dados['nome']}' deletado com sucesso.", QMessageBox.Information, 'Info')
            self.busca()

    def editar(self):
        objeto = self.table.retorna_objeto(self.view.linha_selecionada())
        self.modelEdit = ClienteModel(self.__db, objeto)
        self.limpar_tela()
        self.edit.preencher_campos(self.modelEdit.dados)
        self.edit.show()

    def salvar_edicao(self):
        self.modelEdit.atualizar_dados(self.edit.receber_dados())
        if self.modelEdit.editar():
            texto = "Cliente editado com sucesso!"
            self.limpar_tela()
            self.edit.close()
            self.busca()
        else:
            texto = "Erro ao atualizar cliente, verifique os campos."
        mensagem(texto, QMessageBox.Information, 'Info')

    def cadastrar_fornecedor(self):
        cliente = ClienteModel(self.__db, pd.Series(self.view.receber_dados()))
        cliente.dados['criado_em'] = datetime.now().strftime('%Y-%m-%d')
        if cliente.salvar() is True:
            texto = "Cliente Adicionado com sucesso!"
            self.limpar_tela()
        else:
            texto = "Erro ao inserir Cliente, verifique os campos."
        mensagem(texto, QMessageBox.Information, 'Info')

    def limpar_tela(self):
        self.view.limpar()

    def busca(self):
        campo = self.view.input_pesquisa.text()
        if campo == '':
            select = self.__db.select("SELECT * FROM cliente")
        else:
            select = self.__db.select(f"""SELECT * FROM cliente WHERE nome LIKE '%{campo}%' 
            OR cpf_cnpj = '{campo}' OR celular = '{campo}' OR inscricao_estadual = '{campo}' OR email = '{campo}'""")
        self.table = TabelaCliente(self.view.table_clientes, select, self.__db)
        self.table.preencher_tabela()
