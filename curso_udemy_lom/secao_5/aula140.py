# Funcoes decoradoras e decores em classes
# se fosse usar heranca
# class MyReprMixin:
#     def __repr__(self) -> str:
#         class_name_ = self.__class__.__name__
#         class_dict_ = self.__dict__
#         class_repr_ = f'{class_name_}({class_dict_})'
#         return class_repr_
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


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(terra)
