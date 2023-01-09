"""
Operador lógico not
Ele nega a expressão
not True = False
not False = True
"""

#idade = input('Idade: ')
idade = ''

# vazio é avaliado como falsy
if not idade:
    print('Você não digitou nada')

print(not True)
print(not False)
