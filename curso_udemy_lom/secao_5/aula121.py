# @proporty + @setter
# - como getter
# - evitar quebrar o codigo cliente
# - habilitar um setter
# - executar ações ao obter um atributo
# Atributos que começam com um ou dois underlines
# nao devem ser usados fora da classe
class Caneta:
    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None

    # para escrever um setter eu preciso de uma property
    @property
    def cor(self):
        print('property')
        return self._cor

    @cor.setter
    def cor(self, valor):
        print('Estou no setter:', valor, 'foi declarado')
        # entao aqui posso colocar logicas de validacao
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul')
# getter -> obter o valor
print(caneta.cor)
caneta.cor = 'rosa'
caneta.cor_tampa = 'verde'
print(caneta.cor_tampa)
