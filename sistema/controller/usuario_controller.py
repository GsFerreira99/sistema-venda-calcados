from datetime import datetime
from sistema.view.usuario_view import UsuarioView
from sistema.model.usuario_model import TabelaUsuario, UsuarioModel
from sistema.view.usuario_novo_view import UsuarioNovoView
from sistema.view.usuario_edit_view import UsuarioEditView

from sistema.funcoes.poupup import mensagem, confirma
from PySide2.QtWidgets import QMessageBox

import pandas as pd


class UsuarioController:
    table: TabelaUsuario
    modelEdit: UsuarioModel

    def __init__(self, db) -> None:
        self.__db = db
        self.view = UsuarioView()
        self.novo = UsuarioNovoView()
        self.edit = UsuarioEditView()

        self.novo.btn_salvar.clicked.connect(lambda: self.salvar_novo_usuario())
        self.edit.btn_salvar.clicked.connect(lambda: self.salvar_edicao())

        self.view.btn_novo.clicked.connect(lambda: self.exibir_novo())
        self.view.btn_consultar.clicked.connect(lambda: self.editar())
        self.view.btn_deletar.clicked.connect(lambda: self.deletar())
        self.view.btn_busca.clicked.connect(lambda: self.busca())

    def deletar(self):
        model = UsuarioModel(self.__db, self.table.retorna_objeto(self.view.linha_selecionada()))
        status = confirma(f"Deseja deletar o usuario '{model.dados['usuario']}'?", QMessageBox.Information, 'Confirmação')
        if status is True:
            if model.deletar() is False:
                mensagem(f"Usuario '{model.dados['usuario']}' não pode ser deletado.", QMessageBox.Information, 'Info')
            else:
                mensagem(f"Usuario '{model.dados['usuario']}' deletado com sucesso.", QMessageBox.Information, 'Info')
                self.busca()

    def exibir_novo(self):
        self.novo.limpar()
        self.novo.show()

    def salvar_novo_usuario(self):
        if self.novo.validar_senha() is False:
            mensagem(f"Informe as senhas iguais.", QMessageBox.Warning, 'Erro')
        else:
            if self.novo.verificar_vazios() is False:
                mensagem(f"Preencha todos os campos.", QMessageBox.Warning, 'Erro')
            else:
                model = UsuarioModel(self.__db, pd.Series(self.novo.receber_dados()))
                model.salvar()
                mensagem(f"Usuário Cadastrado com Sucesso.", QMessageBox.Information, 'Confirmar')
                self.novo.limpar()
                self.novo.close()

    def editar(self):
        self.modelEdit = UsuarioModel(self.__db, self.table.retorna_objeto(self.view.linha_selecionada()))
        self.edit.limpar()
        self.edit.preencher_campos(self.modelEdit.dados)
        self.edit.show()

    def salvar_edicao(self):
        self.modelEdit.atualizar_dados(self.edit.receber_dados())
        status = self.modelEdit.editar()
        if status == False:
            texto = f"Usuario '{self.modelEdit.dados['usuario']}' não pode ter seu tipo alterado."
        elif status:
            texto = "Usuario editado com sucesso!"
            self.edit.limpar()
            self.edit.close()
            self.busca()
        else:
            texto = "Erro ao atualizar usuario, verifique os campos."
        mensagem(texto, QMessageBox.Information, 'Info')


    def limpar_tela(self):
        self.view.limpar()

    def busca(self):
        campo = self.view.input_pesquisa.text()
        if campo == '':
            select = self.__db.select("SELECT * FROM usuarios WHERE ativado = TRUE")
        else:
            select = self.__db.select(f"""SELECT * FROM usuarios WHERE usuario LIKE '%{campo}%' 
            OR nome LIKE '%{campo}%' OR sobrenome LIKE '%{campo}%' OR tipo = '{campo}' OR id = '{campo}'
             AND ativado = TRUE""")
        self.table = TabelaUsuario(self.view.table_usuarios, select, self.__db)
        self.table.preencher_tabela()
