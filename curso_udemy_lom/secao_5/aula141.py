# funcoes decoradoras e decoradores com metodos
def meu_repr(self):
    class_name_ = self.__class__.__name__
    class_dict_ = self.__dict__
    class_repr_ = f'{class_name_}({class_dict_})'
    return class_repr_


def adiciona_repr(cls):
    # def meu_repr(self):
    #     class_name_ = self.__class__.__name__
    #     class_dict_ = self.__dict__
    #     class_repr_ = f'{class_name_}({class_dict_})'
    #     return class_repr_
    cls.__repr__ = meu_repr
    return cls


def meu_planeta(metodo):
    def interna(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)
        if 'terra' in resultado.lower():
            return 'Você está em casa'
        return resultado
    return interna


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def falar_nome(self):
        return f'O planeta é {self.nome}'


brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(terra)

print(terra.falar_nome())
print(marte.falar_nome())
