#PySide2
from PySide2.QtWidgets import QWidget

#Telas
from interface.telas.usuarios import Ui_Usuarios

class UsuarioView(Ui_Usuarios, QWidget):

    def __init__(self, parent=None): 
        super().__init__(parent)
        super().setupUi(self)

        self.stackedWidget.setCurrentIndex(1)

    def linha_selecionada(self):
        return self.table_usuarios.currentRow()

    def vazios(self):
        pass

    def navegacao(self, index: int):
        pass
