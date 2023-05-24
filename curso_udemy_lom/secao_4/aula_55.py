"""
Introdução às funções (def) em Python
Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
Por padrão funções python retornam None

Como criar uma função
def nome_da_funcao():
    ...
no exemplo abaixo
num é um argumento
"""


def print_varias_vezes(num=1):
    print(f'Você solicitou {num} prints')
    for i in range(num):
        print(f'Várias vezes: print {i + 1}')


print_varias_vezes()
