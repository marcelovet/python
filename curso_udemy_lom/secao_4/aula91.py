# Exercicio - adiando execucao de funcoes
# Com closure nas funcoes de soma e de multiplicacao
# def executa(funcao, *args):
#     return funcao(*args)

# def soma(y):
#     def somador(x):
#         return x + y
#     return somador

# def multiplica(y):
#     def multiplicador(x):
#         return x * y
#     return multiplicador

# soma_com_cinco = executa(soma, 5)
# multiplica_por_dez = executa(multiplica, 10)

# print(soma_com_cinco(1))
# print(multiplica_por_dez(1))
# ou
# Com closure na funcao que executa as demais
def executa(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

soma_com_cinco = executa(soma, 5)
multiplica_por_dez = executa(multiplica, 10)

print(soma_com_cinco(1))
print(multiplica_por_dez(1))
