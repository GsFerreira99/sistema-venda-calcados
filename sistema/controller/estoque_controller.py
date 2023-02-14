from sistema.view.estoque_view import EstoqueView
from sistema.model.estoque_model import EstoqueModel, TabelaEstoque
from sistema.funcoes.poupup import mensagem, confirma
from sistema.view.estoque_edit_view import EstoqueEditView
from sistema.view.estoque_adicionar_view import EstoqueAdicionarView
from sistema.relatorios.estoque import RelatorioEstoque
from PySide2.QtWidgets import QMessageBox, QFileDialog

from PySide2.QtWidgets import QMessageBox

import pandas as pd


class EstoqueController:

    def __init__(self, db) -> None:

        self.__db = db
        self.view = EstoqueView()
        self.edit = EstoqueEditView()
        self.adicionar = EstoqueAdicionarView()

        self.modelEdit = None
        self.table = None

        self.limpar_tela(self.view)

        self.view.btn_consulta.clicked.connect(lambda: self.view.navegacao(1))
        self.view.btn_novo.clicked.connect(lambda: self.view.navegacao(2))

        self.view.btn_salvar.clicked.connect(lambda: self.cadastrar_estoque())
        self.edit.btn_salvar.clicked.connect(lambda: self.salvar_edicao())

        self.view.btn_relatorio.clicked.connect(lambda: self.relatorio())

        self.view.btn_editar.clicked.connect(lambda: self.editar())
        self.view.btn_busca.clicked.connect(lambda: self.busca())
        self.view.btn_deletar.clicked.connect(lambda: self.deletar())

        self.adicionar.btn_salvar.clicked.connect(lambda: self.salvar_adc_estoque())

    @staticmethod
    def caminho_relatorio():
        try:
            arquivo = QFileDialog.getSaveFileName(caption="Exportar relatório em PDF",
                                                  directory="", filter="PDF files (*.pdf)")[0]
            return arquivo
        except FileNotFoundError:
            return None

    def relatorio(self):
        caminho = self.caminho_relatorio()
        if type(caminho) != str or caminho == '':
            return

        forcedores = self.__db.select("SELECT id, nome FROM fornecedor")
        dados = {}
        for index, fornecedor in forcedores.iterrows():
            id = fornecedor['id']
            dados[fornecedor['nome']] = self.__db.select(f"SELECT * FROM estoque WHERE fornecedorId = {id}")

        rel = RelatorioEstoque(caminho).escrever(dados)

        mensagem('Relatório gerado com sucesso!.', QMessageBox.Information, 'Sucesso')

    def deletar(self):
        model = EstoqueModel(self.__db, self.table.retorna_objeto(self.view.linha_selecionada()))
        status = confirma(f"Deseja deletar o produto '{model['descricao']}'?", QMessageBox.Information,
                          'Confirmação')
        if status:
            model.deletar()
            mensagem(f"Produto '{model['descricao']}' deletado com sucesso.", QMessageBox.Information, 'Info')
            self.busca()

    def adicionar_estoque(self):
        self.adicionar.inserir_dados(self.table.retorna_objeto(self.view.linha_selecionada()))
        self.adicionar.editar_titulo()
        self.adicionar.show()

    def salvar_adc_estoque(self):
        val = self.adicionar.receber_dados()
        model = EstoqueModel(self.__db, self.adicionar.objeto)
        model.atualizar_estoque(val)
        self.adicionar.close()
        self.adicionar.limpar()
        model.adicionarEstoque()
        mensagem(f"Adicionado {val} ao estoque de'{model['descricao']}'.", QMessageBox.Information, 'Info')
        self.busca()

    def busca(self):
        campo = self.view.input_pesquisa.text()
        if campo == '':
            select = self.__db.select("SELECT * FROM estoque WHERE ativado = TRUE")
        else:
            select = self.__db.select(f"""SELECT * FROM estoque WHERE descricao LIKE '%{campo}%' 
            OR cod_barras = '{campo}' AND ativado = TRUE""")
        if select.empty is True:
            fornecedor = self.__db.select(f"SELECT id FROM fornecedor WHERE nome LIKE '%{campo}%' AND ativado = TRUE").iloc[0, 0]
            select = self.__db.select(f"SELECT * FROM estoque WHERE fornecedorId = {fornecedor} AND ativado = TRUE")
        self.table = TabelaEstoque(self.view.table_produtos, select, self.__db)
        self.table.preencher_tabela()

    def editar(self):
        objeto = self.table.retorna_objeto(self.view.linha_selecionada())
        objeto['fornecedorId'] = self.__db.select(
            f"SELECT nome FROM fornecedor WHERE id = '{objeto['fornecedorId']}'").iloc[0, 0]
        self.modelEdit = EstoqueModel(self.__db, objeto)
        self.limpar_tela(self.edit)
        self.edit.preencher_campos(self.modelEdit.dados)
        self.edit.show()

    def salvar_edicao(self):
        self.modelEdit.atualizar_dados(self.edit.receber_dados())
        self.modelEdit.dados['fornecedorId'] = int(self.__db.select(
            f"SELECT id FROM fornecedor WHERE nome = '{self.modelEdit['fornecedorId']}'").iloc[0, 0])
        if self.modelEdit.editar():
            texto = "Produto atualizado com sucesso!"
            self.limpar_tela(self.edit)
            self.edit.close()
            self.busca()
        else:
            texto = "Erro ao atualizar produto, verifique os campos."
        mensagem(texto, QMessageBox.Information, 'Info')

    def limpar_tela(self, view):
        cor = ''
        fornecedor = self.__db.select("SELECT DISTINCT nome FROM fornecedor WHERE ativado = TRUE")['nome'].values.tolist()
        view.limpar(cor, fornecedor)


    def cadastrar_estoque(self):
        dados = pd.Series(self.view.receber_dados())
        dados['fornecedorId'] = int(self.__db.select(
            f"SELECT id FROM fornecedor WHERE nome = '{dados['fornecedorId']}'").iloc[0, 0])
        estoque = EstoqueModel(self.__db, dados)
        if estoque.salvar():
            texto = "Produto Adicionado com sucesso!"
            self.limpar_tela(self.view)
        else:
            texto = "Erro ao inserir produto, verifique os campos."
        mensagem(texto, QMessageBox.Information, 'Info')
