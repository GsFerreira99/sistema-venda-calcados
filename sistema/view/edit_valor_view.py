from PySide2.QtWidgets import QDialog
from interface.telas.edit_valor import Ui_EditValor


class EditValorView(Ui_EditValor, QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setModal(True)


    def limpar(self):
        self.input.setText("")

    def editar_titulo(self, texto: str):
        self.texto.setText(texto.title())

    def editar_valor(self, valor: str):
        self.input.setText(str(valor))

    def receber_dados(self):
        return self.input.text()

    def receber_tipo(self):
        return self.texto.text()
