# list comprehension em Python
# list comprehension é uma forma rapida de criar listas a partir de iteraveis
# print(list(range(10)))
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=60)

# list comprehension
lista = [numero for numero in range(10)]
print(lista)

lista = [numero * 2 for numero in range(10)]
print(lista)

# o interessante é que posso utilizar para fazer um copia disvinculada de de outra lista
lista = [1, 2, 3, 4]
nova_lista = [numero for numero in lista]
lista[0] = 12

print(lista, nova_lista, sep='\n', end=f'\n{10 * "-"}\n\n')

# mapeamento de dados em list comprehension
# no mapeamento, a lista deve ter o mesmo tamanho da anterior
produtos = [
    {'nome': 'p1', 'preco': 20, 'modelo': 'abx'},
    {'nome': 'p2', 'preco': 30, 'modelo': 'abx'},
    {'nome': 'p3', 'preco': 40, 'modelo': 'bcx'},
    {'nome': 'p4', 'preco': 10, 'modelo': 'bcx'},
    {'nome': 'p5', 'preco': 55, 'modelo': 'bcx'},
]

# vou aumentar o valor de cada produto em 5% se seu valor for superior a 20
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

p(novos_produtos)

# filtro em list comprehension
# de 0 a 9, os valores menores que 5
lista = [n for n in range(10) if n < 5]
print(lista)

# mesma regra do anterior, porem somente de modelos bcx
# Importante! ele filtra primeiro antes do mapeamento
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto} # mapeamento
    for produto in produtos
    if produto['modelo'] == 'bcx' # filtro
]

p(novos_produtos)

# list comprehension com mais de um for
lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
print(lista)

lista = [
    (x, y)
    for x in range(3)    
    for y in range(3)    
]
print(lista)
