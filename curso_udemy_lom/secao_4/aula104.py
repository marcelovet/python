# Funcoes recursivas e recursividade
# - funcoes que podem se chamar de volta
# - uteis para dividir problemas grandes em partes menores
# Toda funcao recursiva deve ter:
# - um problema que possa ser dividido em partes menores
# - um caso recursivo que resolve o pequeno problema
# - um caso base que para a recursao
# - fatorial - n! = 5 * 4 * 3 *2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm
# import sys
# sys.setrecursionlimit(1004) # limite de recursao padrao do python é 1000
# def recursiva(start=0, end=4):
#     # caso base
#     if start >= end:
#         return end
#     # caso resursivo - contar até chegar ao final
#     print(start, end)
#     start += 1
#     return recursiva(start, end)
# recursiva(0, 1000)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(2))
print(factorial(5))