# Python special methods, magic methods, ou dunder methods
# dunder = double underscore = __dunder__
# Antigo e util: https://rszalski.github.io/magicmethods
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self, other) - self < other
# __le__(self, other) - self <= other
# __gt__(self, other) - self > other
# __ge__(self, other) - self >= other
# __eq__(self, other) - self == other
# __ne__(self, other) - self != other
# __add__(self, other) - self + other
# __sub__(self, other) - self - other
# __mul__(self, other) - self * other
# __truediv__(self, other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
class Ponto:
    def __init__(self, x, y, z='string') -> None:
        self.x = x
        self.y = y
        self.z = z

    # é uma representacao geral do objeto
    def __str__(self) -> str:
        return f'({self.x}, {self.y}, {self.z})'

    # é uma representacao para outros desenvolvedores de como
    # é a montagem do objeto
    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    def __gt__(self, other) -> bool:
        self_xy = self.x + self.y
        other_xy = other.x + other.y
        comparado = self_xy > other_xy
        return comparado


if __name__ == '__main__':
    p1 = Ponto(1, 2)
    p2 = Ponto(115.44, 22.87)
    # se nao tiver __str__ definido, ele vai buscar o __repr__
    print(p1)
    print(p2)
    # chama o __repr__ se denfinido
    print(repr(p2))
    print(f'{p1!r}')
    p3 = p1 + p2
    print(p3)
    print(f'p1 é maior que p2?: {p1 > p2}')
    print(f'p2 é maior que p1?: {p2 > p1}')
