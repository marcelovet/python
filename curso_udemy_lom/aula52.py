"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
condicao = 10 == 11
variavel = 'Valor' if condicao else 'Outro valor'

print(variavel)

# outro exemplo
digito = 9
nvo_digito = digito if digito <= 9 else 0

print(nvo_digito)

print('Valor' if False else 'Outro valor' if False else 'Fim')
