# metodos de instancias em classes python
class Carro:
    def __init__(self, nome=None):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')

print(fusca.nome)
fusca.acelerar()
