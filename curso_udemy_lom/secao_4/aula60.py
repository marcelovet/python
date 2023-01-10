"""
args - argumentos nao nomeados
* - *args (empacotamento e desempacotamento)
"""
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

#def soma(x, y):
#    return x + y

def soma(*args):
    total = 0
    for num in args:
        print(f'Valor atual = {total}, some com {num}')
        total += num
    return(total)

print(soma(1, 2, 3, 4, 5))