"""
Função lambda em python
A função lambda é uma função anônima que contém apenas uma linha. Ou seja,
tudo deve ser contido dentro de uma única expressão
"""

# lista = [1, 3, 5, 98, 43, 12, 6]
# lista.sort()
# print(lista)
# # sorted(lista) # faz uma shallow copy e ordena

# lista = [1, 3, 5, 98, 43, 12, 6]
# lista.sort(reverse=True)
# print(lista)

# sort vai funcionar em letras ou numeros, mas nao funcionaria em um dict
# entao uma opcao seria passar uma funcao lambda para o sort
lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'José', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Tranqueira'},
    {'nome': 'Manuel', 'sobrenome': 'Bananeira'},
    {'nome': 'Elel', 'sobrenome': 'é um el'},
]

# def ordena(item):
#     return item['nome']
# lista.sort(key=ordena)

# lista.sort(key=lambda item: item['nome']) modifica a original


def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
