"""
Argumentos nomeados e não nomeados em python
argumento nomeado tem nome com sinal de igual
argumento não nomeado recebe apenas o argumento (valor)
"""
def soma(x, y):
    print(f'{x=} {y=}', '|', x + y)

soma(1, 2) # quando não nomeado, deve seguir a posicao
soma(y=2, x=1) # se nomeado, não importa a ordem