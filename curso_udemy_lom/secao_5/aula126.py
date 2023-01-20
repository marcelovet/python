# exercicios com classes
# Crie uma classe Carro (nome)
# Crie uma classe Motor (nome)
# Crie uma classe Fabricante (nome)
# Faca uma ligacao entre carro tem motor, sendo que um motor pode ser de varios carros
# Faca a ligacao entre Carro e Fabricante, sendo que um Fabricante pode fabricar varios carros
# Exiba o nome do carro, motor e fabricantes na tela
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    def inserir_motor(self, motor):
        self._motor = motor.nome

    def inserir_fabricante(self, fabricante):
        self._fabricante = fabricante.nome

    def resumir_carro(self):
        return print(
            f'Nome do carro: {self.nome}\nFabricante: {self._fabricante}\nMotor: {self._motor}')


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


f1 = Fabricante('Fabricante 1')
f2 = Fabricante('Fabricante 2')
m1 = Motor('Motor 1')
m2 = Motor('Motor 2')
c1 = Carro('Carro 1')

print('----Antes de definir fabricante e motor')
c1.resumir_carro()

c1.inserir_fabricante(f1)
c1.inserir_motor(m1)
print('------Depois de definir fabricante e motor')
c1.resumir_carro()

c1.inserir_fabricante(f2)
c1.inserir_motor(m2)
print('------Alterando fabricante e motor')
c1.resumir_carro()
