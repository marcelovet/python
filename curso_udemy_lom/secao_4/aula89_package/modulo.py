# __all__ define o que vai ser chamado ao usar o from modulo import *
# por padrão vai ser tudo que há no modulo
# __all__ = [
#     'soma_do_modulo'
# ]
from aula89_package.modulo_b import fala_oi

variavel = 'variavel'

def soma_do_modulo(x, y):
    return x + y

#fala_oi()
