#PySide2
from PySide2.QtWidgets import QWidget

#Telas
from interface.telas.vendas import Ui_Vendas

class VendasView(Ui_Vendas, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)