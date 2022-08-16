class FornecedorModel:

    def __init__(self, db, dados:object) -> None:
        self.__db = db
        self.__dados = dados

    def salvar(self):
        insert = self.__db.inserir(
            """
            INSERT INTO fornecedor (
                nome,
                celular,
                telefone,
                cpf_cnpj,
                inscricao_estadual,
                email,
                cep,
                endereco,
                complemento,
                bairro,
                cidade,
                uf,
                observacao)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, self.__dados.tolist())
        return insert

    def deletar(self):
        pass

    def editar(self):
        pass
    
    def adicionarEstoque(self, valor):
        pass

    def dadosTabela(self):
        pass

    def __str__(self) -> str:
        return self.__dados['nome']