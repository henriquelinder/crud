import sqlite3

class PessoaDB():
    banco = "pessoas.db"
    conn = None
    cur = None
    conectado = False

    def conectar(self):
        self.conn = sqlite3.connect(self.banco)
        self.cur = self.conn.cursor()
        self.conectado = True

    def desconectar(self):
        self.conn.close
        self.conectado = False

    def executar(self, sql, param = None):
        if self.conectado:
            if param == None:
                self.cur.execute(sql)
            else:
                self.cur.execute(sql,param)
            return True
        else:
            return False

    def fetchall(self):
        return self.cur.fetchall()

    def persistir(self):
        if self.conectado:
            self.conn.commit()
            return True
        else:
            return False

def iniciarBD():
    transacao = PessoaDB()
    transacao.conectar()
    transacao.executar("CREATE TABLE IF NOT EXISTS pessoa (id INTEGER PRIMARY KEY, nome TEXT, pai TEXT, mae TEXT, "
                        "idade INTEGER, endereco TEXT)")
    transacao.persistir()
    transacao.desconectar()

iniciarBD()