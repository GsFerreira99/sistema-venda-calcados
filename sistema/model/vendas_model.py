from sistema.funcoes.model import Model
from sistema.database.banco import DataBase

from sistema.funcoes.tabela import Tabela
from PySide2.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from sistema.funcoes.genericos import moeda

import pandas as pd


class VendasModel(Model):

    def __init__(self, db: DataBase, dados: pd.Series, tabela_sql: str):
        super().__init__(db, dados, tabela_sql)

        self.items_venda = pd.Series()

    def get_items_venda(self):
        return pd.Series(self.items_venda)

    def adicionar_item(self, item: pd.Series):
        self.items_venda = pd.merge(self.items_venda, item)
        print(self.items_venda)



class TabelaVenda(Tabela):

    def __init__(self, obj: QTableWidget, df, db: DataBase):
        super().__init__(obj, df, db)

        self.resize_colum(1, QHeaderView.Stretch)

    def preencher_tabela(self):
        self.limpar()
        print(self.df)
        nrows, ncolumns = self.df.shape
        self.tabela.setRowCount(nrows)
        for row in range(nrows):
            self.tabela.setItem(row, 0, QTableWidgetItem(str(self.df.iloc[row, 1])))
            self.tabela.setItem(row, 1, QTableWidgetItem(str(self.df.iloc[row, 2])))
            self.tabela.setItem(row, 2, QTableWidgetItem(str(self.df.iloc[row, 10])))
            self.tabela.setItem(row, 3, QTableWidgetItem(str(self.df.iloc[row, 11])))
            self.tabela.setItem(row, 4, QTableWidgetItem(str(self.df.iloc[row, 4])))
            self.tabela.setItem(row, 5, QTableWidgetItem(str(self.df.iloc[row, 12])))
            self.tabela.setItem(row, 6, QTableWidgetItem(moeda(self.df.iloc[row, 5])))
            self.tabela.setItem(row, 7, QTableWidgetItem(moeda(self.df.iloc[row, 8])))
            self.tabela.setItem(row, 8, QTableWidgetItem(moeda(self.df.iloc[row, 8])))
            self.tabela.setItem(row, 9, QTableWidgetItem(moeda(self.df.iloc[row, 8])))
            self.tabela.setItem(row, 10, QTableWidgetItem(moeda(self.df.iloc[row, 8])))
            self.tabela.setItem(row, 11, QTableWidgetItem(moeda(self.df.iloc[row, 8])))

