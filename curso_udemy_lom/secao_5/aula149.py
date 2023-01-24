# dataclasses - O que são dataclasses?
# __init__ e __post_init__ em dataclass
from dataclasses import dataclass


@dataclass(init=True)
class Pessoa:
    nome: str
    idade: int
    sobrenome: str

    # se definir init=False no dataclass nao tem post_init
    # e precisa definir o __init__
    def __post_init__(self):
        # print('POST INIT')
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, valor: str):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('Fulano', 12, "Sicrano")
    print(p1)
    print(p1.nome_completo)
