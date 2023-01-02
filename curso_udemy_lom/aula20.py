"""
São considerados falsy:
0   0.0 ''
Também existe um tipo None
None é considerado um não valor

Operadores lógicos
and (e)     or (ou)     not (não)
and - todas as condições são verdadeiras

entrada = input('[E]ntrar ou [S]air? ')
senha_digitada = input('Senha: ')
senha_permitida = '1234'

if entrada.upper() == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
elif entrada.upper() == 'S' and senha_digitada == senha_permitida:
    print('Sair')
else:
    print('Comando inválido')
"""

# Avaliação de curto circuito
# A avaliação para quando a condição atinge o primeiro falsy e retorna esse valor
print(True and True and False and True)
print(True and True and 0 and True)
print(True and True and 0.0 and True)
print(True and True and '' and True)
