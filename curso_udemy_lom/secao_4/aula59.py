"""
Retorno de valores de funções (return)
"""
#variavel = print('Luiz')
#print(variavel)

def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y

soma1 = soma(5 , 4)
soma2 = soma(3 , 1)
print(soma1, soma2)
print(soma(11, 3))
