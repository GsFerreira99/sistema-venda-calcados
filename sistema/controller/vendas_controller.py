import datetime

import pandas as pd

from sistema.database.banco import DataBase
from sistema.funcoes.controller import Controller
from sistema.view.vendas_view import VendasView
from sistema.model.vendas_model import VendasModel, TabelaVenda
from sistema.funcoes.genericos import preencher_combo_box, converter_string_int, converter_string_float

from sistema.funcoes.genericos import moeda

class VendasController(Controller):

    view: VendasView
    model: VendasModel

    def __init__(self, db: DataBase, view):
        super().__init__(db, view)

        self.view.btn_novo.clicked.connect(lambda: self.criar_venda())
        self.view.btn_add.clicked.connect(lambda: self.adicionar_item())

        self.view.input_descricao.currentIndexChanged.connect(lambda: self.cb_cor())
        self.view.input_cor.currentIndexChanged.connect(lambda: self.cb_tamanho())
        self.view.input_tamanho.currentIndexChanged.connect(lambda: self.cb_preco())

    def criar_venda(self):
        dados = self.criar_df()
        self.model = VendasModel(self.db, dados, 'vendas')
        self.view.atualizar_tela(self.model.dados)
        self.cb_clientes()
        self.cb_produtos()

    def cb_clientes(self):
        clientes = self.db.select("SELECT DISTINCT nome FROM cliente")['nome'].values.tolist()
        preencher_combo_box(clientes, self.view.input_cliente)

    def cb_produtos(self):
        produtos = self.db.select("SELECT DISTINCT descricao FROM estoque")['descricao'].values.tolist()
        preencher_combo_box(produtos, self.view.input_descricao)

    def cb_cor(self):
        cores = self.db.select(f"SELECT DISTINCT cor FROM estoque WHERE descricao = '{self.view.campo_produto}'"
                               )['cor'].values.tolist()
        preencher_combo_box(cores, self.view.input_cor)

    def cb_tamanho(self):
        tamanhos = self.db.select(f"""SELECT DISTINCT tamanho FROM estoque WHERE descricao = '{self.view.campo_produto}'
         AND cor = '{self.view.campo_cor}'""")['tamanho'].values.tolist()
        tamanhos = list(map(lambda x: str(x), tamanhos))
        preencher_combo_box(tamanhos, self.view.input_tamanho)

    def cb_preco(self):
        preco = self.db.select(f"""SELECT preco_venda FROM estoque WHERE descricao = '{self.view.campo_produto}'
         AND cor = '{self.view.campo_cor}' AND tamanho = {self.view.campo_tamanho}""")
        if preco.empty is True:
            self.view.preencher_preco(moeda(0.0))
        else:
            self.view.preencher_preco(moeda(preco.iloc[0, 0]))

    def criar_df(self):
        return pd.Series({
            'id': self.nr_venda(),
            'data_venda': datetime.datetime.now(),
            'cliente': 0,
            'total_bruto': 0.0,
            'desconto': 0.0,
            'total_liquido': 0.0,
            'total_items': 0,
            'total_pago': 0.0,
            'troco': 0.0,
        })

    def adicionar_item(self):
        self.model.adicionar_item(self.criar_df_item())
        self.table = TabelaVenda(self.view.table, self.model.get_items_venda(), self.db)
        self.table.preencher_tabela()

    def criar_df_item(self):
        dados = self.db.select(f"""SELECT * FROM estoque WHERE descricao = '{self.view.campo_produto}'
         AND cor = '{self.view.campo_cor}' AND tamanho = {self.view.campo_tamanho}""")
        return pd.Series({
            'codigo': dados['id'],
            'descricao': dados['descricao'],
            'uni': dados['unidade'],
            'quantidade': converter_string_int(self.view.campo_quantidade),
            'tamanho': self.view.campo_tamanho,
            'cor': self.view.campo_cor,
            'preco_venda': self.view.campo_preco,
            'perc_desconto': 0.0,
            'valor_desconto': 0.0,
            'total_bruto': (converter_string_int(self.view.campo_quantidade) *
                            converter_string_float(self.view.campo_preco)),
            'total_liquido': (converter_string_int(self.view.campo_quantidade) *
                            converter_string_float(self.view.campo_preco))
        })

    def nr_venda(self):
        nr = self.db.select('SELECT * FROM vendas ORDER BY ID DESC LIMIT 1')
        if nr.empty is True:
            nr = 1
        else:
            nr = nr.iloc[0, 0] + 1
        return nr
