"""
Introdução ao empacotamento e desempacotamento + tuples (tuplas)
"""
lista = ['Maria', 'José', 'Tereza']

# desempacotar a lista em variaveis para cada elemento
nome_1, nome_2, nome_3 = lista
print(nome_2)

# para desempacotar somente algum elemento da lista
nome, *_ = lista
print(nome)
_, nome, *_ = lista
print(nome)

"""
A tuple é basicamente uma lista imutável
"""
tupla = ('Maria', 'José', 'Tereza')
print(tupla, type(tupla))

# coerção de lista para tupla
tupla = tuple(lista)
print(tupla, type(tupla))
