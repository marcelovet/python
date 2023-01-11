"""
Empacotamento e desempacotamento em dicionarios
"""

pessoa = {
    'nome': 'Marcelo',
    'sobrenome': 'Sidas'
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.56 
}

a, b = pessoa.values()
print(a, b)

a, b = pessoa.items()
print(a, b)

(a1, a2), b = pessoa.items()
print(a1, a2, b)

# ** para extrair o dicionario
pessoa_completa = {
    **pessoa, **dados_pessoa, 'outra_chave': 'outro valor'
}

for chave, valor in pessoa_completa.items():
    print(chave, valor)

print()

# arg e kwargs
# kwargs - keyword arguments (argumentos nomeados)
def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados', args)
    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(1, 2, 3, nome='Joana', qlq=123)

print()

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4
}

mostro_argumentos_nomeados(**configuracoes) # desempacota o dict dentro da função como chave=valor
