# Metodos de classe + factories
# Sao metodos on 'self' sera 'cls', ou seja,
# ao inves de receber a instancia no primeiro
# parametro, receberemos a propria classe
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Meu metodo da classe')

    # permite criar factories methods
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)


Pessoa.metodo_de_classe()
p2 = Pessoa.criar_com_50_anos('Fulano')
print(p2.nome, p2.idade)
