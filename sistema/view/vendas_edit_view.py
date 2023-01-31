from PySide2.QtWidgets import QDialog
from sistema.model.vendas_model import VendasModel
from interface.telas.vendas_consulta import Ui_VendasEdit
from sistema.view.vendas_view import VendasView
from sistema.funcoes.genericos import data, moeda


class VendasEditView(Ui_VendasEdit, QDialog, VendasView):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setModal(True)

    def preencher_campos(self, dados, db):
        self.input_nrVenda_2.setText(str(dados['codigo']))
        self.input_data_2.setDate(data(dados['data_venda']))
        self.input_cliente.setText(str(dados['cliente']))
        vendedor = db.select(f"SELECT nome, sobrenome from usuarios WHERE id = {dados['vendido_por']}")
        self.input_vendedor.setText(f"{vendedor.iloc[0, 0]} {vendedor.iloc[0, 1]}")

        self.input_totalBruto.setText(moeda(dados['total_bruto']))
        self.input_desconto.setText(moeda(dados['desconto']))
        self.input_totalLiquido.setText(moeda(dados['total_liquido']))
        self.input_totalItem.setText(str(dados['total_items']))
        self.input_totalPago.setText(moeda(dados['total_pago']))
        self.input_troco.setText(moeda(dados['troco']))


    def limpar(self):
        self.input_nrVenda_2.setText("")
        self.input_cliente.setText("")

        self.input_totalBruto.setText("")
        self.input_desconto.setText("")
        self.input_totalLiquido.setText("")
        self.input_totalItem.setText("")
        self.input_totalPago.setText("")
        self.input_troco.setText("")



