# dataclasses - O que são dataclasses?
from dataclasses import asdict, astuple, dataclass

# frozen congela a class
# entao nao consigo redefinir as instancias inicializadas
# order cria a regra para ordenar o objeto da classe
# porem é uma melhor pratica criar sua regra de ordenacao
# @dataclass(frozen=True, order=True)
# class Pessoa:
#     nome: str
#     sobrenome: str

#     def __post_init__(self):
#         print('Pos init')


@dataclass(frozen=True, order=False)
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):
        print('Pos init')


if __name__ == '__main__':
    p1 = Pessoa('Fulano', "Sicrano")
    p2 = Pessoa('Fulano', "bertanho")
    p3 = Pessoa('Fulano', "giocono")
    pessoas = [Pessoa('A', "Z"), Pessoa('B', "X"), Pessoa('C', "Y")]
    ordenadas = sorted(pessoas, reverse=True, key=lambda p: p.sobrenome)
    print(ordenadas)
    pessoas = [p1, p2, p3]
    # asdict e astuple
    pessoas_lt_dict = [
        asdict(p)
        for p in pessoas
        if p.sobrenome != 'Sicrano'
    ]
    print(pessoas_lt_dict)
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1)[0])
    # nao funciona pq esta frozen
    # p1.nome = 'Tiago'
