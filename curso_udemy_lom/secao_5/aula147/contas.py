# Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
#     ContaCorrente deve ter um limite extra
#     Contas têm agência, número da conta e saldo
#     Contas devem ter método para depósito
#     Conta (super classe) deve ter o método sacar abstrato (Abstração e
#     polimorfismo - as subclasses que implementam o método sacar)
from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: str, conta: str, saldo: int | float) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float) -> str: ...

    def depositar(self, valor: float) -> str:
        self.saldo += valor
        return f'Depósito de R$ {valor} realizado com sucesso\n'

    def exibir_saldo(self) -> str:
        texto_saldo = f'Agência {self.agencia}\n'
        texto_saldo += f'Conta {self.conta}\nSaldo = R$ {self.saldo:.2f}\n'
        return texto_saldo

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.agencia!r}, {self.conta!r}, {self.saldo!r}'
        return f'{class_name}({attrs})'


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            e_msg = 'Saldo insuficiente para o valor solicitado '
            e_msg += f'(R$ {valor}).\n'
            e_msg += f'Seu limite para saque é de R$ {self.saldo:.2f}\n'
            return e_msg
        self.saldo -= valor
        return f'Saque de R$ {valor} realizado com sucesso\n'


class ContaCorrente(Conta):
    def __init__(self, agencia: str, conta: str, saldo: int | float) -> None:
        super().__init__(agencia, conta, saldo)
        self._cheque_especial = 100

    def sacar(self, valor):
        limite = self.saldo + self._cheque_especial
        if limite < valor:
            e_msg = 'Saldo insuficiente para o valor solicitado '
            e_msg += f'(R$ {valor}).\n'
            e_msg += f'Seu limite para saque é de R$ {limite:.2f}\n'
            return e_msg
        self.saldo -= valor
        return f'Saque de R$ {valor} realizado com sucesso\n'


if __name__ == '__main__':
    conta_p_1 = ContaPoupanca('agencia P', 'conta P', 10.5)
    print(conta_p_1.exibir_saldo())
    print(conta_p_1.depositar(100))
    print(conta_p_1.sacar(200))
    conta_c_1 = ContaCorrente('a', 'b', 10)
    print(conta_c_1.exibir_saldo())
    print(conta_c_1.depositar(100))
    x = conta_c_1.sacar(300)
    print(x)
    print(conta_c_1.exibir_saldo())
