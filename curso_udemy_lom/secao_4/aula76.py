"""
Usos de list comprehension
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

divisao = [numero / 2 for numero in numeros]
multiplicacao = [numero * 2 for numero in numeros]
quadrado = [numero ** 2 for numero in numeros]

print(numeros)
print(divisao)
print(multiplicacao)
print(quadrado)

# dobro daqueles maiores que 5
novos_numeros = [
    numero * 2
    for numero in numeros
    if numero > 5
]

print(novos_numeros)

# numeros cujo dobro é maior que 8

novos_numeros = [
    numero * 2
    for numero in numeros
]

novos_numeros = [
    numero
    for numero in novos_numeros
    if numero > 8
]

print(novos_numeros)

# o dobro se maior que 8, se nao o proprio numero

novos_numeros = [
    numero * 2
    if (numero * 2) > 8 else numero
    for numero in numeros
]

print(novos_numeros)

#
par_de_coord = [
    {'x': 0, 'y': 0},
    {'x': 1, 'y': 1},
    {'x': 2, 'y': 2},
    {'x': 3, 'y': 3},
]

par_em_tupla = [
    (par['x'], par['y'])
    for par in par_de_coord
]
print(par_em_tupla)

novo_par_coord = [
    {'x': par[0], 'y': par[1]}
    for par in par_em_tupla
]
print(novo_par_coord)

lista_ruas = [
    {'rua': 'rua 0'},
    {'rua': 'rua 1'},
    {'rua': 'rua 2'},
    {'rua': 'rua 3'}
]
print(lista_ruas)

lista_rua_coord = [
    {**lista_ruas[i], **novo_par_coord[i], 'elemento': i}
    for i in range(len(lista_ruas))
]
print(lista_rua_coord)

# adicionar caracteres em strings a partir de uma lógica
string = 'Essa é uma string'
num_letras = 2

nova_string = '-'.join([
    string[idx:idx + num_letras]
    for idx in range(0, len(string), num_letras)
])

print(nova_string)

# lista flat a partir de lista dentro de lista
numeros = [[numero, numero ** 2] for numero in range(10)]
flat = [y for x in numeros for y in x]

print(numeros)
print(flat)
