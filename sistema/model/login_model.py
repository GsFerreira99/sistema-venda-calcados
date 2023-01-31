class LoginModel:

    def __init__(self, db:object) -> None:
        self.db = db
        self.__usuario = None
        self.__senha = None

    def definir_credenciais(self, credenciais:dict):
        self.__usuario = credenciais['usuario']
        self.__senha = credenciais['senha']

    def autenticar(self):
        if self.__usuario == '' or self.__senha == '':
            return False
        consulta = self.db.select(f"""SELECT * FROM usuarios WHERE usuario = '{self.__usuario}' AND
         senha = '{self.__senha}' AND ativado = TRUE""")
        if consulta.empty is False:
            return consulta
        else:
            return False
