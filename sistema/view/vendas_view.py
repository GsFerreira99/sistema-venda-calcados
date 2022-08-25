from sistema.funcoes.view import View
from interface.telas.vendas import Ui_Vendas
from PySide2.QtWidgets import QWidget

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

        self.config()

    def config(self):
        self.input_nrVenda.setReadOnly(True)

    def atualizar_tela(self, dados):
        self.config()
        self.preencher_data(dados["data_venda"])
        self.preencher_nr_venda(dados["id"])

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
    def campo_cor(self):
        return self.input_cor.currentText()

    @property
    def campo_quantidade(self):
        return self.input_quantidade.text()

    @property
    def campo_preco(self):
        return self.input_preco.text()

    @property
    def campo_tamanho(self):
        campo = self.input_tamanho.currentText()
        if campo != '':
            return int(self.input_tamanho.currentText())
        else:
            return 0
