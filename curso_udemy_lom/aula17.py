"""
Operações condicionais
if / elif / else (se, se não se, se não)
if pode ser usado sozinho
elif e else precisam de um if
else é sempre a última condição
"""

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição satisfeita')

print('Este é o código fora do if')
