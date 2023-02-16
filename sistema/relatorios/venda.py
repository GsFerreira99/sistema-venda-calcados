from sistema.relatorios.base_pdf import Pdf
from sistema.funcoes.genericos import cpf_cnpj, data, celular, moeda, mascara_porcento
from datetime import datetime

class RelatorioVenda:

    def __init__(self, caminho):
        self.pdf = Pdf(caminho)

        self.pdf.set_titulo(caminho)
        self.registrar_fontes()

    def registrar_fontes(self):
        self.pdf.registrar_font('Franklin Gothic Book Regular',
                                'sistema/relatorios/fonts/Franklin Gothic Book Regular.ttf')
        self.pdf.registrar_font('Cambria', 'sistema/relatorios/fonts/Cambria.ttf')
        self.pdf.registrar_font('Cambria-Bold', 'sistema/relatorios/fonts/Cambria-Bold.ttf')

    def escrever(self):
        self.cabecalho()
        self.dados_venda({'data': '09/09/2022', 'venda': 234})
        self.endereco_entrega({})
        self.vendas()
        self.pdf.salvar()

    def cabecalho(self, titulo='NOTA VENDAS'):
        self.pdf.set_font(font='Franklin Gothic Book Regular', tamanho=12)
        self.pdf.string(200, 820, 'F PESSOAS BESERRA - ERIVALDO CEARA')
        self.pdf.string(275, 805, 'Endereço:')
        self.pdf.string(125, 790, 'CNPJ:08.963.172/0001-72 CEP:63704-560 - PONTE PRETA - Crateús/CE')
        self.pdf.string(200, 775, 'Fone: (88) 99231-2220 - (88) 9 9654-6363')

        self.pdf.set_font(font='Cambria-Bold', tamanho=16)
        self.pdf.string(255, 750, titulo)

    def cabecalho_vendas_geral(self, periodos):
        self.cabecalho('')
        self.pdf.set_font(font='Cambria-Bold', tamanho=16)
        self.pdf.string(210, 750, 'RELATORIO GERAL VENDAS')
        self.pdf.set_font(font='Cambria', tamanho=10)
        self.pdf.string(220, 730, f'Periodo: {periodos[0].strftime("%d/%m/%Y")} até {periodos[1].strftime("%d/%m/%Y")}')


    def dados_venda(self, dados):
        self.pdf.set_font(font='Cambria-Bold', tamanho=10)
        self.pdf.string(25, 730, "DATA:")
        self.pdf.string(450, 730, "NR. VENDA:")

        self.pdf.set_font(font='Cambria', tamanho=10)
        self.pdf.string(60, 730, f"{dados['data']}")
        self.pdf.string(520, 730, f"{dados['venda']}")

    def endereco_entrega(self, dados):
        self.pdf.set_font(font='Cambria-Bold', tamanho=8)
        self.pdf.string(25, 721, "(ENDEREÇO DE ENTREGA)")

        self.pdf.set_font(font='Cambria-Bold', tamanho=10)
        self.pdf.string(25, 710, "CLIENTE:")
        self.pdf.string(25, 698, "CPF/CNPJ:")
        self.pdf.string(200, 698, "INSC. ESTADUAL:")
        self.pdf.string(25, 686, "END:")
        self.pdf.string(25, 674, "COMPL.:")
        self.pdf.string(25, 662, "BAIRRO:")

        self.pdf.string(170, 662, "CIDADE:")

        self.pdf.set_font(font='Cambria', tamanho=10)
        self.pdf.string(90, 710, f"{dados['nome'][0]}")
        self.pdf.string(100, 698, f"{cpf_cnpj(dados['cpf_cnpj'][0])}")
        self.pdf.string(290, 698, f"{dados['inscricao_estadual'][0]}")
        self.pdf.string(70, 686, f"{dados['endereco'][0]}")
        self.pdf.string(70, 674, f"{dados['complemento'][0]}")
        self.pdf.string(70, 662, f"{dados['bairro'][0]}")
        self.pdf.string(230, 662, f"{dados['cidade'][0]}-{dados['uf'][0]}")

    def items_fornecedor(self):
        pass

    def vendas(self, items, db):
        self.pdf.set_font(font='Cambria-Bold', tamanho=7)
        self.pdf.string(25, 635, "CÓDIGO")
        self.pdf.string(140, 635, "DESCRIÇÃO")
        self.pdf.string(400, 635, "UND")
        self.pdf.string(430, 635, "QTDE")
        self.pdf.string(460, 635, "FORNECEDOR")

        self.pdf.set_font(font='Cambria', tamanho=7)

        y = 620
        total = 0
        if len(items) == 1:
            item = items
            produto = db.select(f'SELECT * FROM estoque WHERE id = {item["produto"][0]}')
            fornecedor = db.select(f'SELECT * FROM fornecedor WHERE id = {produto["fornecedorId"][0]}')
            self.pdf.string(25, y, f"{produto['cod_barras'][0]}")
            self.pdf.string(400, y, f"{produto['unidade'][0]}")
            self.pdf.string(430, y, f"{item['quantidade']}")
            self.pdf.string(460, y, f"{fornecedor['nome'][0]}")
            texto = f"{produto['descricao'][0]} – {item['cor'][0]} – {item['tamanho'][0]}"
            if len(texto) < 85:
                self.pdf.string(80, y, texto)
            else:
                self.pdf.string(80, y, texto[:86])
                y -= 8
                self.pdf.string(80, y, texto[85:])
            total = item['quantidade'][0]

        else:
            for index, item in items.iterrows():
                produto = db.select(f'SELECT * FROM estoque WHERE id = {item["produto"]}')
                fornecedor = db.select(f'SELECT * FROM fornecedor WHERE id = {produto["fornecedorId"][0]}')
                self.pdf.string(25, y, f"{produto['cod_barras'][0]}")
                self.pdf.string(400, y, f"{produto['unidade'][0]}")
                self.pdf.string(430, y, f"{item['quantidade']}")
                self.pdf.string(460, y, f"{fornecedor['nome'][0]}")
                texto = f"{produto['descricao'][0]} – {item['cor']} – {item['tamanho']}"
                if len(texto) < 80:
                    self.pdf.string(80, y, texto)
                else:
                    self.pdf.string(80, y, texto[:81])
                    y -= 8
                    self.pdf.string(80, y, texto[80:])
                y-=10
                total+= item['quantidade']
                if y <= 100:
                    self.pdf.can.showPage()
                    self.pdf.set_font(font='Cambria', tamanho=8)
                    y = 775
        y-=20
        self.pdf.set_font(font='Cambria-Bold', tamanho=7)
        self.pdf.string(25, y, "TOTAL")
        self.pdf.string(500, y, f"{total}")

        self.pdf.set_font(font='Cambria', tamanho=10)

        self.pdf.string(210, y-70, "__________________________________________________________")
        self.pdf.string(270, y-85, "Assinatura do Cliente")

    def vendas_fornecedor(self, items, fornecedor, db):
        self.pdf.set_font(font='Cambria-Bold', tamanho=12)

        self.pdf.string(260, 635, f"{fornecedor}")
        self.pdf.set_font(font='Cambria-Bold', tamanho=7)
        self.pdf.string(25, 615, "CÓDIGO")
        self.pdf.string(140, 615, "DESCRIÇÃO")
        self.pdf.string(400, 615, "UND")
        self.pdf.string(430, 615, "QTDE")
        self.pdf.string(460, 615, "FORNECEDOR")

        self.pdf.set_font(font='Cambria', tamanho=7)

        y = 600
        total = 0

        for item in items:
                produto = db.select(f'SELECT * FROM estoque WHERE id = {item["produto"]}')
                fornecedor = db.select(f'SELECT * FROM fornecedor WHERE id = {produto["fornecedorId"][0]}')
                self.pdf.string(25, y, f"{produto['cod_barras'][0]}")
                self.pdf.string(400, y, f"{produto['unidade'][0]}")
                self.pdf.string(430, y, f"{item['quantidade']}")
                self.pdf.string(460, y, f"{fornecedor['nome'][0]}")
                texto = f"{produto['descricao'][0]} – {item['cor']} – {item['tamanho']}"
                if len(texto) < 80:
                    self.pdf.string(80, y, texto)
                else:
                    self.pdf.string(80, y, texto[:81])
                    y -= 8
                    self.pdf.string(80, y, texto[80:])
                y -= 10
                total += item['quantidade']
                if y <= 100:
                    self.pdf.can.showPage()
                    self.pdf.set_font(font='Cambria', tamanho=8)
                    y = 775
        y -= 20
        self.pdf.set_font(font='Cambria-Bold', tamanho=7)
        self.pdf.string(25, y, "TOTAL")
        self.pdf.string(500, y, f"{total}")

        self.pdf.set_font(font='Cambria', tamanho=10)

        self.pdf.string(210, y - 70, "__________________________________________________________")
        self.pdf.string(270, y - 85, "Assinatura do Cliente")

    def vendas_detalhado(self, items, db):
        self.pdf.set_font(font='Cambria-Bold', tamanho=7)
        self.pdf.string(25, 635, "CÓDIGO")
        self.pdf.string(80, 635, "DESCRIÇÃO")
        self.pdf.string(340, 635, "UND")
        self.pdf.string(360, 635, "R$ UNI.")
        self.pdf.string(400, 635, "QTDE")
        self.pdf.string(420, 635, "SUBTOTAL")
        self.pdf.string(460, 635, "% DESC")
        self.pdf.string(500, 635, "R$ DESC")
        self.pdf.string(540, 635, "TOTAL")

        self.pdf.set_font(font='Cambria', tamanho=7)

        y = 620

        qnt = 0
        bruto = 0
        desc = 0
        total = 0

        if len(items) == 1:
            item = items
            produto = db.select(f'SELECT * FROM estoque WHERE id = {item["produto"][0]}')
            self.pdf.string(25, y, f"{produto['cod_barras'][0]}")
            self.pdf.string(340, y, f"{produto['unidade'][0]}")
            self.pdf.string(360, y, f"{moeda(item['preco'][0])}")
            self.pdf.string(400, y, f"{item['quantidade'][0]}")
            self.pdf.string(420, y, f"{moeda(item['total_bruto'][0])}")
            self.pdf.string(460, y, f"{mascara_porcento(item['percent_desconto'][0])}")
            self.pdf.string(500, y, f"{moeda(item['valor_desconto'][0])}")
            self.pdf.string(540, y, f"{moeda(item['total_liquido'][0])}")
            texto = f"{produto['descricao'][0]} – {item['cor'][0]} – {item['tamanho'][0]}"
            if len(texto) < 65:
                self.pdf.string(80, y, texto)
            else:
                self.pdf.string(80, y, texto[:66])
                self.pdf.string(80, y-10, texto[65:])

        else:
            for index, item in items.iterrows():
                produto = db.select(f'SELECT * FROM estoque WHERE id = {item["produto"]}')
                self.pdf.string(25, y, f"{produto['cod_barras'][0]}")
                self.pdf.string(340, y, f"{produto['unidade'][0]}")
                self.pdf.string(360, y, f"{moeda(item['preco'])}")
                self.pdf.string(400, y, f"{item['quantidade']}")
                self.pdf.string(420, y, f"{moeda(item['total_bruto'])}")
                self.pdf.string(460, y, f"{mascara_porcento(item['percent_desconto'])}")
                self.pdf.string(500, y, f"{moeda(item['valor_desconto'])}")
                self.pdf.string(540, y, f"{moeda(item['total_liquido'])}")
                texto = f"{produto['descricao'][0]} – {item['cor']} – {item['tamanho']}"
                if len(texto) < 65:
                    self.pdf.string(80, y, texto)
                else:
                    self.pdf.string(80, y, texto[:66])
                    y-=8
                    self.pdf.string(80, y, texto[65:])
                y-=10

                qnt += item['quantidade']
                bruto += item['total_bruto']
                desc += item['valor_desconto']
                total += item['total_liquido']

                if y <= 100:
                    self.pdf.can.showPage()
                    self.pdf.set_font(font='Cambria', tamanho=8)
                    y = 775

        y -= 20
        self.pdf.set_font(font='Cambria-Bold', tamanho=7)
        self.pdf.string(25, y, "TOTAL")
        self.pdf.string(400, y, f"{qnt}")
        self.pdf.string(420, y, f"{moeda(bruto)}")
        self.pdf.string(500, y, f"{moeda(desc)}")
        self.pdf.string(540, y, f"{moeda(total)}")

        self.pdf.set_font(font='Cambria', tamanho=10)

        self.pdf.string(210, y-70, "__________________________________________________________")
        self.pdf.string(270, y-85, "Assinatura do Cliente")

    def vendas_geral(self, items):
        self.pdf.set_font(font='Cambria-Bold', tamanho=7)
        self.pdf.string(30, 700, "COD.")
        self.pdf.string(70, 700, "DATA")
        self.pdf.string(120, 700, "CLIENTE")
        self.pdf.string(280, 700, "QTDE ITEMS")
        self.pdf.string(350, 700, "TOTAL BRUTO")
        self.pdf.string(420, 700, "DESCONTO")
        self.pdf.string(490, 700, "TOTAL LIQUIDO")

        self.pdf.set_font(font='Cambria', tamanho=7)

        y = 685
        total_bruto = 0
        desconto = 0
        total_liquido = 0
        total_items = 0
        if len(items) == 1:
            item = items
            self.pdf.string(30, y, f"{item['id'][0]}")
            self.pdf.string(70, y, f"{item['data_venda'][0].strftime('%d/%m/%Y')}")
            self.pdf.string(120, y, f"{item['cliente'][0]}")
            self.pdf.string(280, y, f"{item['total_items'][0]}")
            self.pdf.string(350, y, f"{moeda(item['total_bruto'][0])}")
            self.pdf.string(420, y, f"{moeda(item['desconto'][0])}")
            self.pdf.string(490, y, f"{moeda(item['total_liquido'][0])}")

            total_bruto = item['total_bruto'][0]
            desconto = item['desconto'][0]
            total_liquido = item['total_liquido'][0]
            total_items = item['total_items'][0]


        else:
            for index, item in items.iterrows():
                self.pdf.string(30, y, f"{item['id']}")
                self.pdf.string(70, y, f"{item['data_venda'].strftime('%d/%m/%Y')}")
                self.pdf.string(120, y, f"{item['cliente']}")
                self.pdf.string(280, y, f"{item['total_items']}")
                self.pdf.string(350, y, f"{moeda(item['total_bruto'])}")
                self.pdf.string(420, y, f"{moeda(item['desconto'])}")
                self.pdf.string(490, y, f"{moeda(item['total_liquido'])}")

                y-=10
                total_bruto += item['total_bruto']
                desconto += item['desconto']
                total_liquido += item['total_liquido']
                total_items += item['total_items']

                if y <= 100:
                    self.pdf.can.showPage()
                    self.pdf.set_font(font='Cambria', tamanho=8)
                    y = 775
        y-=20
        self.pdf.set_font(font='Cambria-Bold', tamanho=7)
        self.pdf.string(25, y, "TOTAL")
        self.pdf.string(280, y, f"{total_items}")
        self.pdf.string(350, y, f"{moeda(total_bruto)}")
        self.pdf.string(420, y, f"{moeda(desconto)}")
        self.pdf.string(490, y, f"{moeda(total_liquido)}")




RelatorioVenda('relatorio_venda')
