# reduce - faz a reducao de um iteravel em um valor
from functools import reduce

def print_iter(iterator):
    print(*list(iterator), sep='\n', end='\n\n')


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

total = 0

for p in produtos:
    total += p['preco']

total = round(total, 2)

print(total)

# ou ainda usando list comprehension
total = sum([
    p['preco'] for p in produtos
])

total = round(total, 2)

print(total)

def funcao_do_reduce(acumulador, produto):
    # print(acumulador)
    # print(produto)
    return acumulador + produto['preco']

# com reduce
total = reduce(
    funcao_do_reduce,
    produtos,
    0 # valor inicial
)

print(round(total, 2))

# com lambda
total = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0 # valor inicial
)

print(round(total, 2))
