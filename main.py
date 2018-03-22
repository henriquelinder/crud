from pessoa import Pessoa
import pessoa_db

#pessoa1 = Pessoa("Cesar","Cesar Augusto Linder","Marlene Aparecida Andrade",27,"Rua Bittencourt Sampaio")
try:
    pessoa1 = Pessoa(input("Digite o nome: "),input("Digite o nome do pai: "),input("Digite o nome da mãe: "),int(input("Digite a idade: ")), input("Digite o endereço: "))
    print("O nome da pessoa é: "+pessoa1.nome)
    pessoa1.mandarSeFoder()
    pessoa1.salvaPessoa()
except ValueError as v:
    print("Deu erro, seu burro! A descrição do erro é:  "+v.__str__())
finally:
    exit(1)
