# lançando erros - raise
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Não é possível dividir por zero')
    return True

def deve_ser_int_ou_float(valor):
    tipo_valor = type(valor)

    if not isinstance(valor, (int, float)):
        raise TypeError(
            f'{valor=} deve ser int ou float. '
            f'Você enviou {tipo_valor.__name__}'
        )
    
    return True

def divide(n, d):
    deve_ser_int_ou_float(d)
    deve_ser_int_ou_float(n)
    nao_aceito_zero(d)    
    return n / d

print(divide(8, 0))
