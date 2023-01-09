"""
Operadores lógicos
and (e)     or (ou)     not (não)
or - pelo menos uma das condições são verdadeiras
entrada = input('[E]ntrar ou [S]air? ')
senha_digitada = input('Senha: ')
senha_permitida = '1234'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
elif (entrada == 'S' or entrada == 's') and senha_digitada == senha_permitida:
    print('Sair')
else:
    print('Comando inválido')
"""

# Avaliação de curto circuito
# A avaliação para quando a condição atinge o primeiro falsy e retorna esse valor
print(True or False)
print(False or 1 or True)
print(False or 'ab' or True)
idade = input('Idade: ') or 'Você não digitou sua idade'

print(idade)
