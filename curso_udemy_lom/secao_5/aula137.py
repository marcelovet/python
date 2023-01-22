# __new__ e __init__ em classes python
# __new__ é o responsavel por criar e retornar o novo objeto
# Por isso, __new__ recebe cls
# __new__ deve retornar o novo objeto!
# __init__ é o responsavel por inicializar a instancia
# Por isso, __init__ recebe self
# __init__ nao deve retornar None!
# object é a superclasse de uma classe
class A:
    # na maioria dos casos nao sera util e nao é obrigatorio
    def __new__(cls, *args, **kwargs):
        print('Uma execucao antes de criar a instancia')
        instance = super().__new__(cls)
        print('Uma execucao depois de criar a instancia')
        return instance

    def __init__(self, x):
        self.x = x
        print('Sou o __init__')

    def __repr__(self) -> str:
        return f'A(x={self.x})'


a = A(123)
print(a)
