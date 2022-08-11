from sistema.view.vendas_view import VendasView
from sistema.model.vendas_model import VendasModel



class VendasController:

    def __init__(self) -> None:
        self.view = VendasView()
        self.model = VendasModel()