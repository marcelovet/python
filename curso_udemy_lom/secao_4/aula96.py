# Exercicio - unir listas
# crie uma funcao zipper (como o zipper de roupas)
# o trabalho dessa funcao sera unir duas listas em ordem
# use todos os valores da menor lista
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
from itertools import zip_longest


def zipper(lista1, lista2):
    intervalo_maximo = min(len(lista1), len(lista2))
    return [
        (lista1[i], lista2[i])
        for i in range(intervalo_maximo)
    ]


l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(l1, l2))

# o python tem uma funcao que faz isso - zip()
print(list(zip(l1, l2)))

# e o modelo itertools tem uma funcao para considerar a lista maior
print(list(zip_longest(l1, l2, fillvalue='Sem cidade')))
