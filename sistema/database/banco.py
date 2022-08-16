from sqlalchemy import create_engine
import pandas as pd
import mysql.connector


class DataBase:

    def __init__(self, host, user, password, porta) -> None:
        self._host = host
        self._user = user
        self._porta = porta
        self._password = password

    def conectar(self):
        try:
            self._db = mysql.connector.connect(
                        host=self._host,
                        user=self._user,
                        password=self._password,
                        port=self._porta,
                        database="db_sapatos"
                        )
            self._cursor = self._db.cursor()
            self._engine = create_engine(f'mysql://{self._user}:{self._password}@{self._host}:{self._porta}/db_sapatos')
            return "Conectado com sucesso."
        except mysql.connector.Error as e:
            if e.errno == 1049:
                return self.criar_db()
            else:
                return e

    def criar_db(self):
        db = mysql.connector.connect(
                        host=self._host,
                        user=self._user,
                        port=self._porta,
                        password=self._password,
                        )
        cursor = db.cursor()
        try:
            cursor.execute("CREATE DATABASE db_sapatos")
            self.conectar()
            self.criar_tabelas()
            return 'Banco de Dados criado com sucesso.'
        except mysql.connector.errors.DatabaseError as e:
            return e

    def criar_tabelas(self):
        try:
            self.tabela_estoque()
            self.tabela_usuario()
        except mysql.connector.errors.ProgrammingError as e:
            return e
        return "Tabela 'estoque' criada com sucesso."

    def tabela_estoque(self):
        self._cursor.execute("""CREATE TABLE estoque (
                id INT AUTO_INCREMENT PRIMARY KEY,
                cod_barras VARCHAR(30) UNIQUE,
                descricao VARCHAR(255),
                fornecedorId int,
                CONSTRAINT FK_Fornecedor FOREIGN KEY (fornecedorId)
                REFERENCES fornecedor(id),
                unidade VARCHAR(25),
                preco_compra FLOAT,
                margem FLOAT,
                lucro FLOAT,
                preco_venda FLOAT,
                preco_atacado FLOAT,
                cor VARCHAR(255),
                tamanho INT,
                estoque_atual INT,
                observacao VARCHAR(255)
                )""")

    def tabela_fornecedor(self):
        self._cursor.execute("""CREATE TABLE fornecedor (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                celular VARCHAR(11),
                telefone VARCHAR(11),
                cpf_cnpj VARCHAR(14) NOT NULL,
                inscricao_estadual VARCHAR(14) NOT NULL,
                email VARCHAR(50),
                cep VARCHAR(8),
                endereco VARCHAR(255),
                complemento VARCHAR(255),
                bairro VARCHAR(255),
                cidade VARCHAR(255),
                uf VARCHAR(2),
                observacao VARCHAR(255)
                )""")

    def tabela_usuario(self):
        self._cursor.execute("""CREATE TABLE usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                usuario VARCHAR(100),
                senha VARCHAR(100),
                nome VARCHAR(100),
                sobrenome VARCHAR(100)
                )""")

    def inserir(self, sql, val):
        try:
            self._cursor.execute(sql, val)
            self._db.commit()
            return True
        except mysql.connector.Error as e:
            print(e)
            return False

    def select(self, sql):
        return pd.read_sql(sql, con=self._engine)



sql = """INSERT INTO decretos (
            N_DECRETO,
            DOTACAO_SUPLEMENTADA,
            DOTACAO_ANULADO,
            VALOR_FINANCEIRO,
            VALOR_FISICO_ATUAL_SUPLEMENTADO,
            VALOR_FISICO_ATUAL_ANULADO,
            DATA_ALTERACAO_ORCAMENTARIA,
            NOME_ORGAO_SUPLEMENTADO,
            UNIDADE_SUPLEMENTADO,
            NOME_ORGAO_SUPLEMENTADO2,
            FUCAO_SUPLEMENTADO,
            SUBFUNCAO_SUPLEMENTADO,
            ID_PROGRAMA_SUPLEMENTADO,
            PROGRAMA_SUPLEMENTADO,
            ID_ACAO_SUPLEMENTADO,
            ACAO_SUPLEMENTADO,
            NATUREZA_DA_DESPESA_SUPLEMENTADO,
            FONTE_DE_RECURSO_SUPLEMENTADO,
            NOME_PRODUTO_SUPLEMENTADO,
            ORGAO_ANULADO,
            UNIDADE_ANULADO,
            NOME_ORGAO_ANULADO,
            FUNCAO_ANULADO,
            SUBFUNCAO_ANULADO,
            ID_PROGRAMA_ANULADO,
            PROGRAMA_ANULADO,
            ID_ACAO_ANULADO,
            ACAO_ANULADO,
            NATUREZA_DA_DESPEZA_ANULADA,
            FONTE_DE_RECURSO_ANULADA,
            NOME_PRODUTO_ANULADO,
            OCORRIDO,
            COL_ALERTA,
            DATA_EMAIL_INICIAL,
            EMAIL_INICIAL,
            EMAIL_ENVIADO,
            NOVA_META_FISICA_ANULADO,
            NOVA_META_FISICA_SUPLEMENTADO,
            INSERIDO_METAS,
            ATUALIZADO_NO_SISTEMA,
            DATA_CONTATO_1_ORIGEM,
            CONTATO_1_ORIGEM,
            STATUS_1_ORIGEM,
            DATA_CONTATO_2_ORIGEM,
            CONTATO_2_ORIGEM,
            STATUS_2_ORIGEM,
            DATA_CONTATO_3_ORIGEM,
            CONTATO_3_ORIGEM,
            STATUS_3_ORIGEM,
            DATA_CONTATO_1_DESTINO,
            CONTATO_1_DESTINO,
            STATUS_1_DESTINO,
            DATA_CONTATO_2_DESTINO,
            CONTATO_2_DESTINO,
            STATUS_2_DESTINO,
            DATA_CONTATO_3_DESTINO,
            CONTATO_3_DESTINO,
            STATUS_3_DESTINO
            ) 
            VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""