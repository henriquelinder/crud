from pessoa_db import *

class Pessoa:

    def __init__(self, nome: str, pai: str, mae: str, idade: int, endereco: str):
        self.nome = nome
        self.pai = pai
        self.mae = mae
        self.idade = idade
        self.endereco = endereco

    def mandarSeFoder(self):
        print("VAI SE FODER, "+self.nome)

    def salvaPessoa(self):
        print("entrando")
        transacao = PessoaDB()
        print("conectar...")
        transacao.conectar()
        print("executar...")
        #transacao.executar("CREATE TABLE IF NOT EXISTS teste (id INTEGER PRIMARY KEY)")
        transacao.executar("INSERT INTO pessoa VALUES (NULL,?,?,?,?,?)",(self.nome,self.pai,self.mae,self.idade,self.endereco))
        print("persistir...")
        transacao.persistir()
        transacao.desconectar()

