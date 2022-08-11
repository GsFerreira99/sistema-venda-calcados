#PySide2
from PySide2.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PySide2 import QtGui

#Controllers
from sistema.controller.main_controller import MainController

import sys


class App(QMainWindow):

    def __init__(self):
        self.definir_window()
        self.main = MainController(self.StackedWidget)
        self.main.definir_telas()
        self.main.definir_telas_sistema()

    def definir_window(self):
        self.StackedWidget = QStackedWidget()
        self.StackedWidget.setWindowIcon(QtGui.QIcon('logo.ico'))

    def exibir_tela_login(self):
        self.StackedWidget.show()
    

if __name__ == "__main__":
    root = QApplication(sys.argv)
    app = App()
    app.exibir_tela_login()
    sys.exit(root.exec_())
