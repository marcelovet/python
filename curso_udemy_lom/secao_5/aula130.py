# Heranca multipla - POO do python
# No python uma classe pode estender varias outras classes
# Heranca simples
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Heranca multipla e mixins
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)
# Python 3 usa C3 superclass linearization para gerar o mro
# https://en.wikipedia.org/wiki/C3_linearization
# Para saber a ordem de chamada dos metodos use Classe.mro()
# ou o atributo __mro__
# Pode gerar o problema de diamante
# A, B, C, D
# D(B, C) - B(A) - C(A) - A
#       A
#     /   \
#    B     C
#     \   /
#       D
class A:
    ...

    def quem_sou(self):
        print('A')


class B(A):
    ...

    def quem_sou(self):
        print('B')


class C(A):
    ...

    def quem_sou(self):
        print('C')


class D(B, C):
    ...

    # def quem_sou(self):
    #     print('D')


d = D()
d.quem_sou()
# print(D.mro())
print('Ordem de busca, resolucao, do metodo (verificado com o mro()):')
print(*D.__mro__, sep='| --> |')
