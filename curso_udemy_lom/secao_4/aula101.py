from functools import partial
from types import GeneratorType

# map - mapeamento de dados
def print_iter(iterator):
    print(*list(iterator), sep='\n', end='\n\n')

# partial é função que retorna uma closure
def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# novos_produtos = [
#     {**p, 'preco': aumentar_dez_porcento(p['preco'])} for p in produtos
# ]
# o mesmo com o map()
def muda_preco_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(produto['preco'])
    }

novos_produtos = map(
    muda_preco_produtos,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos) # map cria um iterator
print(hasattr(novos_produtos, '__iter__'))
print(hasattr(novos_produtos, '__next__'))
print(isinstance(novos_produtos, GeneratorType))

# entao para ter ele como na list comprehension, faço a conversao
novos_produtos = list(map(
    muda_preco_produtos,
    produtos
))
print(novos_produtos)
print(hasattr(novos_produtos, '__iter__'))
print(hasattr(novos_produtos, '__next__'))
print(isinstance(novos_produtos, GeneratorType))
