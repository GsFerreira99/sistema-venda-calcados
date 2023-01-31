from sistema.funcoes.tabela import Tabela
from sistema.database.banco import DataBase
from PySide2.QtWidgets import QTableWidgetItem, QHeaderView, QTableWidget

import pandas as pd


class UsuarioModel:

    dados: pd.Series

    def __init__(self, db, dados: pd.Series):
        self.__db = db
        self.dados = dados

    def salvar(self):
        insert = self.__db.inserir(
            """
            INSERT INTO usuarios (
                usuario,
                senha,
                nome,
                sobrenome,
                tipo)
                VALUES (%s, %s, %s, %s, %s)
                """, self.dados.tolist())
        return insert

    def deletar(self):
        if int(self.dados['id']) == 1:
            return False

        self.__db.atualizar(f"""UPDATE usuarios
                                SET ativado = FALSE
                                WHERE id = {self.dados['id']};""")

    def editar(self):
        if self.dados['id'] == 1 and self.dados['tipo'] != 1:
            return False
        else:
            update = self.__db.atualizar(
                f"""
                UPDATE usuarios
                SET
                    usuario = '{self.dados['usuario']}',
                    senha = '{self.dados['senha']}',
                    nome = '{self.dados['nome']}',
                    sobrenome = '{self.dados['sobrenome']}',
                    tipo = '{self.dados['tipo']}'
                WHERE
                    id = {self.dados['id']}
                    """)
            return update


    def atualizar_dados(self, dados: dict):
        dados['id'] = self.dados['id']
        self.dados = pd.Series(dados)

    def __getitem__(self, item):
        return self.dados[item]

    def __setitem__(self, key, value):
        self.dados[key] = value

    def __str__(self) -> str:
        return self.dados['nome']


class TabelaUsuario(Tabela):

    tabela: QTableWidget

    def __init__(self, obj: QTableWidget, df, db: DataBase):
        super().__init__(obj, df, db)
        self.resize_colum(1, QHeaderView.Stretch)

    def preencher_tabela(self):
        self.limpar()

        nrows, ncolums = self.df.shape
        self.tabela.setRowCount(nrows)
        for row in range(nrows):
            self.tabela.setItem(row, 0, QTableWidgetItem(str(self.df.iloc[row, 0])))
            self.tabela.setItem(row, 1, QTableWidgetItem(str(self.df.iloc[row, 1])))
            self.tabela.setItem(row, 2, QTableWidgetItem(self.df.iloc[row, 3]))
            self.tabela.setItem(row, 3, QTableWidgetItem(self.df.iloc[row, 4]))
            self.tabela.setItem(row, 4, QTableWidgetItem(str(self.df.iloc[row, 5])))

