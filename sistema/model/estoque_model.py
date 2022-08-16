from sistema.funcoes.genericos import moeda
from sistema.funcoes.tabela import Tabela
from PySide2.QtWidgets import QTableWidgetItem

class EstoqueModel:

    def __init__(self, db, dados:object) -> None:
        self.__db = db
        self.__dados = dados

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
                """, self.__dados.tolist())
        return insert

    def deletar(self):
        pass

    def editar(self):
        pass
    
    def adicionarEstoque(self, valor):
        pass

    def dadosTabela(self):
        pass

    def __str__(self) -> str:
        return self.__dados['descricao']

class TabelaEstoque(Tabela):

    def __init__(self, obj: object, df, db):
        super().__init__(obj, df, db)

    def preencher_tabela(self):
        self.limpar()

        nRows, nColumns = self.df.shape
        self.tabela.setRowCount(nRows)
        for row in range(nRows):
            self.tabela.setItem(row, 0, QTableWidgetItem(str(self.df.iloc[row, 1])))
            self.tabela.setItem(row, 1, QTableWidgetItem(str(self.df.iloc[row, 2])))
            self.tabela.setItem(row, 2, QTableWidgetItem(str(self.df.iloc[row, 4])))
            self.tabela.setItem(row, 3, QTableWidgetItem(str(self.df.iloc[row, 12])))
            self.tabela.setItem(row, 4, QTableWidgetItem(moeda(self.df.iloc[row, 5])))
            self.tabela.setItem(row, 5, QTableWidgetItem(moeda(self.df.iloc[row, 8])))
            self.tabela.setItem(row, 6, QTableWidgetItem(str(self.db.select(f"SELECT nome from fornecedor WHERE id = {self.df.iloc[row, 3]}").iloc[0,0])))



    
    

    