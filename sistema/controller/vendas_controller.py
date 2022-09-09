import datetime

import pandas as pd

from sistema.funcoes.poupup import confirma, mensagem
from PySide2.QtWidgets import QMessageBox
from sistema.database.banco import DataBase
from sistema.funcoes.controller import Controller
from sistema.view.vendas_view import VendasView
from sistema.model.vendas_model import VendasModel, TabelaVenda
from sistema.funcoes.genericos import preencher_combo_box, converter_string_int, mascara_porcento, \
    limpar_dinheiro, limpar_porcento

from sistema.funcoes.genericos import moeda


class VendasController(Controller):

    view: VendasView
    model: VendasModel

    def __init__(self, db: DataBase, view):
        super().__init__(db, view)

        self.view.btn_novo.clicked.connect(lambda: self.criar_venda())
        self.view.btn_add.clicked.connect(lambda: self.adicionar_item())

        self.view.btn_salvar.clicked.connect(lambda: self.salvar_venda())

        self.view.input_descricao.currentIndexChanged.connect(lambda: self.cb_preco())
        self.view.input_percDesc.editingFinished.connect(lambda: self.desconto())
        self.view.input_quantidade.editingFinished.connect(lambda: self.definir_total())
        self.view.input_totalPago.editingFinished.connect(lambda: self.mascara_total_pago())

    def criar_venda(self):
        dados = self.criar_df()
        self.model = VendasModel(self.db, dados, 'vendas')
        self.atualizar_tela()
        self.view.atualizar_tela(self.model.dados)
        self.cb_clientes()
        self.cb_produtos()

    def cb_clientes(self):
        clientes = self.db.select("SELECT DISTINCT nome FROM cliente")['nome'].values.tolist()
        preencher_combo_box(clientes, self.view.input_cliente)

    def cb_produtos(self):
        produtos = self.db.select("SELECT DISTINCT descricao FROM estoque")['descricao'].values.tolist()
        preencher_combo_box(produtos, self.view.input_descricao)

    def cb_preco(self):
        preco = self.db.select(f"""SELECT preco_venda FROM estoque WHERE descricao = '{self.view.campo_produto}'""")
        if preco.empty is True:
            self.view.preencher_preco(moeda(0.0))
        else:
            self.view.preencher_preco(moeda(preco.iloc[0, 0]))
        self.definir_desconto()
        self.definir_total()

    def salvar_venda(self):
        if self.view.input_cliente.currentText() != '':
            self.model.dados['cliente'] = int(self.db.select(
                f"SELECT id FROM cliente WHERE nome = '{self.view.input_cliente.currentText()}'").iloc[0, 0])
            if confirma('Finalizar e salvar venda?', QMessageBox.Information, 'Confirmação') is True:
                self.model.salvar("""
                INSERT INTO vendas (
                    data_venda,
                    cliente,
                    total_bruto,
                    desconto,
                    total_liquido,
                    total_items,
                    total_pago,
                    troco)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """)
                self.model.salvar_items()
                mensagem('Venda cadastrada com sucesso.', QMessageBox.Information, 'Sucesso')
                self.view.navegacao(1)
        else:
            mensagem('Selecione um Cliente.', QMessageBox.Information, 'Erro')

    def troco(self):
        troco = limpar_dinheiro(self.view.input_totalPago.text()) - self.model.dados['total_liquido']
        self.view.input_troco.setText(moeda(troco))

    def mascara_total_pago(self):
        self.view.input_totalPago.setText(moeda(self.view.input_totalPago.text()))
        self.troco()

    def atualizar_tela(self):
        self.definir_qnt()
        self.definir_desconto()
        self.definir_totais()

    def definir_total(self):
        total = (limpar_dinheiro(self.view.input_preco.text()) * converter_string_int(self.view.input_quantidade.text())) - \
                limpar_dinheiro(self.view.input_valDesc.text())
        self.view.input_total.setText(moeda(total))

    def desconto(self):
        val = (limpar_porcento(self.view.input_percDesc.text()) * 0.01) * (converter_string_int(
            self.view.campo_quantidade) * limpar_dinheiro(self.view.campo_preco))
        self.view.input_percDesc.setText(mascara_porcento(self.view.input_percDesc.text()))
        self.view.input_valDesc.setText(moeda(val))
        self.definir_total()

    def definir_desconto(self):
        self.view.input_percDesc.setText(mascara_porcento(0))
        self.view.input_valDesc.setText(moeda(0))

    def definir_qnt(self):
        self.view.input_quantidade.setText('1')

    def limpar(self):
        self.view.input_cor.setText('')
        self.view.input_tamanho.setText('')

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

    def inserir_valores_totais(self, dados: pd.Series):
        self.model.dados['total_bruto'] = self.model.dados['total_bruto'] + dados['total_bruto']
        self.model.dados['desconto'] = self.model.dados['desconto'] + dados['valor_desconto']
        self.model.dados['total_liquido'] = self.model.dados['total_liquido'] + dados['total_liquido']
        self.model.dados['total_items'] = self.model.dados['total_items'] + dados['quantidade']

    def adicionar_item(self):
        item = self.criar_df_item()
        if item is not False:
            self.model.adicionar_item(item)
            self.inserir_valores_totais(item)
            self.table = TabelaVenda(self.view.table, self.model.get_items_venda(), self.db)
            self.table.preencher_tabela()
            self.view.input_descricao.setCurrentIndex(0)
            self.definir_qnt()
            self.definir_totais()
            self.limpar()
        else:
            mensagem('Preencha todos os campos!', QMessageBox.Information, 'Erro')

    def criar_df_item(self):
        try:
            dados = self.db.select(f"""SELECT * FROM estoque WHERE descricao = '{self.view.campo_produto}'""")
            if self.view.campo_tamanho != '' and self.view.campo_cor != '':
                return pd.Series({
                    'codigo': dados['cod_barras'].values[0],
                    'descricao': dados['descricao'].values[0],
                    'uni': dados['unidade'].values[0],
                    'quantidade': converter_string_int(self.view.campo_quantidade),
                    'tamanho': self.view.campo_tamanho,
                    'cor': self.view.campo_cor,
                    'preco_venda': limpar_dinheiro(self.view.campo_preco),
                    'perc_desconto': limpar_porcento(self.view.campo_perc_desconto),
                    'valor_desconto': limpar_dinheiro(self.view.campo_val_desconto),
                    'total_bruto': converter_string_int(self.view.campo_quantidade) * limpar_dinheiro(
                        self.view.campo_preco),
                    'total_liquido': limpar_dinheiro(self.view.campo_total)
                })
            else:
                return False
        except IndexError:
            return False


    def valor_desconto(self):
        pass

    def definir_totais(self):
        self.view.input_totalBruto.setText(moeda(self.model.dados['total_bruto']))
        self.view.input_desconto.setText(moeda(self.model.dados['desconto']))
        self.view.input_totalLiquido.setText(moeda(self.model.dados['total_liquido']))
        self.view.input_totalItem.setText(f"{self.model.dados['total_items']}")
        self.view.input_totalPago.setText(moeda(0))
        self.view.input_troco.setText(moeda(0))

    def nr_venda(self):
        nr = self.db.select('SELECT * FROM vendas ORDER BY ID DESC LIMIT 1')
        if nr.empty is True:
            nr = 1
        else:
            nr = nr.iloc[0, 0] + 1
        return nr
