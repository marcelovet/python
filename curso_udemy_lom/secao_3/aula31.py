"""
Faça um programa que peça ao usuário para digitar um numero inteiro,
informe se este numero é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um inteiro.
"""
numero_str = input('Digite um número inteiro: ')

try:
    numero_int = int(numero_str)
    if numero_int % 2 == 0:
        print('Seu número é par')
    else:
        print('Seu número é ímpar')
except:
    print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte ao usuario a hora e, baseando-se no horário descrito,
exiba a saudação apropriada. Ex.: Bom dia (0-11), Boa tarde (12-17), Boa noite (18-23)
"""

hora_informada = input('Informe a hora atual: ')

try:
    hora_int = int(hora_informada)
    hora_dia = hora_int >= 0 and hora_int <= 11
    hora_tarde = hora_int >= 12 and hora_int <= 17

    if hora_dia:
        print('Bom dia')
    elif hora_tarde:
        print('Boa tarde')
    elif hora_int > 23:
        print('Não conheço essa hora')
    else:
        print('Boa noite')
except:
    print('Você não digitou uma hora')

"""
Faça um programa que peça ao usuário o primeiro nome. Se o nome tiver 4 letras ou menos,
exiba 'Seu nome é curto'; entre 5 e 6 letras, 'Seu nome é normal'; maior que 6 'Seu nome é muito grande'
"""
nome_informado = input('Digite o seu primeiro nome: ')
comprimento_nome = len(nome_informado)
nome_curto = comprimento_nome <= 4
nome_grande = comprimento_nome > 6

if not nome_informado:
    print('Você não informou seu nome')
elif nome_curto:
    print('Seu nome é curto')
elif nome_grande:
    print('Seu nome é muito grande')
else:
    print('Seu nome é normal')
