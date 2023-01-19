# @property - é um getter no modo pythonico
# getter - é um metodo para obter um atributo
# @property é uma propriedade do objeto, um metodo que se comporta como um atributo
# geralmente usado nas seguintes situações:
# - como getter
# - evitar quebrar o codigo cliente
# - habilitar um setter
# - executar ações ao obter um atributo
# Codigo cliente - é o codigo que utilizará o codigo da classe
# class Caneta:
#     def __init__(self, cor):
#         self.cor = cor
# # se o atributo cor mudasse de nome, o codigo cliente quebraria
# caneta = Caneta('Azul')
# print(caneta.cor)

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    # essa seria um modo de poder mudar atributos da instancia sem quebrar o codigo cliente
    # mas ainda comportaria como metodo
    def get_cor(self):
        return self.cor_tinta

    # permite alterar o nome do atributo da instancia
    # e ainda manter o atributo anterior, pois esse metodo comporta como atributo
    @property
    def cor(self):
        return self.cor_tinta


caneta = Caneta('Azul')
print(caneta.get_cor())
print(caneta.cor)
