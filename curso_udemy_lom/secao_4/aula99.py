# Combinations, permutations e products - itertools
# combinação - orndem não importa, iteravel + tamanho do grupo
# permutacao - ordem importa
# produto - ordem importa e repete valores unicos
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n', end='\n\n')

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino']
]


# print_iter(combinations(pessoas, 2))

# print_iter(permutations(pessoas, 2))
# print_iter(product(*camisetas))

lista_de_camisetas = [
    {'cor': cor, 'tamanho': tamanho, 'genero': genero}
    for cor, tamanho, genero in product(*camisetas)
]

print(*lista_de_camisetas, sep='\n', end='\n\n')