"""
enumerate - enumera iteráveis (índices)
"""
lista = ['Maria', 'José', 'Tereza']
lista_enumerada = list(enumerate(lista))

# isso funciona como um for dentro de outro for
for indice, nome in enumerate(lista):
    print(f'Para o índice {indice} temos {nome}')

for item in enumerate(lista):
    for valor in item:
        print(valor)

print(lista_enumerada)
