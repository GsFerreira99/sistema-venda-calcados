#PySide2
from PySide2.QtWidgets import QWidget

from sistema.funcoes.genericos import gerar_cod_barras, limpar_dinheiro, limpar_porcento, moeda, mascara_porcento

from sistema.funcoes.tabela import Tabela
#Telas
from interface.telas.estoque import Ui_Estoque

class EstoqueView(Ui_Estoque, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.input_precoVenda.editingFinished.connect(lambda: self.calculo_margem())

        self.input_precoCompra.editingFinished.connect(lambda: self.input_precoCompra.setText(moeda(self.input_precoCompra.text())))
        self.input_precoVenda.editingFinished.connect(lambda: self.input_precoVenda.setText(moeda(self.input_precoVenda.text())))
        self.input_lucro.editingFinished.connect(lambda: self.input_lucro.setText(moeda(self.input_lucro.text())))
        self.inputMargem.editingFinished.connect(lambda: self.inputMargem.setText(mascara_porcento(self.inputMargem.text())))

        self.btn_salvar_2.clicked.connect(lambda: self.input_codBarras.setText(f"{gerar_cod_barras()}"))

    def preencher_tabela(self):
        pass

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

    def navegacao(self, index:int):
        botoes = {
            1 : self.btn_consulta,
            2 : self.btn_novo
        }
 
        self.stackedWidget.setCurrentIndex(index)

        for ind, botao in botoes.items():
            if ind == index:
                botao.setStyleSheet("""
                    QPushButton{
                        color: white;
                        border: none;
                        border-radius: 0;
                        border-top-left-radius: 10px;
                        border-top-right-radius: 10px;
                        background-color: rgb(56, 91, 138)
                    }
                """)
            else:
                botao.setStyleSheet("""
                    QPushButton{
                        color: white;
                        border: none;
                        border-radius: 0;
                        border-top-left-radius: 10px;
                        border-top-right-radius: 10px;
                        background-color: rgb(74, 121, 184)
                    }

                    QPushButton:hover{
                        background-color: rgb(89, 146, 221)
                    }

                    QPushButton:pressed{
                        background-color: rgb(42, 68, 103)
                    }
                """)

    def calculo_margem(self):
        compra = limpar_dinheiro(self.input_precoCompra.text())
        venda = limpar_dinheiro(self.input_precoVenda.text())
        valLucro = venda - compra
        percLucro = (valLucro*100)/venda

        self.input_lucro.setText(moeda(valLucro))
        self.inputMargem.setText(mascara_porcento(percLucro))

    def linha_selecionada(self):
        return self.table_produtos.currentRow()

    def receber_dados(self):
        return {
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