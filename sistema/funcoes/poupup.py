from PySide2.QtWidgets import QMessageBox

def mensagem(mensagem, tipo, titulo="Confirmação",):
        msg = QMessageBox()
        msg.setWindowTitle(titulo)
        msg.setIcon(tipo)
        msg.setText(mensagem)
        msg.addButton(QMessageBox.Ok)

        msg.exec_()

def confirma(mensagem, tipo, titulo="Confirmação",):
        status = False
        msg = QMessageBox()
        msg.setWindowTitle(titulo)
        msg.setIcon(tipo)
        msg.setText(mensagem)
        btn_yes = msg.addButton(QMessageBox.Yes)
        msg.addButton(QMessageBox.No)

        execute = msg.exec_()

        if execute == QMessageBox.Yes:
            status = True

        return status