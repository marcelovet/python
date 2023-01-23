# Criar classe Cliente que herda da classe Pessoa (Herança)
#     Pessoa tem nome e idade (com getters)
#     Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
import contas


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.nome!r}, {self.idade!r}'
        return f'{class_name}({attrs})'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self._conta: contas.Conta | None = None

    # decorator property - o getter
    @property
    def conta(self):
        return self._conta

    # o setter
    @conta.setter
    def conta(self, conta: contas.Conta):
        if not isinstance(conta, contas.Conta):
            raise ValueError('Você deve inserir child class de Conta')
        print(f'Definindo nova conta ao cliente {self.nome}:')
        self._conta = conta
        print(self._conta.exibir_saldo())


if __name__ == '__main__':
    p1 = Cliente('Fulano', 12)
    conta_p_1 = contas.ContaPoupanca('agencia P', 'conta P', 10.5)
    p1.conta = conta_p_1
    print(p1.conta.exibir_saldo())

    p2 = Cliente('Fulano', 12)
    conta_c_1 = contas.ContaCorrente('agencia C', 'conta C', 10.5)
    p2.conta = conta_c_1
    print(p2.conta.exibir_saldo())
