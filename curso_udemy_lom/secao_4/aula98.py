# count - um iterador sem fim
from itertools import count

c1 = count() # nele só vai vir o start e o step
r1 = range(10) # nao tem metodo next

# a cada next, será adicionado um step
print(next(c1))
print(next(c1))

for i in c1:
    if i > 5:
        break
    print(i, 'dentro do for')

for i in r1:
    print(i, 'dentro do for i')

for a in r1:
    print(a, 'dentro do for a')