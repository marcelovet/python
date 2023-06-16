# ORIENTACAO A OBJETOS
# class - classes sao moldes para criar novos objetos (instancias) que
# podem ter seus proprios atributos e metodos
# Os objetos gerados pela classe podem usar seus dados internos para realizar
# varias acoes
# Por convencao, usamos PascalCase para nomes de classes
# string = 'Luiz'  # uma instancia da classe str
# print(string.upper())  # upper é um metodo aceito para a classe str
# cria uma classe
# class Pessoa:
#     ...
# p1 = Pessoa()
# p1.nome = 'luiz'
# p1.sobrenome = 'otavio'
# print(p1.nome)


class Pessoa:
    # __init__ inicializa os atributos e self indica o proprio objeto
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('luiz', 'otavio')
print(p1.nome, p1.sobrenome)
