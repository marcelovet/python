# Sao 4 os pilares da programacao orientada a objetos
# Encapsulamento, abstração, herança e polimorfismo
# Encapsulamento (modificadores de acesso: public, protected, private)
# Python nao tem modificadores de acessso
# mas podemos seguir as seguintes CONVENCOES
#   (sem underline) = public
# pode ser usado em qualquer lugar
# _ (um underline) = protected
# não deve ser usado fora da classe ou subclasses
# __ (dois underlines) = private
# _NameClass__attr_or_method
# "name mangling" (desfiguracao de nomes) em python so DEVE ser usado na classe em que foi declarado
class Foo:
    def __init__(self):
        self.public = 'Isso é publico'
        self._protected = 'Isso é protegido'
        self.__private = 'isso é private'

    def metodo_publico(self):
        print(self._metodo_protected())
        print(self.__private)
        print(self.__metodo_private())
        return 'metodo publico'

    def _metodo_protected(self):
        return 'metodo protegido'

    def __metodo_private(self):
        return 'metodo private'


f = Foo()
print(f.public)
print(f.metodo_publico())
# faz a desfiguracao de nomes
print(f._Foo__metodo_private)
