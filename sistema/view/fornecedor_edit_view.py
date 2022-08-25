from PySide2.QtWidgets import QDialog
from sistema.model.fornecedore_model import FornecedorModel
from interface.telas.fornecedor_edicao import Ui_FornecedorEdit
from sistema.view.fornecedor_view import FornecedorView


class FornecedorEditView(Ui_FornecedorEdit, QDialog, FornecedorView):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setModal(True)

    def preencher_campos(self, dados: FornecedorModel.dados):
        self.input_nome.setText(dados['nome'])
        self.input_celular.setText(dados['celular'])
        self.input_telefone.setText(dados['telefone'])
        self.input_cpf.setText(dados['cpf_cnpj'])
        self.input_inscricaoEstadual.setText(dados['inscricao_estadual'])
        self.input_email.setText(dados['email'])
        self.input_cep.setText(dados['cep'])
        self.input_endereco.setText(dados['endereco'])
        self.input_complemento.setText(dados['complemento'])
        self.input_bairro.setText(dados['bairro'])
        self.input_cidade.setText(dados['cidade'])
        self.input_uf.setText(dados['uf'])
        self.input_observacao.setText(dados['observacao'])
