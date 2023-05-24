"""
interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
"""
nome1 = 'Luiz'
nome2 = 'ze'
preco = 1000.95897643
variavel = '%s e %s, o preço é R$%.2f' % (nome1, nome2, preco)

print(variavel)
print('O hexadecimal de %d é %06x' % (15, 15))
