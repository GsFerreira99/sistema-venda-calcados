from sistema.database.banco import DataBase

import pandas as pd


class Model:

    def __init__(self, db: DataBase, dados: pd.Series, tabela_sql: str):
        self.__db = db
        self.dados = dados
        self.tabela_sql = tabela_sql

    @property
    def db(self):
        return self.__db

    def salvar(self, sql: str):
        """Implementar INSERT ex.: INSERT INTO cliente (criado_em, nome, celular) VALUES (%s, %s, %s)"""
        dados = self.dados.tolist()
        dados.pop(0)
        insert = self.__db.inserir(sql, dados)
        return insert

    def deletar(self, sql: str):
        """Implementar DELETE ex.: DELETE FROM cliente WHERE id = {int(self.dados['id'])}"""
        insert = self.__db.deletar(sql)
        return insert

    def editar(self, sql: str):
        """Implementar UPDATE ex.: UPDATE cliente SET nome = '',
        celular = '', telefone = '',
        WHERE id = 0"""
        update = self.__db.atualizar(sql)
        return update

    def atualizar_dados(self, dados: dict):
        """Informar dict para criação de DataFrame Pandas"""
        dados['id'] = self.dados['id']
        self.dados = pd.Series(dados)

    def __getitem__(self, item):
        return self.dados[item]

    def __setitem__(self, key, value):
        self.dados[key] = value

    def __str__(self) -> str:
        return self.dados['nome']
