from sistema.view.estoque_view import EstoqueView
from sistema.model.estoque_model import EstoqueModel



class EstoqueController:

    def __init__(self) -> None:
        self.view = EstoqueView()
        self.model = EstoqueModel()

        self.view.btn_consulta.clicked.connect(lambda: self.view.navegacao(1))
        self.view.btn_novo.clicked.connect(lambda: self.view.navegacao(2))