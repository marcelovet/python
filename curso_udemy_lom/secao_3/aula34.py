"""
Calculadora com while
Pedir dois numeros e um operador
e realizar a operação
"""
print('Bem vindo à calculadora de burrico')

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Você digitou algo que não é um número')
        continue

    operadores_permitidos = '+-/*'
    operador = input(f"""Digite a operação que quer realizar:
    +: soma
    -: subtração
    /: divisão
    *: multiplicação\nSeu operador: """)

    while (operador not in operadores_permitidos) or not operador:
        operador = input('Você utilizou uma operação inválida. Use um operador permitido!\nDigite seu operador: ')
    while len(operador) > 1:
        operador = input('Você utilizou uma operação inválida. Use somente um operador permitido!\nDigite seu operador: ')

    if operador == '+':
        resultado = numero_1_float + numero_2_float
        print(f'{numero_1_float} + {numero_2_float} = {resultado:.2f}')
    elif operador == '-':
        resultado = numero_1_float - numero_2_float
        print(f'{numero_1_float} - {numero_2_float} = {resultado:.2f}')
    elif operador == '/':
        resultado = numero_1_float / numero_2_float
        print(f'{numero_1_float} / {numero_2_float} = {resultado:.2f}')
    elif operador == '*':
        resultado = numero_1_float * numero_2_float
        print(f'{numero_1_float} * {numero_2_float} = {resultado:.2f}')
    
    # Opção de finalizar a calculadora
    sair = input(f'{"-" * 100}\nQuer sair? [s]im: ')
    sair = sair.lower().startswith('s')
    if sair:
        break

print('Calculadora de burrico finalizada')
