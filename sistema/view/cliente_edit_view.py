#PySide2
from PySide2.QtWidgets import QDialog
from PySide2.QtCore import QDate

from sistema.funcoes.genericos import cpf_cnpj, celular, data

#Telas
from interface.telas.cliente_edicao import Ui_ClienteEdit

class ClienteEditView(Ui_ClienteEdit, QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setModal(True)

    def limpar(self):
        self.input_nome.setText('')
        self.input_celular.setText('')
        self.input_telefone.setText('')
        self.input_cpf.setText('')
        self.input_inscricaoEstadual.setText('')
        self.input_nascimento.setDate(QDate(2000, 1, 1))
        self.input_email.setText('')
        self.input_cep.setText('')
        self.input_endereco.setText('')
        self.input_complemento.setText('')
        self.input_bairro.setText('')
        self.input_cidade.setText('')
        self.input_uf.setText('')
        self.input_observacao.setText('')

    def preencher_campos(self, dados):
        self.input_nome.setText(dados['nome'])
        self.input_celular.setText(dados['celular'])
        self.input_telefone.setText(dados['telefone'])
        self.input_cpf.setText(dados['cpf_cnpj'])
        self.input_inscricaoEstadual.setText(dados['inscricao_estadual'])
        self.input_nascimento.setDate(data(dados['nascimento']))
        self.input_email.setText(dados['email'])
        self.input_cep.setText(dados['cep'])
        self.input_endereco.setText(dados['endereco'])
        self.input_complemento.setText(str(dados['complemento']))
        self.input_bairro.setText(str(dados['bairro']))
        self.input_cidade.setText(dados['cidade'])
        self.input_uf.setText(str(dados['uf']))
        self.input_observacao.setText(dados['observacao'])

    def receber_dados(self):
        return {
            "criado_em": None,
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