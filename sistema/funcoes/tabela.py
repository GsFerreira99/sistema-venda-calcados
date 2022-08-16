from PySide2.QtWidgets import QTableWidgetItem


class Tabela:

    def __init__(self, obj:object, df, db):
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
    
        nRows, nColumns = self.df.shape
        self.tabela.setRowCount(nRows)
        for row in range(nRows):
            for column in range(nColumns):
                self.tabela.setItem(row, column, QTableWidgetItem(str(self.df.iloc[row, column])))

    def limpar(self):
        for i in range(self.tabela.rowCount()):
             self.tabela.removeRow(i)

    def atualizar_df(self, df):
        self.df = df

    
    

    