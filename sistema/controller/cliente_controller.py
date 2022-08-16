from sistema.view.cliente_view import ClienteView
from sistema.model.cliente_model import ClienteModel



class ClienteController:

    def __init__(self) -> None:
        self.view = ClienteView()
        self.model = ClienteModel()

        self.view.btn_consulta.clicked.connect(lambda: self.view.navegacao(1))
        self.view.btn_novo.clicked.connect(lambda: self.view.navegacao(2))