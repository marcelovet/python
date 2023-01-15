# recarregando modulos
# modulos sao singletons, ou seja, ele sao uma instancia unica no python
# se eu tenho dois modulos sendo importados no __main__ e ambos importam outros modulos
# se um desses modulos ja foi importado, ele nao sera importado novamente
import aula87_m
import importlib

# for i in range(10):
#     print(i, end=' ')
#     import aula87_m

for i in range(10):
    print(i, end=' ')
    importlib.reload(aula87_m)
