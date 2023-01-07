"""
enumerate - enumera iteráveis (índices)
"""
lista = ['Maria', 'José', 'Tereza']
lista_enumerada = list(enumerate(lista))

# isso funciona como um for dentro de outro for
for indice, nome in enumerate(lista):
    print(f'Para o {indice=} temos {nome=}')

"""
enumerate recebe um iterator então se atribuir ele a uma variavel
e utiliza-lo em um for, se tentar usar de novo vai lançar um erro
uma vez que ja percorreu todo o iterator
for item in enumerate(lista):
    for valor in item:
        print(valor)
"""
print(lista_enumerada)
