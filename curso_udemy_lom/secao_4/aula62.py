"""
Exercícios com funções

Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável

Crie um função que fala se um numero é par ou impar
retorne se o numero é par ou impar
"""

def multiplica(*args):
    produto = 1
    for numero in args:
        produto *= numero
    return produto

print(1*2*3*4)
print(multiplica(1, 2, 3, 4))

def verifica_par(x):
    par = x % 2 == 0
    if par:
        return f'{x} é um valor par'
    return f'{x} é um valor ímpar'

print(verifica_par(1))
print(verifica_par(2))
print(verifica_par(11))
print(verifica_par(46))
