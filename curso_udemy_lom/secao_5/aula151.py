# dataclasses - O que são dataclasses?
from dataclasses import dataclass, field

# é possível definir um valor padrao nas dataclass
# desde que seja um valor imutavel


@dataclass
class Pessoa:
    nome: str = 'Missing'
    sobrenome: str = 'Not sent'
    idade: int = 100
    # field permite eu usar o valor mutavel padrao
    # pq a cada nova instancia ele vai chamar a funcao list (cria uma nova)
    enderecos: list[str] = field(default_factory=list)
    registro: bool = field(
        default=True, repr=False
    )


if __name__ == '__main__':
    p1 = Pessoa()
    print(p1)
