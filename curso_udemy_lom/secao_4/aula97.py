"""
considerando duas listas de inteiros ou floats (lista_a e lista_b)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma vai considerar a menor lista
Ex.:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4, 5]
resultado
[2, 4, 6, 8, 10]
"""
from itertools import zip_longest

def soma_listas(lista_a, lista_b):
    intervalo = min(len(lista_a), len(lista_b))

    return [
        lista_a[i] + lista_b[i]
        for i in range(intervalo)
    ]

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4, 5]

print(soma_listas(lista_a, lista_b))

# ou ainda mais facil
lista_da_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_da_soma)

# se eu quiser usar a maior, definindo um fill padrao
lista_da_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_da_soma)
