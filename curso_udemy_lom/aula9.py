"""
Operadores aritméticos
"""

adicao = 10 + 10
print('Adição: 10 + 10 =', adicao)

subtracao = 10 - 5
print('Subtração: 10 - 5 =', subtracao)

divisao = 10 / 2.2 # sempre retorna float
print('Divisão: 10 / 2.2 =', divisao)

divisao_inteira = 10 // 2.2
print('Divisão inteira: 10 // 2.2 =', divisao_inteira)

modulo = 10 % 2.2 # resto da divisao
print('Resto da divisão (módulo): 10 % 2.2 =', modulo)
print('Uso de módulo para verificar se um número é divisível:')
print('10 é divisível por 8 (10 % 8 == 0)?', 10 % 8 == 0)
print('10 é par (10 % 2 == 0)?', 10 % 2 == 0)
print('3 é ímpar (3 % 2 != 0)?', 3 % 2 != 0)

potencia = 10 ** 2
print('Potência: 10 ** 2 =', potencia)
