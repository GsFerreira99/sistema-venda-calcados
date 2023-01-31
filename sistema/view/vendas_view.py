from sistema.funcoes.view import View
from interface.telas.vendas import Ui_Vendas
from PySide2.QtWidgets import QWidget
import datetime

from sistema.funcoes.genericos import data

class VendasView(Ui_Vendas, QWidget, View):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.botoes = {
            1: self.btn_consulta,
            2: self.btn_novo
        }

        self.nav_widget = self.stackedWidget

        self.radio_periodo.toggled.connect(lambda: self.busca_periodo())

    def busca_periodo(self):
        if self.frame_periodo.width() == 0:
            self.definir_data()
            self.frame_periodo.setMaximumWidth(300)
        else:
            self.frame_periodo.setMaximumWidth(0)



    def definir_data(self):
        hoje = datetime.date.today()
        self.input_data_ini.setDate(hoje)
        self.input_data_fim.setDate(hoje)

    def config(self):
        self.input_nrVenda.setReadOnly(True)

    def atualizar_tela(self, dados):
        self.preencher_data(dados["data_venda"])
        self.preencher_nr_venda(dados["codigo"])

    def preencher_nr_venda(self, val):
        self.input_nrVenda.setText(f'{val}')

    def preencher_data(self, date):
        self.input_data.setDate(data(date))

    def preencher_preco(self, val):
        self.input_preco.setText(val)

    @property
    def campo_produto(self):
        return self.input_descricao.currentText()

    @property
    def campo_quantidade(self):
        return self.input_quantidade.text()

    @property
    def campo_perc_desconto(self):
        return self.input_percDesc.text()

    @property
    def campo_val_desconto(self):
        return self.input_valDesc.text()

    @property
    def campo_preco(self):
        return self.input_preco.text()

    @property
    def campo_cor(self):
        return self.input_cor.text()

    @property
    def campo_tamanho(self):
        return self.input_tamanho.text()

    @property
    def campo_total(self):
        return self.input_total.text()

    def linha_selecionada(self):
        return self.table_vendas.currentRow()

    def limpar(self):
        self.input_nrVenda.setText("")
        self.input_cliente.setText("")

        self.input_totalBruto.setText("")
        self.input_desconto.setText("")
        self.input_totalLiquido.setText("")
        self.input_totalItem.setText("")
        self.input_totalPago.setText("")
        self.input_troco.setText("")
