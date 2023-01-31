#PySide2
from PySide2.QtWidgets import QWidget

#Telas
from interface.telas.usuario_novo import Ui_UsuarioNovo

class UsuarioNovoView(Ui_UsuarioNovo, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)


    def linha_selecionada(self):
        return self.table_usuarios.currentRow()

    def limpar(self):
        self.input_usuario.setText('')
        self.input_senha.setText('')
        self.input_senhaComfirm.setText('')
        self.input_nome.setText('')
        self.input_sobrenome.setText('')
        self.input_tipo.setCurrentIndex(0)

    def validar_senha(self):
        if self.input_senha.text() == self.input_senhaComfirm.text():
            return True
        else:
            return False

    def receber_dados(self):
        return {
            "usuario": self.input_usuario.text(),
            "senha": self.input_senha.text(),
            "nome": self.input_nome.text(),
            "sobrenome": self.input_sobrenome.text(),
            "tipo": self.id_tipo(self.input_tipo.currentText()),
        }

    def verificar_vazios(self):
        if self.input_usuario.text() != '' and self.input_senha.text() != '' and self.input_nome.text() != ''\
                and self.input_sobrenome.text() != '' and self.input_tipo.currentText() != '':
            return True
        else:
            return False

    def id_tipo(self, tipo):
        tipos = {
            'ADMINISTRADOR': 1,
            'USUARIO': 2
        }
        if tipo != 0:
            return tipos[tipo]
        else:
            return 2

    def navegacao(self, index: int):
        pass