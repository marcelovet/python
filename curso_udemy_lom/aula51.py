"""
Desempacotamento em chamadas
de métodos e funções
"""
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, ['Maria', 'Helena', 1, 2, 3, 'Eduarda'], 'Eduarda']
tupla = ('Python', 'é', 'legal')

p, b, *_, ap, u = lista
print(p, u)

# exemplo de desempacotamento em chamada
print(*string)
print(*lista)
print(*tupla)
