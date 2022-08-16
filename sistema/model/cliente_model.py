from ..funcoes.genericos import celular, cpf_cnpj
from sistema.funcoes.tabela import Tabela
from PySide2.QtWidgets import QTableWidgetItem, QHeaderView

class ClienteModel:

    def __init__(self, db, dados:object) -> None:
        self.__db = db
        self.dados = dados

    def salvar(self):
        insert = self.__db.inserir(
            """
            INSERT INTO cliente (
                criado_em,
                nome,
                celular,
                telefone,
                cpf_cnpj,
                inscricao_estadual,
                nascimento,
                email,
                cep,
                endereco,
                complemento,
                bairro,
                cidade,
                uf,
                observacao)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, self.dados.tolist())
        return insert

    def deletar(self):
        insert = self.__db.deletar(f"DELETE FROM cliente WHERE id = {int(self.dados['id'])}" )
        return insert

    def editar(self):
        pass
    
    def adicionarEstoque(self, valor):
        pass

    def dadosTabela(self):
        pass

    def __str__(self) -> str:
        return self.dados['nome']

class TabelaCliente(Tabela):

    def __init__(self, obj: object, df, db):
        super().__init__(obj, df, db)

        self.resize_colum(1, QHeaderView.Stretch)

    def preencher_tabela(self): 
        self.limpar() 

        nRows, nColumns = self.df.shape
        self.tabela.setRowCount(nRows)
        for row in range(nRows):
            self.tabela.setItem(row, 0, QTableWidgetItem(str(self.df.iloc[row, 0])))
            self.tabela.setItem(row, 1, QTableWidgetItem(str(self.df.iloc[row, 2])))
            self.tabela.setItem(row, 2, QTableWidgetItem(celular(self.df.iloc[row, 3])))
            self.tabela.setItem(row, 3, QTableWidgetItem(cpf_cnpj(self.df.iloc[row, 5])))
            self.tabela.setItem(row, 4, QTableWidgetItem(str(self.df.iloc[row, 6])))
            self.tabela.setItem(row, 5, QTableWidgetItem(str(self.df.iloc[row, 8])))