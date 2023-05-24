# Coletar dados do usuário
# input() sempre capta o dado no tipo str
# print(f'O seu nome é {nome=}') usando o = após o nome da variável ele traz
# o print com a variavel e valor
# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')
# print(f'O seu nome é {nome=}')
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos dois números é: {numero_1 + numero_2}')
