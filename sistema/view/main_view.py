#PySide2
from PySide2.QtWidgets import QWidget
from funcoes.animacoes import toggle

#Telas
from interface.telas.main import Ui_Home


class MainView(Ui_Home, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

    def animacao_menu_lateral(self, ui):
        toggle.toggle_width(ui, self.left_bar, 150, True)


