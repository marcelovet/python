"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem ter valores padrão.
Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.
Sempre que um parãmetro tem um valor padrão, os demais também precisarão de valor padrão
Refatorar: editar seu código.
"""
def soma(x, y, z=None): # o None no z como padrão permite enviar ou não o parâmetro
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(1, 2)
soma(3, 5)

soma(3, 5, 6)
