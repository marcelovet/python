# atributos de classe
class Pessoa:
    # atributo da classe
    ano_atual = 2022

    # atributo da instancia
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('João', 35)
p2 = Pessoa('Maria', 26)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
Pessoa.ano_atual = 1980
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
