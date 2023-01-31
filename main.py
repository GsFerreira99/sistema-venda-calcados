from PySide2.QtWidgets import QApplication, QStackedWidget
from PySide2 import QtGui

from sistema.controller.main_controller import MainController

import sys


class App:

    def __init__(self):
        self.StackedWidget = QStackedWidget()
        self.StackedWidget.setWindowIcon(QtGui.QIcon('logo.ico'))
        self.main = MainController(self.StackedWidget)
        self.main.definir_telas()
        self.main.definir_telas_sistema()

    def tamanho_tela(self):
        self.StackedWidget.setStyleSheet("background-color: rgb(236, 242, 248);")
        self.StackedWidget.setMinimumSize(450, 600)

    def exibir_tela_login(self):
        self.StackedWidget.show()



if __name__ == "__main__":
    root = QApplication(sys.argv)
    app = App()
    app.tamanho_tela()
    app.exibir_tela_login()
    sys.exit(root.exec_())
