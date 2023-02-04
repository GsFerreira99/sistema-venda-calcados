from sistema.funcoes.model import Model
from sistema.database.banco import DataBase

from sistema.funcoes.tabela import Tabela
from PySide2.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from PySide2.QtCore import Qt
from sistema.funcoes.genericos import moeda, mascara_porcento, data

import pandas as pd


class VendasModel(Model):

    def __init__(self, db: DataBase, dados: pd.Series, tabela_sql: str):
        super().__init__(db, dados, tabela_sql)

        self.items_venda = {}

    def definir_usuario(self, user):
        try:
            self.user = self.dados['vendido_por']
        except:
            self.user = user

    def get_items_venda(self):
        return pd.Series(self.items_venda)

    def remover(self, index):
        try:
            index +=1
            item = self.items_venda.pop(index)
            self.atualizar_index_items()
            self.subtrair_totais(item)
        except:
            pass

    def atualizar_item(self, dados: dict):
        item = self.items_venda[int(dados['id']) + 1]
        item[dados['tipo']] = dados['valor']
        if dados['tipo'] == 'quantidade':
            item['total_bruto'] = item['quantidade'] * item['preco_venda']
            item['total_liquido'] = item['total_bruto'] - (item['total_bruto'] * (item['perc_desconto'] * 0.01))
            self.atualizar_totais()

    def atualizar_totais(self):
        bruto = 0
        desconto = 0
        liquido = 0
        quantidade = 0
        for key, item in self.items_venda.items():
            bruto += int(item['total_bruto'])
            desconto += int(item['valor_desconto'])
            liquido += int(item['total_liquido'])
            quantidade += int(item['quantidade'])
        self.dados['total_bruto'] = bruto
        self.dados['desconto'] = desconto
        self.dados['total_liquido'] = liquido
        self.dados['total_items'] = quantidade

    def deletar(self):
        self.db.atualizar(f"""UPDATE vendas
                            SET ativado = FALSE
                            WHERE codigo = {self.dados['codigo']};""")

    def subtrair_totais(self, dados: pd.Series):
        self.dados['total_bruto'] = self.dados['total_bruto'] - dados['total_bruto']
        self.dados['desconto'] = self.dados['desconto'] - dados['valor_desconto']
        self.dados['total_liquido'] = self.dados['total_liquido'] - dados['total_liquido']
        self.dados['total_items'] = self.dados['total_items'] - dados['quantidade']

    def atualizar_index_items(self):
        new = {}
        for i, j in enumerate(self.items_venda.values()):
            new[i+1] = j
        self.items_venda = new
    def carregar_items_venda(self):
        self.items_venda = self.db.select(f"SELECT * FROM item_venda WHERE venda = {self.dados['id']}")

    def nome_cliente(self):
        self.dados['cliente'] = self.db.select(
            f"SELECT nome FROM cliente WHERE id = {self.dados['cliente']}").iloc[0, 0]

    def dados_item(self, item: pd.Series):
        return [
            int(self.db.select('SELECT MAX(id) as id FROM vendas').iloc[0, 0]),
            int(self.db.select(f"SELECT id FROM estoque WHERE descricao = '{item['descricao']}'").iloc[0, 0]),
            item['preco_venda'],
            item['quantidade'],
            item['tamanho'],
            item['cor'],
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
                    tamanho,
                    cor,
                    percent_desconto,
                    valor_desconto,
                    total_bruto,
                    total_liquido)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, item)

    def adicionar_item(self, item: pd.Series):
        self.items_venda[len(self.items_venda) + 1] = item

    def salvar(self, sql: str):
        """Implementar INSERT ex.: INSERT INTO cliente (criado_em, nome, celular) VALUES (%s, %s, %s)"""
        dados = self.dados.tolist()
        dados.pop(0)
        dados.append(int(self.user[0]))
        insert = self.db.inserir(sql, dados)
        return insert

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
            self.tabela.setItem(row, 0, QTableWidgetItem(str(
                self.db.select(f"SELECT cod_barras FROM estoque WHERE descricao = '{item['descricao']}'").iloc[0, 0]
            )))
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

            self.tabela.item(row, 0).setFlags(Qt.ItemIsSelectable)
            self.tabela.item(row, 1).setFlags(Qt.ItemIsSelectable)
            self.tabela.item(row, 2).setFlags(Qt.ItemIsSelectable)
            self.tabela.item(row, 6).setFlags(Qt.ItemIsSelectable)
            self.tabela.item(row, 7).setFlags(Qt.ItemIsSelectable)
            self.tabela.item(row, 8).setFlags(Qt.ItemIsSelectable)
            self.tabela.item(row, 9).setFlags(Qt.ItemIsSelectable)
            self.tabela.item(row, 10).setFlags(Qt.ItemIsSelectable)

        self.resize()


class TabelaVendaEdit(TabelaVenda):

    def __init__(self, obj: QTableWidget, df, db: DataBase):
        super().__init__(obj, df, db)

    def preencher_tabela(self):
        self.limpar()

        nrows = len(self.df)
        self.tabela.setRowCount(nrows)
        for row in range(nrows):
            self.tabela.setItem(row, 0, QTableWidgetItem(str(
                self.db.select(f"SELECT cod_barras FROM estoque WHERE id = {self.df.iloc[row, 2]}").iloc[0, 0]
            )))
            self.tabela.setItem(row, 1, QTableWidgetItem(
                self.db.select(f"SELECT descricao FROM estoque WHERE id = {self.df.iloc[row, 2]}").iloc[0, 0]
            ))
            #self.tabela.setItem(row, 2, QTableWidgetItem(str(self.df.iloc[row, 2])))
            self.tabela.setItem(row, 2, QTableWidgetItem(str(
                self.db.select(f"SELECT unidade FROM estoque WHERE id = {self.df.iloc[row, 2]}").iloc[0, 0]
            )))
            self.tabela.setItem(row, 3, QTableWidgetItem(str(self.df.iloc[row, 4])))
            self.tabela.setItem(row, 4, QTableWidgetItem(str(self.df.iloc[row, 5])))
            self.tabela.setItem(row, 5, QTableWidgetItem(str(self.df.iloc[row, 6])))
            self.tabela.setItem(row, 6, QTableWidgetItem(moeda(self.df.iloc[row, 3])))
            self.tabela.setItem(row, 7, QTableWidgetItem(moeda(self.df.iloc[row, 9])))
            self.tabela.setItem(row, 8, QTableWidgetItem(mascara_porcento(self.df.iloc[row, 7])))
            self.tabela.setItem(row, 9, QTableWidgetItem(moeda(self.df.iloc[row, 8])))
            self.tabela.setItem(row, 10, QTableWidgetItem(moeda(self.df.iloc[row, 10])))
        self.resize()


class TabelaVendas(Tabela):

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

    def preencher_tabela(self):
        self.limpar()

        nrows = len(self.df)
        self.tabela.setRowCount(nrows)
        for row in range(nrows):
            self.tabela.setItem(row, 0, QTableWidgetItem(str(self.df.iloc[row, 1])))
            self.tabela.setItem(row, 1, QTableWidgetItem(self.df.iloc[row, 2].strftime("%d/%m/%Y")))
            self.tabela.setItem(row, 2, QTableWidgetItem(str(
                    self.db.select(f"SELECT nome from cliente WHERE id = {self.df.iloc[row, 3]}").iloc[0, 0])))
            self.tabela.setItem(row, 3, QTableWidgetItem(moeda(self.df.iloc[row, 6])))
            self.tabela.setItem(row, 4, QTableWidgetItem(str(self.df.iloc[row, 7])))
            vendedor = self.db.select(f"SELECT nome, sobrenome from usuarios WHERE id = {self.df.iloc[row, 10]}")
            self.tabela.setItem(row, 5, QTableWidgetItem(f"{vendedor.iloc[0, 0]} {vendedor.iloc[0, 1]}"))

        self.resize()
