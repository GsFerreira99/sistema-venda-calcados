from sistema.relatorios.base_pdf import Pdf
from sistema.funcoes.genericos import cpf_cnpj, data, celular, moeda, mascara_porcento
from datetime import datetime
from sistema.database.banco import DataBase
import random


def dados_estoque():
    db = DataBase('localhost', 'gabriel', 'Gabriel151299', '3306')
    db.conectar()

    forcedores = db.select("SELECT id, nome FROM fornecedor")
    dados = {}
    for index, fornecedor  in forcedores.iterrows():
        id = fornecedor['id']
        dados[fornecedor['nome']] = db.select(f"SELECT * FROM estoque WHERE fornecedorId = {id}")

    return dados

def seed():
    db = DataBase('localhost', 'gabriel', 'Gabriel151299', '3306')
    db.conectar()

    for i in range(20):

        produto = 'TÊNIS '+str(i + 1)

        db.inserir("""
            INSERT INTO estoque ( 
            cod_barras, 
            descricao, 
            fornecedorId, 
            unidade, 
            preco_compra, 
            margem, 
            lucro, 
            preco_venda, 
            preco_atacado, 
            observacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (random.randint(1111111111111, 9999999999999), produto, 3, 'UNI', random.randint(10, 100), 0, 0, 0, 0, ''))

class RelatorioEstoque:

    def __init__(self, caminho):
        self.pdf = Pdf(caminho)

        self.pdf.set_titulo(caminho)
        self.registrar_fontes()

    def registrar_fontes(self):
        self.pdf.registrar_font('Franklin Gothic Book Regular',
                                'sistema/relatorios/fonts/Franklin Gothic Book Regular.ttf')
        self.pdf.registrar_font('Cambria', 'sistema/relatorios/fonts/Cambria.ttf')
        self.pdf.registrar_font('Cambria-Bold', 'sistema/relatorios/fonts/Cambria-Bold.ttf')

    def escrever(self, dados):
        self.cabecalho()
        self.escrever_dados(dados)
        self.pdf.salvar()

    def cabecalho(self, titulo='RELAÇÃO DE PRODUTOS CADASTRADOS'):
        self.pdf.set_font(font='Franklin Gothic Book Regular', tamanho=12)
        self.pdf.string(200, 820, 'F PESSOAS BESERRA - ERIVALDO CEARA')
        self.pdf.string(275, 805, 'Endereço:')
        self.pdf.string(125, 790, 'CNPJ:08.963.172/0001-72 CEP:63704-560 - PONTE PRETA - Crateús/CE')
        self.pdf.string(200, 775, 'Fone: (88) 99231-2220 - (88) 9 9654-6363')

        self.pdf.set_font(font='Cambria-Bold', tamanho=16)
        self.pdf.string(155, 750, titulo)


    def escrever_dados(self, items):
        y = 700
        total = 0

        for key, value in items.items():
            self.pdf.set_font(font='Cambria', tamanho=12)
            self.pdf.string(255, y, key)

            y -= 15
            self.pdf.can.line(20, y+10, 570, y+10)

            self.pdf.set_font(font='Cambria-Bold', tamanho=10)
            self.pdf.string(25, y, "Código")
            self.pdf.string(140, y, "Descrição do Produto ")
            self.pdf.string(380, y, "Valor C.")
            self.pdf.string(450, y, "Valor V.")
            self.pdf.string(520, y, "Und.")
            y -= 4
            self.pdf.can.line(20, y, 570, y)
            y -= 12



            for index, item in value.iterrows():
                self.pdf.set_font(font='Cambria', tamanho=10)
                self.pdf.string(25, y, f"{item['cod_barras']}")
                self.pdf.string(140, y, f"{item['descricao']}")
                self.pdf.set_font(font='Cambria-Bold', tamanho=10)
                self.pdf.string(380, y, f"R$ {item['preco_compra']}")
                self.pdf.string(450, y, f"R$ {item['preco_venda']}")
                self.pdf.set_font(font='Cambria', tamanho=10)
                self.pdf.string(520, y, f"{item['unidade']}")
                y -= 15


                if y <= 100:
                    self.pdf.can.showPage()
                    y = 775

            if y <= 100:
                self.pdf.can.showPage()
                y = 775
            y -= 30
