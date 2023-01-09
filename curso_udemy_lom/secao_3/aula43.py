# for para listas
lista = ['Maria', 'José', 'Tereza']

for nome in lista:
    print(nome)

"""
Exiba os índices dessa lista
"""
idx = 0

for nome in lista:
    print(idx, nome)
    idx += 1

# ou
indices = range(len(lista))

for i in indices:
    print(i, lista[i])
