#PySide2
from PySide2.QtWidgets import QDialog

from sistema.funcoes.genericos import converter_string_int, limpar_dinheiro, limpar_porcento, moeda, mascara_porcento

#Telas
from interface.telas.estoque_edicao import Ui_EstoqueEdit

class EstoqueEditView(Ui_EstoqueEdit, QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setModal(True)

        self.input_precoVenda.editingFinished.connect(lambda: self.calculo_margem())

        self.input_precoCompra.editingFinished.connect(lambda: self.input_precoCompra.setText(moeda(self.input_precoCompra.text())))
        self.input_precoVenda.editingFinished.connect(lambda: self.input_precoVenda.setText(moeda(self.input_precoVenda.text())))
        self.input_lucro.editingFinished.connect(lambda: self.input_lucro.setText(moeda(self.input_lucro.text())))
        self.inputMargem.editingFinished.connect(lambda: self.inputMargem.setText(mascara_porcento(self.inputMargem.text())))

    def preencher_fornecedor(self, dados):
        self.input_fornecedor.clear()
        self.input_fornecedor.addItem('')
        self.input_fornecedor.addItems(dados)

    def limpar(self, cores, fornecedor):
        self.input_codBarras.setText('')
        self.input_descricao.setText('')
        self.preencher_fornecedor(fornecedor)
        self.input_unidade.setCurrentIndex(0)
        self.input_precoCompra.setText('')
        self.inputMargem.setText('')
        self.input_lucro.setText('')
        self.input_precoVenda.setText('')
        self.input_observacao.setText('')

    def calculo_margem(self):
        compra = limpar_dinheiro(self.input_precoCompra.text())
        venda = limpar_dinheiro(self.input_precoVenda.text())
        valLucro = venda - compra
        percLucro = (valLucro * 100) / venda

        self.input_lucro.setText(moeda(valLucro))
        self.inputMargem.setText(mascara_porcento(percLucro))

    def preencher_campos(self, dados):
        self.input_codBarras.setText(dados['cod_barras'])
        self.input_descricao.setText(dados['descricao'])
        self.input_fornecedor.setCurrentText(str(dados['fornecedorId']))
        self.input_unidade.setCurrentText(dados['unidade'])
        self.input_precoCompra.setText(moeda(dados['preco_compra']))
        self.inputMargem.setText(mascara_porcento(dados['margem']))
        self.input_lucro.setText(moeda(dados['lucro']))
        self.input_precoVenda.setText(moeda(dados['preco_venda']))
        self.input_observacao.setText(dados['observacao'])

    def receber_dados(self):
        return {
            "id": None,
            "cod_barras": self.input_codBarras.text(),
            "descricao": self.input_descricao.text(),
            "fornecedorId": self.input_fornecedor.currentText(),
            "unidade": self.input_unidade.currentText(),
            "preco_compra": limpar_dinheiro(self.input_precoCompra.text()),
            "margem": limpar_porcento(self.inputMargem.text()),
            "lucro": limpar_dinheiro(self.input_lucro.text()),
            "preco_venda": limpar_dinheiro(self.input_precoVenda.text()),
            "preco_atacado": 0,
            "observacao": self.input_observacao.toPlainText(),
        }