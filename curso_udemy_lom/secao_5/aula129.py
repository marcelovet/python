# super() é a super class na sub class
# Classe pricipal (Pessoa)
# -> super class, base class, parent class
# Classes filhas (Cliente)
# -> sub class, child class, derived class
class MinhaString(str):
    def upper(self):
        print('Chamou upper')
        return super().upper()


string = MinhaString('fulano')
print(string.upper())


class A:
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, atributo_novo):
        super().__init__(atributo)  # necessario para nao sobrescrever o __init__ de A
        self.atributo_novo = atributo_novo

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        print('Uma execução qualquer')
        super().__init__(*args, **kwargs)  # para receber os atributos dos pais

    def metodo(self):
        # a partir de C procure metodo em seu super, o B
        super(C, self).metodo()
        # a partir de B procure metodo em seu super, o A
        super(B, self).metodo()
        print('C')


c = C('atributo', 'atributo novo')
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()
# print('MRO DAS CLASSES:')
# print('class C', C.mro())
# print('class B', B.mro())
# print('class A', A.mro())
