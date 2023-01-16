# Exercicios
# Aumente o preço dos produtos em 10%
# gere novos_produtos por deep copy
# ordene os produtos por nome descrescente
# gere produtos_ordenados_por_nome por deep copy
# ordene os produtos por preço crescente
# gere produtos_ordenados_por_preco por deep copy
from aula90_pkg import produtos
import copy

def mostra_listas(l1, l2):
    print(*l1, sep='\n', end='\n\n')
    print(*l2, sep='\n', end='\n\n')

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]
mostra_listas(produtos, novos_produtos)

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)
mostra_listas(produtos, produtos_ordenados_por_nome)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco'],
    reverse=False
)
mostra_listas(produtos, produtos_ordenados_por_preco)
