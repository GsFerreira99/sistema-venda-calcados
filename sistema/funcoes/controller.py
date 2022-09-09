from sistema.database.banco import DataBase
from sistema.funcoes.tabela import Tabela
from sistema.funcoes.model import Model
from sistema.funcoes.view import View
from sistema.funcoes.poupup import mensagem, confirma
from PySide2.QtWidgets import QMessageBox


class Controller:

    table: Tabela
    model: Model

    def __init__(self, db: DataBase, view):
        """ex: db= DataBase(), view= View(), edit_view=View()"""
        self.db = db
        self.view = view

        self.view.btn_consulta.clicked.connect(lambda: self.view.navegacao(1))
        self.view.btn_novo.clicked.connect(lambda: self.view.navegacao(2))

    def definir_model(self, model: Model):
        self.model = model

    def deletar(self):
        """ex: model= Model()"""
        status = confirma(f"Deseja deletar '{self.model.dados['nome']}'?", QMessageBox.Information, 'Confirmação')
        if status is True:
            self.model.deletar(f"DELETE FROM {self.model.tabela_sql} WHERE id = {self.model.dados['id']}")
            mensagem(f"Cliente '{self.model.dados['nome']}' deletado com sucesso.", QMessageBox.Information, 'Info')
            """self.busca()"""

    def limpar_tela(self):
        """Chama método limpar da View"""
        self.view.limpar()

    def busca(self, campo: str, tabela_db: str, sql: str, tabela_class: Tabela):
        """ex: campo='Gabriel', tabela_db='cliente', sql='SELECT * FROM cliente WHERE nome LIKE '%Gabriel%',
        tabela_class=Tabela()"""
        dados = self.db.pesquisar(campo, tabela_db, sql)
        self.table = tabela_class
        self.table.atualizar_df(dados)
        self.table.preencher_tabela()
