"""
Argumentos nomeados e não nomeados em python
argumento nomeado tem nome com sinal de igual
argumento não nomeado recebe apenas o argumento (valor)
"""
def soma(x, y, z, t=2):
    print(f'{x=} {y=} {z=} {t=}', '|', x + y + z + t)

soma(1, 2, 3) # quando não nomeado, deve seguir a posicao
soma(y=2, x=1, z=3) # se nomeado, não importa a ordem
soma(2, y=1, z=3) # se nomear, os demais precisam ser nomeados, a não ser que já tenham um padrão