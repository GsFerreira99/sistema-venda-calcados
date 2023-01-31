from sistema.funcoes.genericos import moeda
from sistema.funcoes.tabela import Tabela
from sistema.database.banco import DataBase
from PySide2.QtWidgets import QTableWidgetItem, QHeaderView, QTableWidget

import pandas as pd


class EstoqueModel:

    def __init__(self, db, dados: pd.Series):
        self.__db = db
        self.dados = dados

    def salvar(self):
        insert = self.__db.inserir(
            """
            INSERT INTO estoque (
                cod_barras,
                descricao,
                fornecedorId,
                unidade,
                preco_compra,
                margem,
                lucro,
                preco_venda,
                preco_atacado,
                observacao)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, self.dados.tolist())
        return insert

    def deletar(self):
        self.__db.atualizar(f"""UPDATE estoque
                            SET ativado = FALSE
                            WHERE id = {self.dados['id']};""")

    def __getitem__(self, item):
        return self.dados[item]

    def editar(self):
        update = self.__db.atualizar(
            f"""
            UPDATE estoque
            SET
                cod_barras = '{self.dados['cod_barras']}',
                descricao = '{self.dados['descricao']}',
                fornecedorId = {int(self.dados['fornecedorId'])},
                unidade = '{self.dados['unidade']}',
                preco_compra = {self.dados['preco_compra']},
                margem = {self.dados['margem']},
                lucro = {self.dados['lucro']},
                preco_venda = {self.dados['preco_venda']},
                preco_atacado = {self.dados['preco_atacado']},
                observacao = '{self.dados['observacao']}'
            WHERE
                id = {self.dados['id']}
                """)
        return update
    
    def adicionarEstoque(self):
        update = self.__db.atualizar(
            f"""
                    UPDATE estoque
                    SET
                        estoque_atual = {self.dados['estoque_atual']}
                    WHERE
                        id = {self.dados['id']}
                        """)
        return update

    def atualizar_estoque(self, val):
        self.dados['estoque_atual'] = val + int(self.dados['estoque_atual'])

    def atualizar_dados(self, dados: dict):
        dados['id'] = self.dados['id']
        self.dados = pd.Series(dados)

    def __str__(self) -> str:
        return self.dados['descricao']


class TabelaEstoque(Tabela):

    def __init__(self, obj: QTableWidget, df, db: DataBase):
        super().__init__(obj, df, db)

        self.resize_colum(1, QHeaderView.Stretch)

    def preencher_tabela(self): 
        self.limpar()
 
        nRows, nColumns = self.df.shape
        self.tabela.setRowCount(nRows)
        for row in range(nRows):
            self.tabela.setItem(row, 0, QTableWidgetItem(str(self.df.iloc[row, 1])))
            self.tabela.setItem(row, 1, QTableWidgetItem(str(self.df.iloc[row, 2])))
            self.tabela.setItem(row, 2, QTableWidgetItem(str(self.df.iloc[row, 4])))
            self.tabela.setItem(row, 3, QTableWidgetItem(moeda(self.df.iloc[row, 5])))
            self.tabela.setItem(row, 4, QTableWidgetItem(moeda(self.df.iloc[row, 8])))
            self.tabela.setItem(row, 5, QTableWidgetItem(str(
                self.db.select(f"SELECT nome from fornecedor WHERE id = {self.df.iloc[row, 3]}").iloc[0, 0])))
