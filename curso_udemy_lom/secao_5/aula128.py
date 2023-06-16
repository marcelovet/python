# Heranca simples - relacoes entre classes
# Associacao - usa, Agregacao - tem, Composicao - é dono de, Heranca - É um

# Heranca vs Composicao

# Classe pricipal (Pessoa)
# -> super class, base class, parent class
# Classes filhas (Cliente)
# -> sub class, child class, derived class
# toda class ja tem uma heranca de object
class Pessoa:
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('class Pessoa')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    # seguindo o method resolution order (MRO)
    # ele vai encontrar esse metodo aqui e nao vai executar o de
    # mesmo nome em Pessoa
    def falar_nome_classe(self):
        print('class Cliente')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa):
    cpf = 'cpf do aluno'
    ...


c1 = Cliente('Fulano', 'de Tal')
a1 = Aluno('Sicrano', 'de Tal')

c1.falar_nome_classe()
a1.falar_nome_classe()
print(c1.cpf)
print(a1.cpf)
# heranca de 3 niveis = OK, mais que isso a complexidade começa a ser muito
# grande
