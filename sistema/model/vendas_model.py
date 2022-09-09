from sistema.funcoes.model import Model
from sistema.database.banco import DataBase

from sistema.funcoes.tabela import Tabela
from PySide2.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from sistema.funcoes.genericos import moeda, mascara_porcento

import pandas as pd


class VendasModel(Model):

    def __init__(self, db: DataBase, dados: pd.Series, tabela_sql: str):
        super().__init__(db, dados, tabela_sql)

        self.items_venda = {}

    def get_items_venda(self):
        return pd.Series(self.items_venda)

    def dados_item(self, item: pd.Series):
        return [
            int(self.dados['id']),
            int(self.db.select(f"SELECT id FROM estoque WHERE descricao = '{item['descricao']}'").iloc[0, 0]),
            item['preco_venda'],
            item['quantidade'],
            item['perc_desconto'],
            item['valor_desconto'],
            item['total_bruto'],
            item['total_liquido']
        ]

    def salvar_items(self):
        for item in self.items_venda.values():
            item = self.dados_item(item)
            self.db.inserir("""
                INSERT INTO item_venda (
                    venda,
                    produto,
                    preco,
                    quantidade,
                    percent_desconto,
                    valor_desconto,
                    total_bruto,
                    total_liquido)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """, item)

    def adicionar_item(self, item: pd.Series):
        self.items_venda[len(self.items_venda) + 1] = item


class TabelaVenda(Tabela):

    def __init__(self, obj: QTableWidget, df, db: DataBase):
        super().__init__(obj, df, db)

        self.resize()

    def resize(self):
        self.resize_colum(0, QHeaderView.Stretch)
        self.resize_colum(1, QHeaderView.Stretch)
        self.resize_colum(2, QHeaderView.Stretch)
        self.resize_colum(3, QHeaderView.Stretch)
        self.resize_colum(4, QHeaderView.Stretch)
        self.resize_colum(5, QHeaderView.Stretch)
        self.resize_colum(6, QHeaderView.Stretch)
        self.resize_colum(7, QHeaderView.Stretch)
        self.resize_colum(8, QHeaderView.Stretch)
        self.resize_colum(9, QHeaderView.Stretch)
        self.resize_colum(10, QHeaderView.Stretch)

    def preencher_tabela(self):
        self.limpar()

        nrows = len(self.df)
        self.tabela.setRowCount(nrows)
        for row in range(nrows):
            item = self.df[row + 1]
            self.tabela.setItem(row, 0, QTableWidgetItem(str(item['codigo'])))
            self.tabela.setItem(row, 1, QTableWidgetItem(str(item['descricao'])))
            self.tabela.setItem(row, 2, QTableWidgetItem(str(item['uni'])))
            self.tabela.setItem(row, 3, QTableWidgetItem(str(item['quantidade'])))
            self.tabela.setItem(row, 4, QTableWidgetItem(str(item['tamanho'])))
            self.tabela.setItem(row, 5, QTableWidgetItem(str(item['cor'])))
            self.tabela.setItem(row, 6, QTableWidgetItem(moeda(item['preco_venda'])))
            self.tabela.setItem(row, 7, QTableWidgetItem(moeda(item['total_bruto'])))
            self.tabela.setItem(row, 8, QTableWidgetItem(mascara_porcento(item['perc_desconto'])))
            self.tabela.setItem(row, 9, QTableWidgetItem(moeda(item['valor_desconto'])))
            self.tabela.setItem(row, 10, QTableWidgetItem(moeda(item['total_liquido'])))
        self.resize()
