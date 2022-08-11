class LoginModel:

    def __init__(self) -> None:
        self.__usuario = None
        self.__senha = None


    def definir_credenciais(self, credenciais:dict):
        self.__usuario = credenciais['usuario']
        self.__senha = credenciais['senha']

    def autenticar(self):
        if self.__usuario == '' or self.__senha == '':
            return False
        elif self.__usuario == 'gabriel' and self.__senha == 'gsf151299':
            return True
        else:
            return False
