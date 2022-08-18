from PySide2.QtWidgets import QDialog
from interface.telas.estoque_adicionar import Ui_EstoqueAdicionar


class EstoqueAdicionarView(Ui_EstoqueAdicionar, QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setModal(True)

        self.objeto = None

    def inserir_dados(self, objeto: object):
        self.objeto = objeto

    def limpar(self):
        self.input_quantidade.setValue(0)

    def editar_titulo(self):
        self.label_3.setText(self.objeto['descricao'])

    def receber_dados(self):
        return self.input_quantidade.value()
