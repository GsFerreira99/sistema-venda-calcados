from PySide2.QtWidgets import QDialog
from interface.telas.relatorio_geral_vendas import Ui_RelatorioGeralVendas
from sistema.funcoes.genericos import calcular_mes
import datetime
from calendar import monthrange


class RelatorioGeralVendasView(Ui_RelatorioGeralVendas, QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setModal(True)
        self.definir_data()

        self.objeto = None

        self.input_periodo.currentIndexChanged.connect(lambda: self.exibir_periodos())

    def exibir_periodos(self):
        if self.input_periodo.currentText() == 'Selecionar Periodo':
            self.frame_periodo.setMaximumHeight(50)
        else:
            self.frame_periodo.setMaximumHeight(0)

    def definir_data(self):
        hoje = datetime.date.today()
        self.input_data_ini.setDate(hoje)
        self.input_data_fim.setDate(hoje)

    def get_periodo(self):
        hoje = datetime.date.today()
        if self.input_periodo.currentText() == 'Mês Atual':
            return datetime.date(hoje.year, hoje.month, 1), hoje
        elif self.input_periodo.currentText() == 'Mês Anterior':
            mes = calcular_mes(hoje.month, 1)
            day = monthrange(hoje.year, mes)[1]
            return datetime.date(hoje.year, mes, 1), datetime.date(hoje.year, mes, day)
        elif self.input_periodo.currentText() == 'Selecionar Periodo':
            return self.input_data_ini.date().toPython(), self.input_data_fim.date().toPython()
