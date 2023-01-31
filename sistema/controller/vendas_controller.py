import datetime

import pandas as pd

from sistema.funcoes.poupup import confirma, mensagem
from PySide2.QtWidgets import QMessageBox, QFileDialog
from sistema.database.banco import DataBase
from sistema.funcoes.controller import Controller
from sistema.view.vendas_view import VendasView
from sistema.view.vendas_edit_view import VendasEditView
from sistema.model.vendas_model import VendasModel, TabelaVenda, TabelaVendas, TabelaVendaEdit
from sistema.funcoes.genericos import preencher_combo_box, converter_string_int, mascara_porcento, \
    limpar_dinheiro, limpar_porcento

from sistema.view.edit_valor_view import EditValorView

from sistema.funcoes.genericos import moeda
from sistema.view.relatorio_geral_vendas_view import RelatorioGeralVendasView
from sistema.relatorios.venda import RelatorioVenda


class VendasController(Controller):

    view: VendasView
    model: VendasModel
    modelEdit: VendasModel

    def __init__(self, db: DataBase, view):
        super().__init__(db, view)

        self.edit = VendasEditView()
        self.view_edit_item = EditValorView()
        self.relatorioGeralVendas = RelatorioGeralVendasView()

        self.view.btn_novo.clicked.connect(lambda: self.criar_venda())
        self.view.btn_add.clicked.connect(lambda: self.adicionar_item())

        self.view.btn_salvar.clicked.connect(lambda: self.salvar_venda())

        self.view.input_descricao.currentIndexChanged.connect(lambda: self.cb_preco())
        self.view.input_percDesc.editingFinished.connect(lambda: self.desconto())
        self.view.input_quantidade.editingFinished.connect(lambda: self.definir_total())
        self.view.input_totalPago.editingFinished.connect(lambda: self.mascara_total_pago())

        self.view.btn_deletar.clicked.connect(lambda: self.deletar())

        self.view.input_descricao.lineEdit().editingFinished.connect(lambda: self.pesquisa_cod_barras())

        self.view.btn_busca.clicked.connect(lambda: self.buscar())
        self.view.btn_editar.clicked.connect(lambda: self.editar())
        self.view.btn_relatorio_geral.clicked.connect(lambda: self.relatorio_geral())

        self.relatorioGeralVendas.btn_gerar.clicked.connect(lambda: self.gerar_relatorio_geral_vendas())

        self.view.btn_remover.clicked.connect(lambda: self.remover_item())

        self.edit.btn_relatorio.clicked.connect(lambda: self.relatorio_resumido())
        self.edit.btn_relatorio_full.clicked.connect(lambda: self.relatorio_completo())
        self.edit.btn_relatorioFornecedores.clicked.connect(lambda: self.relatorio_fornecedores())

        self.view.table.cellClicked.connect(lambda: self.editar_item_venda())
        self.view_edit_item.btn_salvar.clicked.connect(lambda: self.editar_item(self.view.table.currentRow()))

    def editar_item(self, row):
        valor = self.view_edit_item.receber_dados()
        tipo = self.view_edit_item.receber_tipo().lower()
        if tipo == 'quantidade':
            try:
                valor = int(valor)
            except ValueError:
                self.view_edit_item.limpar()
                self.view_edit_item.close()

        if row != -1:
            dados = {
                    'id': row,
                    'tipo': tipo,
                    'valor': valor
                                 }
            self.model.atualizar_item(dados)
            self.table.preencher_tabela()
            self.view_edit_item.limpar()
            self.view_edit_item.close()
            self.definir_totais()

    def editar_item_venda(self):
        row = self.view.table.currentRow() if  self.view.table.currentRow() >= 0 else 0
        item = self.model.items_venda[row + 1]
        try:
            if 3 == self.view.table.currentItem().column():
                self.view_edit_item.editar_titulo('quantidade')
                self.view_edit_item.editar_valor(item['quantidade'])
            elif 4 == self.view.table.currentItem().column():
                self.view_edit_item.editar_titulo('tamanho')
                self.view_edit_item.editar_valor(item['tamanho'])
            elif 5 == self.view.table.currentItem().column():
                self.view_edit_item.editar_titulo('cor')
                self.view_edit_item.editar_valor(item['cor'])
            self.view_edit_item.show()
        except AttributeError:
            pass


    def definir_user(self, user):
        self.user = user

    def deletar(self):
        model = VendasModel(self.db, self.table.retorna_objeto(self.view.linha_selecionada()), 'vendas')
        status = confirma(f"Deseja deletar a venda '{model['codigo']}'?", QMessageBox.Information,
                          'Confirmação')
        if status:
            model.deletar()
            mensagem(f"Venda '{model['codigo']}' deletada com sucesso.", QMessageBox.Information, 'Info')
            self.buscar()

    def buscar(self):
        campo = self.view.input_pesquisa.text()
        periodo_status = self.view.radio_periodo.isChecked()
        select = []
        ini = self.view.input_data_ini.date().toPython()
        fim = self.view.input_data_fim.date().toPython()
        if periodo_status is False:
            periodo = ''
        else:
            periodo = f"data_venda BETWEEN '{ini}' AND '{fim}' AND ativado = TRUE"

        if campo == '':
            if periodo_status is True:
                periodo = 'WHERE ' + periodo
            else:
                periodo = 'WHERE ativado = TRUE'
            select = [f"SELECT * FROM vendas {periodo}"]
        else:
            if periodo_status is True:
                periodo = 'AND ' + periodo
            try:
                clientes = int(campo)
            except:
                clientes = self.db.select(f"""SELECT * FROM cliente WHERE nome LIKE '%{campo}%' AND ativado = TRUE""")

            if type(clientes) != int:
                for index, cliente in clientes.iterrows():
                    select.append(
                        f"""SELECT * FROM vendas WHERE cliente = {cliente['id']} {periodo}""")
            else:
                select.append(
                    f"""SELECT * FROM vendas WHERE codigo = {campo} {periodo}""")

        tabela = TabelaVendas(self.view.table_vendas, {}, self.db)
        self.busca(self.view.input_pesquisa.text(), 'vendas', select, tabela)

    def busca(self, campo: str, tabela_db: str, sql: list, tabela_class):
        campo = '0'
        for j, i in enumerate(sql):
            if j == 0:
                df = self.db.pesquisar(campo, tabela_db, i)
            else:
                dados = self.db.pesquisar(campo, tabela_db, i)
                df = pd.concat([dados, df])

        self.table = tabela_class
        self.table.atualizar_df(df)
        self.table.preencher_tabela()

    def relatorio_geral(self):
        self.relatorioGeralVendas.definir_data()
        self.relatorioGeralVendas.show()

    def relatorio_resumido(self):
        rel, items = self.relatorio()

        rel.vendas(items, self.db)
        rel.pdf.salvar()
        mensagem('Relatório gerado com sucesso!.', QMessageBox.Information, 'Sucesso')

    def gerar_relatorio_geral_vendas(self):
        caminho = self.caminho_relatorio()
        if type(caminho) != str or caminho == '':
            return

        data_inicio, data_fim = self.relatorioGeralVendas.get_periodo()

        vendas = self.db.select(f"SELECT * FROM vendas WHERE data_venda BETWEEN '{data_inicio}' AND '{data_fim}'")

        vendas['cliente'] = vendas['cliente'].astype(str)
        for index, venda in vendas.iterrows():
            vendas.loc[index, 'cliente'] = self.db.select(f'SELECT nome FROM cliente WHERE id = {venda["cliente"]}')['nome'][0]

        rel = RelatorioVenda(caminho)
        rel.cabecalho_vendas_geral([data_inicio, data_fim])
        rel.vendas_geral(vendas)
        rel.pdf.salvar()

        mensagem('Relatório gerado com sucesso!.', QMessageBox.Information, 'Sucesso')

    def relatorio(self):
        caminho = self.caminho_relatorio()
        if type(caminho) != str or caminho == '':
            return

        rel = RelatorioVenda(caminho)
        venda = self.db.select(f"SELECT * FROM vendas WHERE codigo = {self.edit.input_nrVenda_2.text()}")
        cliente = self.db.select(f"SELECT * FROM cliente WHERE nome = '{self.edit.input_cliente.text()}'")
        items = self.db.select(f"SELECT * FROM item_venda WHERE venda = {venda['id'][0]}")

        if len(items) == 1:
            items = pd.DataFrame(items)

        rel.cabecalho()
        rel.dados_venda({'data': venda['data_venda'][0].strftime('%d/%m/%Y'), 'venda': venda['id'][0]})
        rel.endereco_entrega(cliente)

        return rel, items

    def relatorio_completo(self):
        rel, items = self.relatorio()

        rel.vendas_detalhado(items, self.db)
        rel.pdf.salvar()
        mensagem('Relatório gerado com sucesso!.', QMessageBox.Information, 'Sucesso')

    def relatorio_fornecedores(self):
        caminho = self.caminho_relatorio_pasta()
        if type(caminho) != str or caminho == '':
            return

        venda = self.db.select(f"SELECT * FROM vendas WHERE codigo = {self.edit.input_nrVenda_2.text()}")
        cliente = self.db.select(f"SELECT * FROM cliente WHERE nome = '{self.edit.input_cliente.text()}'")
        items = self.db.select(f"SELECT * FROM item_venda WHERE venda = {venda['id'][0]}")

        vendas = {}
        fornecedores = set([])
        for index, linha in items.iterrows():
            produto = self.db.select(f"SELECT * FROM estoque WHERE id = {linha['produto']}")
            fornecedor = self.db.select(f"SELECT * FROM fornecedor WHERE id = {produto['fornecedorId'][0]}")
            vendas[index] = [fornecedor['nome'][0], linha]
            fornecedores.add(fornecedor['nome'][0])

        dados = {}
        for fornecedor in fornecedores:
            dados[fornecedor] = []
            for index, item in enumerate(vendas.values()):
                if fornecedor == item[0]:
                    dados[fornecedor].append(item[1])

        for fornecedor, vend in dados.items():
            rel = RelatorioVenda(f'{caminho}/{venda["codigo"][0]}_{fornecedor}_{cliente["nome"][0]}.pdf')
            rel.cabecalho()
            rel.dados_venda({'data': venda['data_venda'][0].strftime('%d/%m/%Y'), 'venda': venda['id'][0]})
            rel.endereco_entrega(cliente)
            rel.vendas_fornecedor(vend, fornecedor, self.db)
            rel.pdf.salvar()
        mensagem('Relatório gerado com sucesso!.', QMessageBox.Information, 'Sucesso')

    def criar_venda(self):
        dados = self.criar_df()
        self.model = VendasModel(self.db, dados, 'vendas')
        self.model.definir_usuario(self.user['id'])
        self.atualizar_tela()
        self.view.atualizar_tela(self.model.dados)
        self.cb_clientes()
        self.cb_produtos()

    @staticmethod
    def caminho_relatorio():
        try:
            arquivo = QFileDialog.getSaveFileName(caption="Exportar relatório em PDF",
                                                  directory="", filter="PDF files (*.pdf)")[0]
            return arquivo
        except FileNotFoundError:
            return None

    @staticmethod
    def caminho_relatorio_pasta():
        try:
            arquivo = QFileDialog.getExistingDirectory(caption="Exportar relatório em PDF",
                                                  filter="PDF files (*.pdf)")
            return arquivo
        except FileNotFoundError:
            return None

    def cb_clientes(self):
        clientes = self.db.select("SELECT DISTINCT nome FROM cliente WHERE ativado = TRUE")['nome'].values.tolist()
        preencher_combo_box(clientes, self.view.input_cliente)

    def cb_produtos(self):
        produtos = self.db.select(
            "SELECT DISTINCT descricao FROM estoque WHERE ativado = TRUE ORDER BY descricao")['descricao'].values.tolist()
        preencher_combo_box(produtos, self.view.input_descricao)

    def pesquisa_cod_barras(self):
        try:
            int(self.view.input_descricao.currentText())
            cod = self.view.input_descricao.currentText()
            produto = self.db.select(f"SELECT descricao FROM estoque WHERE cod_barras = '{cod}' AND ativado = TRUE").iloc[0, 0]
            self.cb_produtos()
            self.view.input_descricao.setCurrentText(produto)
            self.cb_preco()

        except:
            return


    def cb_preco(self):
        preco = self.db.select(f"""SELECT preco_venda FROM estoque WHERE descricao = '{self.view.campo_produto}'""")
        if preco.empty is True:
            self.view.preencher_preco(moeda(0.0))
        else:
            self.view.preencher_preco(moeda(preco.iloc[0, 0]))
        self.definir_desconto()
        self.definir_total()

    def remover_item(self):
        try:
            row = self.view.table.currentRow()
        except:
            return
        if type(row) == int:
            self.model.remover(row)
            self.table = TabelaVenda(self.view.table, self.model.get_items_venda(), self.db)
            self.table.preencher_tabela()
            self.definir_totais()


    def salvar_venda(self):
        if self.view.input_cliente.currentText() != '':
            self.model['data_venda'] = self.view.input_data.date().toPython()
            try:
                self.model['codigo'] = int(self.view.input_nrVenda.text())
            except:
                mensagem('Informe um numero de venda válido!', QMessageBox.Warning, 'Error')
            self.model.dados['cliente'] = int(self.db.select(
                f"SELECT id FROM cliente WHERE nome = '{self.view.input_cliente.currentText()}'").iloc[0, 0])
            self.model.dados['total_pago'] = limpar_dinheiro(self.view.input_totalPago.text())
            self.model.dados['troco'] = limpar_dinheiro(self.view.input_troco.text())
            if confirma('Finalizar e salvar venda?', QMessageBox.Information, 'Confirmação') is True:
                self.model.salvar("""
                INSERT INTO vendas (
                    codigo,
                    data_venda,
                    cliente,
                    total_bruto,
                    desconto,
                    total_liquido,
                    total_items,
                    total_pago,
                    troco,
                    vendido_por)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """)
                self.model.salvar_items()
                mensagem('Venda cadastrada com sucesso.', QMessageBox.Information, 'Sucesso')
                self.view.navegacao(1)
        else:
            mensagem('Selecione um Cliente.', QMessageBox.Information, 'Erro')

    def troco(self):
        troco = limpar_dinheiro(self.view.input_totalPago.text()) - self.model.dados['total_liquido']
        self.view.input_troco.setText(moeda(troco))

    def mascara_total_pago(self):
        self.view.input_totalPago.setText(moeda(self.view.input_totalPago.text()))
        self.troco()

    def atualizar_tela(self):
        self.definir_qnt()
        self.definir_desconto()
        self.definir_totais()

    def definir_total(self):
        total = (limpar_dinheiro(self.view.input_preco.text()) * converter_string_int(self.view.input_quantidade.text())) - \
                limpar_dinheiro(self.view.input_valDesc.text())
        self.view.input_total.setText(moeda(total))

    def desconto(self):
        val = (limpar_porcento(self.view.input_percDesc.text()) * 0.01) * (converter_string_int(
            self.view.campo_quantidade) * limpar_dinheiro(self.view.campo_preco))
        self.view.input_percDesc.setText(mascara_porcento(self.view.input_percDesc.text()))
        self.view.input_valDesc.setText(moeda(val))
        self.definir_total()

    def definir_desconto(self):
        self.view.input_percDesc.setText(mascara_porcento(0))
        self.view.input_valDesc.setText(moeda(0))

    def definir_qnt(self):
        self.view.input_quantidade.setText('1')

    def limpar(self):
        self.view.input_cor.setText('')
        self.view.input_tamanho.setText('')

    def criar_df(self):
        return pd.Series({
            'id': self.nr_venda(),
            'codigo': int(self.nr_venda()),
            'data_venda': datetime.datetime.now(),
            'cliente': 0,
            'total_bruto': 0.0,
            'desconto': 0.0,
            'total_liquido': 0.0,
            'total_items': 0,
            'total_pago': 0.0,
            'troco': 0.0,
        })

    def inserir_valores_totais(self, dados: pd.Series):
        self.model.dados['total_bruto'] = self.model.dados['total_bruto'] + dados['total_bruto']
        self.model.dados['desconto'] = self.model.dados['desconto'] + dados['valor_desconto']
        self.model.dados['total_liquido'] = self.model.dados['total_liquido'] + dados['total_liquido']
        self.model.dados['total_items'] = self.model.dados['total_items'] + dados['quantidade']

    def adicionar_item(self):
        item = self.criar_df_item()
        if item is not False:
            self.model.adicionar_item(item)
            self.inserir_valores_totais(item)
            self.table = TabelaVenda(self.view.table, self.model.get_items_venda(), self.db)
            self.table.preencher_tabela()
            self.view.input_descricao.setCurrentIndex(0)
            self.definir_qnt()
            self.definir_totais()
            self.limpar()
        else:
            mensagem('Preencha todos os campos!', QMessageBox.Information, 'Erro')

    def criar_df_item(self):
        try:
            dados = self.db.select(f"""SELECT * FROM estoque WHERE descricao = '{self.view.campo_produto}'""")
            if self.view.campo_tamanho != '' and self.view.campo_cor != '':
                return pd.Series({
                    'codigo': dados['cod_barras'].values[0],
                    'descricao': dados['descricao'].values[0],
                    'uni': dados['unidade'].values[0],
                    'quantidade': converter_string_int(self.view.campo_quantidade),
                    'tamanho': self.view.campo_tamanho,
                    'cor': self.view.campo_cor,
                    'preco_venda': limpar_dinheiro(self.view.campo_preco),
                    'perc_desconto': limpar_porcento(self.view.campo_perc_desconto),
                    'valor_desconto': limpar_dinheiro(self.view.campo_val_desconto),
                    'total_bruto': converter_string_int(self.view.campo_quantidade) * limpar_dinheiro(
                        self.view.campo_preco),
                    'total_liquido': limpar_dinheiro(self.view.campo_total)
                })
            else:
                return False
        except IndexError:
            return False


    def valor_desconto(self):
        pass

    def definir_totais(self):
        self.view.input_totalBruto.setText(moeda(self.model.dados['total_bruto']))
        self.view.input_desconto.setText(moeda(self.model.dados['desconto']))
        self.view.input_totalLiquido.setText(moeda(self.model.dados['total_liquido']))
        self.view.input_totalItem.setText(f"{self.model.dados['total_items']}")
        self.view.input_totalPago.setText(moeda(0))
        self.view.input_troco.setText(moeda(0))

    def nr_venda(self):
        nr = self.db.select('SELECT * FROM vendas ORDER BY codigo DESC LIMIT 1')
        if nr.empty is True:
            nr = 1
        else:
            nr = nr.iloc[0, 1] + 1
        return nr

    def editar(self):
        objeto = self.table.retorna_objeto(self.view.linha_selecionada())
        self.modelEdit = VendasModel(self.db, objeto, 'vendas')
        self.modelEdit.carregar_items_venda()
        self.modelEdit.nome_cliente()
        table = TabelaVendaEdit(self.edit.table, self.modelEdit.items_venda, self.db)
        table.preencher_tabela()
        self.edit.limpar()
        self.edit.preencher_campos(self.modelEdit.dados, self.db)
        self.edit.show()
