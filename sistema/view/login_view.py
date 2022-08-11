#PySide2
from PySide2.QtWidgets import QWidget

#Telas
from interface.telas.login import Ui_Login


class LoginView(Ui_Login, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

    
    def receber_credenciais_login(self):
        return {'usuario' : self.input_usuario.text(), 'senha' : self.input_senha.text()}

    def mensagem_erro(self, status):
        if status == False:
            self.lb_mensagem.setMaximumHeight(30)
        else:
            self.lb_mensagem.setMaximumHeight(0)
    