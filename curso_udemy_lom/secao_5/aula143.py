# Classes decoradoras (Decorator classes)
class MultiplicarPor:
    def __init__(self, multiplicador) -> None:
        # print('INIT recebe', func)
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            elementos = f'{func.__name__} com elementos {args}{kwargs}'
            print(elementos, 'será multiplicada por', self._multiplicador)
            return resultado * self._multiplicador
        return interna


@MultiplicarPor(2)
def soma(x, y):
    return x + y


dois_mais_cinco = soma(x=2, y=5)
print(dois_mais_cinco)
