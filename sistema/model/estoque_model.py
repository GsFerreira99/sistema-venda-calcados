from sistema.funcoes.genericos import moeda
from sistema.funcoes.tabela import Tabela
from PySide2.QtWidgets import QTableWidgetItem, QHeaderView

import pandas as pd

class EstoqueModel:

    def __init__(self, db, dados:object) -> None:
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
                cor,
                tamanho,
                estoque_atual,
                observacao)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, self.dados.tolist())
        return insert

    def deletar(self):
        insert = self.__db.deletar(f"DELETE FROM estoque WHERE id = {int(self.dados['id'])}" )
        return insert

    def __getitem__(self, item):
        return self.dados[item]

    def editar(self):
        update = self.__db.atualizar(
            f"""
            UPDATE estoque
            SET
                cod_barras = '{self.dados['cod_barras']}',
                descricao = '{self.dados['descricao']}',
                fornecedorId = {self.dados['fornecedorId']},
                unidade = '{self.dados['unidade']}',
                preco_compra = {self.dados['preco_compra']},
                margem = {self.dados['margem']},
                lucro = {self.dados['lucro']},
                preco_venda = {self.dados['preco_venda']},
                preco_atacado = {self.dados['preco_atacado']},
                cor = '{self.dados['cor']}',
                tamanho = {self.dados['tamanho']},
                estoque_atual = {self.dados['estoque_atual']},
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

    def atualizar_dados(self, dados:dict):
        dados['id'] = self.dados['id']
        self.dados = pd.Series(dados)

    def __str__(self) -> str:
        return self.dados['descricao']

class TabelaEstoque(Tabela):

    def __init__(self, obj: object, df, db):
        super().__init__(obj, df, db)

        self.resize_colum(1, QHeaderView.Stretch)

    def preencher_tabela(self): 
        self.limpar()
 
        nRows, nColumns = self.df.shape
        self.tabela.setRowCount(nRows)
        for row in range(nRows):
            self.tabela.setItem(row, 0, QTableWidgetItem(str(self.df.iloc[row, 1])))
            self.tabela.setItem(row, 1, QTableWidgetItem(str(self.df.iloc[row, 2])))
            self.tabela.setItem(row, 2, QTableWidgetItem(str(self.df.iloc[row, 10])))
            self.tabela.setItem(row, 3, QTableWidgetItem(str(self.df.iloc[row, 11])))
            self.tabela.setItem(row, 4, QTableWidgetItem(str(self.df.iloc[row, 4])))
            self.tabela.setItem(row, 5, QTableWidgetItem(str(self.df.iloc[row, 12])))
            self.tabela.setItem(row, 6, QTableWidgetItem(moeda(self.df.iloc[row, 5])))
            self.tabela.setItem(row, 7, QTableWidgetItem(moeda(self.df.iloc[row, 8])))
            self.tabela.setItem(row, 8, QTableWidgetItem(str(self.db.select(f"SELECT nome from fornecedor WHERE id = {self.df.iloc[row, 3]}").iloc[0,0])))
