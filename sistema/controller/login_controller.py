from sistema.model.login_model import LoginModel
from sistema.view.login_view import LoginView


class LoginController:

    def __init__(self, parent=None):
        self.view = LoginView(parent)
        self.model = LoginModel()

        self.view.btn_acessar.setAutoDefault(True)

    def acessar_sistema(self):
        self.model.definir_credenciais(self.view.receber_credenciais_login())
        autenticacao = self.model.autenticar()
        if autenticacao == True:
            self.view.mensagem_erro(autenticacao)
            return True
        else:
            self.view.mensagem_erro(autenticacao)
            
        
