# funcoes decoradoras e decoradores
# decorar = adicionar / remover / restringir / alterar funcoes
# decoradores sao usados para ter funcoes decoradoras em outras funcoes
# abaixo é uma funcao decoradora
def cria_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}')
        return resultado
    return interna

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

def inverte_string(string):
    print(f'{inverte_string.__name__}')    
    return string[::-1]

inverte_checando_param = cria_funcao(inverte_string)
invertida = inverte_checando_param('123')
print(invertida) # com a etapa de funcao decoradora
invertida = inverte_string('123')
print(invertida) # sem a etapa de funcao decoradora

# Decoradores são 'Sintax sugar' (acucar sintatico)
@ cria_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]

invertida = inverte_string('123')
print(invertida) # com a funcao decoradora sem precisar usar ela explicitamente