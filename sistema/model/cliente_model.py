from sistema.funcoes.genericos import celular, cpf_cnpj
from sistema.funcoes.tabela import Tabela
from sistema.database.banco import DataBase
from PySide2.QtWidgets import QTableWidgetItem, QHeaderView, QTableWidget

import pandas as pd


class ClienteModel:

    dados: pd.Series

    def __init__(self, db, dados: pd.Series):
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
        insert = self.__db.deletar(f"DELETE FROM cliente WHERE id = {int(self.dados['id'])}")
        return insert

    def editar(self):
        update = self.__db.atualizar(
            f"""
            UPDATE cliente
            SET
                nome = '{self.dados['nome']}',
                celular = '{self.dados['celular']}',
                telefone = '{self.dados['telefone']}',
                cpf_cnpj = '{self.dados['cpf_cnpj']}',
                inscricao_estadual = '{self.dados['inscricao_estadual']}',
                nascimento = '{self.dados['nascimento']}',
                email = '{self.dados['email']}',
                cep = '{self.dados['cep']}',
                endereco = '{self.dados['endereco']}',
                complemento = '{self.dados['complemento']}',
                bairro = '{self.dados['bairro']}',
                cidade = '{self.dados['cidade']}',
                uf = '{self.dados['uf']}',
                observacao = '{self.dados['observacao']}'
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


class TabelaCliente(Tabela):

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
            self.tabela.setItem(row, 1, QTableWidgetItem(str(self.df.iloc[row, 2])))
            self.tabela.setItem(row, 2, QTableWidgetItem(celular(self.df.iloc[row, 3])))
            self.tabela.setItem(row, 3, QTableWidgetItem(cpf_cnpj(self.df.iloc[row, 5])))
            self.tabela.setItem(row, 4, QTableWidgetItem(str(self.df.iloc[row, 6])))
            self.tabela.setItem(row, 5, QTableWidgetItem(str(self.df.iloc[row, 8])))
