from PySide2.QtWidgets import QStackedWidget


class View:
    _botoes: dict
    _nav_widget = QStackedWidget

    def __init__(self):
        """OBRIGATÓRIO DEFINIR OS ATRIBUTOS botoes e nav_widget"""
        pass

    @property
    def botoes(self):
        return self._botoes

    @property
    def nav_widget(self):
        return self._nav_widget

    @botoes.setter
    def botoes(self, botoes: dict):
        """ex.: {1: self.btn_consulta,2: self.btn_novo}"""
        self._botoes = botoes

    @nav_widget.setter
    def nav_widget(self, widget: QStackedWidget):
        """ex.: self.stackedWidget"""
        self._nav_widget = widget

    def navegacao(self, index: int):
        self.nav_widget.setCurrentIndex(index)

        for ind, botao in self.botoes.items():
            if ind == index:
                botao.setStyleSheet("""
                    QPushButton{
                        color: white;
                        border: none;
                        border-radius: 0;
                        border-top-left-radius: 10px;
                        border-top-right-radius: 10px;
                        background-color: rgb(56, 91, 138)
                    }
                """)
            else:
                botao.setStyleSheet("""
                    QPushButton{
                        color: white;
                        border: none;
                        border-radius: 0;
                        border-top-left-radius: 10px;
                        border-top-right-radius: 10px;
                        background-color: rgb(74, 121, 184)
                    }

                    QPushButton:hover{
                        background-color: rgb(89, 146, 221)
                    }

                    QPushButton:pressed{
                        background-color: rgb(42, 68, 103)
                    }
                """)


