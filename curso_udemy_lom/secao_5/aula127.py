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

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

    def resumir_carro(self):
        tem_fabricante = self._fabricante is not None
        tem_motor = self._motor is not None

        if tem_fabricante and tem_motor:
            return print(
                f'Nome do carro: {self.nome}\nFabricante: {self._fabricante.nome}\nMotor: {self._motor.nome}', end='\n\n')
        elif tem_fabricante and not tem_motor:
            return print(
                f'Nome do carro: {self.nome}\nFabricante: {self._fabricante.nome}\nMotor: indefinido', end='\n\n')
        elif not tem_fabricante and tem_motor:
            return print(
                f'Nome do carro: {self.nome}\nFabricante: indefinido\nMotor: {self._motor.nome}', end='\n\n')
        return print(
            f'Nome do carro: {self.nome}\nFabricante: indefinido\nMotor: indefinido', end='\n\n')


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

c1.fabricante = f1
c1.motor = m1
print('------Depois de definir fabricante e motor')
c1.resumir_carro()

c1.fabricante = f2
c1.motor = m2
print('------Alterando fabricante e motor')
c1.resumir_carro()

c2 = Carro('Carro 2')
c2.fabricante = f1
c2.motor = m2
c2.resumir_carro()
