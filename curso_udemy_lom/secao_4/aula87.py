# Entendendo seus proprios modulos python
# o primeiro modulo executando chama __main__
# você pode importar outro modulo inteiro ou em partes
# o python reconhece a dir onde o modulo __main__ está e as abaixo dela
# mas ele nao reconhece as acima dele por padrao
# python reconhece os modulos e pacotes nos caminhos em sys.path
import aula87_m as mod_87
from aula87_m import variavel_modulo
import sys

print('Este modulo chama', __name__)
print(*sys.path, sep='\n')
print(mod_87.variavel_modulo)
print(variavel_modulo)
