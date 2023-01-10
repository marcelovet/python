"""
args - argumentos nao nomeados
* - *args (empacotamento e desempacotamento)
"""
#x, y, *resto = 1, 2, 3, 4
#print(x, y, resto)

#def soma(x, y):
#    return x + y

def soma(*args):
    total = 0
    for num in args:
        total += num
    return(total)

soma_1_2_3 = soma(*[1, 2, 3]) # * empacote ou desempacota
print(soma_1_2_3)
print(sum([1, 2, 3]))
