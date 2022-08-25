from PySide2.QtWidgets import QTableWidgetItem, QTableWidget
from sistema.database.banco import DataBase


class Tabela:

    def __init__(self, obj: QTableWidget, df, db: DataBase):
        self.df = df
        self.tabela = obj
        self.db = db

    def df_table(self):
        pass

    def retorna_objeto(self, index):
        return self.df.iloc[index]

    def resize_colum(self, column, tipo):
        """colum=(numero da coluna), tipo=(QHeaderView.ResizeToContents, QHeaderView.Stretch)"""
        header = self.tabela.horizontalHeader()       
        header.setSectionResizeMode(column, tipo)
    
    def preencher_tabela(self):
        self.limpar()
    
        nrows, ncolumns = self.df.shape
        self.tabela.setRowCount(nrows)
        for row in range(nrows):
            for column in range(ncolumns):
                self.tabela.setItem(row, column, QTableWidgetItem(str(self.df.iloc[row, column])))

    def limpar(self):
        for i in range(self.tabela.rowCount()):
            self.tabela.removeRow(i)

    def atualizar_df(self, df):
        self.df = df
