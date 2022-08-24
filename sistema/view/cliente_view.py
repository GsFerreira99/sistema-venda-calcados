#PySide2
from PySide2.QtWidgets import QWidget

#Telas
from interface.telas.cliente import Ui_Cliente

class ClienteView(Ui_Cliente, QWidget):

    def __init__(self, parent=None): 
        super().__init__(parent)
        super().setupUi(self)

    def navegacao(self, index:int):
        botoes = {
            1 : self.btn_consulta,
            2 : self.btn_novo
        }
 
        self.stackedWidget.setCurrentIndex(index)

        for ind, botao in botoes.items():
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

    def limpar(self):
        self.input_nome.setText('')
        self.input_celular.setText('')
        self.input_telefone.setText('')
        self.input_cpf.setText('')
        self.input_inscricaoEstadual.setText('')
        self.input_email.setText('')
        self.input_cep.setText('')
        self.input_endereco.setText('')
        self.input_complemento.setText('')
        self.input_bairro.setText('')
        self.input_cidade.setText('')
        self.input_uf.setText('')
        self.input_observacao.setText('')

    def receber_dados(self):
        return {
            "criado_em" : None,
            "nome": self.input_nome.text(),
            "celular": self.input_celular.text(),
            "telefone": self.input_telefone.text(),
            "cpf_cnpj": self.input_cpf.text(),
            "inscricao_estadual": self.input_inscricaoEstadual.text(),
            "nascimento": self.input_nascimento.date().toPython(),
            "email": self.input_email.text(),
            "cep": self.input_cep.text(),
            "endereco": self.input_endereco.text(),
            "complemento": self.input_complemento.text(),
            "bairro": self.input_bairro.text(),
            "cidade": self.input_cidade.text(),
            "uf": self.input_uf.text(),
            "observacao": self.input_observacao.toPlainText(),
        }

    def linha_selecionada(self):
        return self.table_clientes.currentRow()

    def vazios(self):
        pass