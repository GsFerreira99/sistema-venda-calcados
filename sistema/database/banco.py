from sqlalchemy import create_engine, text
import pandas as pd
import mysql.connector


class DataBase:

    _db: mysql.connector.connect
    _engine: create_engine
    _cursor: None

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
            self.tabela_fornecedor()
            self.tabela_estoque()
            self.tabela_usuario()
            self.tabela_cliente()
            self.tabela_vendas()
            self.tabela_item_venda()
        except mysql.connector.errors.ProgrammingError as e:
            return e
        return "Tabelas criadas com sucesso."

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
    
    def tabela_cliente(self):
        self._cursor.execute("""CREATE TABLE cliente (
                id INT AUTO_INCREMENT PRIMARY KEY,
                criado_em DATE NOT NULL,
                nome VARCHAR(255) NOT NULL,
                celular VARCHAR(11),
                telefone VARCHAR(11),
                cpf_cnpj VARCHAR(14) NOT NULL,
                inscricao_estadual VARCHAR(14),
                nascimento DATE,
                email VARCHAR(50),
                cep VARCHAR(8),
                endereco VARCHAR(255),
                complemento VARCHAR(255),
                bairro VARCHAR(255),
                cidade VARCHAR(255),
                uf VARCHAR(2),
                observacao VARCHAR(255)
                )""")

    def tabela_vendas(self):
        self._cursor.execute("""CREATE TABLE vendas (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        data_venda DATE NOT NULL,
                        cliente INT,
                        CONSTRAINT FK_Cliente FOREIGN KEY (cliente)
                        REFERENCES cliente(id),
                        total_bruto FLOAT,
                        desconto FLOAT,
                        total_liquido FLOAT,
                        total_items INT,
                        total_pago FLOAT,
                        troco FLOAT
                        )""")

    def tabela_item_venda(self):
        self._cursor.execute("""CREATE TABLE item_venda (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                venda INT,
                                CONSTRAINT FK_Venda FOREIGN KEY (venda)
                                REFERENCES vendas(id),
                                produto INT,
                                CONSTRAINT FK_Produto FOREIGN KEY (produto)
                                REFERENCES estoque(id),
                                preco FLOAT,
                                quantidade FLOAT,
                                percent_desconto FLOAT,
                                valor_desconto FLOAT,
                                total_bruto FLOAT,
                                total_liquido FLOAT
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
        return pd.read_sql(text(sql), con=self._engine)

    def deletar(self, sql):
        try:
            self._cursor.execute(sql)
            self._db.commit()
            return True
        except mysql.connector.Error as e:
            print(e)
            return False

    def pesquisar(self, campo: str, tabela: str, sql: str):
        """ exemplo: campo='Gabriel', tabela='clientes', sql='SELECT * FROM clientes WHERE nome LIKE '%Gabriel%' """
        if campo == '':
            select = pd.read_sql(text(f"SELECT * FROM {tabela}"), con=self._engine)
        else:
            select = pd.read_sql(text(sql), con=self._engine)
        return select

    def atualizar(self, sql):
        try:
            self._cursor.execute(sql)
            self._db.commit()
            return True
        except mysql.connector.Error as e:
            print(e)
            return False
