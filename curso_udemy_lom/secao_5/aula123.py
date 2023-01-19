# UML (unified modelling language) = da para fazer no draw.io
# Relacoes entre classes: associação, agregação, composicao
# Associacao é um tipo de relacao onde os objetos estao ligados dentro do sistema
# Essa é a relacao mais comum entre objetos e tem subconjuntos como agregacao e composicao
# Geralmente, temos uma associacao quando um objeto tem um atributo que referencia outro objeto
# A associacao nao especifica como um objeto controla o ciclo de vida de outro objeto
class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


escritor = Escritor('Luiz')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Maquina de escrever')

print(caneta.escrever())
escritor.ferramenta = caneta
print(escritor.ferramenta.escrever())
escritor.ferramenta = maquina_de_escrever
print(escritor.ferramenta.escrever())
