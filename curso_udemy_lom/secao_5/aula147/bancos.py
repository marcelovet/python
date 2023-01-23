# Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
# Banco será responsável autenticar o cliente e as contas da seguinte maneira:
#     Banco tem contas e clentes (Agregação)
#     * Checar se a agência é daquele banco
#     * Checar se o cliente é daquele banco
#     * Checar se a conta é daquele banco
# Só será possível sacar se passar na autenticação do banco (descrita acima)
# Banco autentica por um método (autenticar).
import clientes
import contas


class Banco:
    def __init__(
        self,
        agencias: list[str] | None = None,
        clientes: list[clientes.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None
    ) -> None:
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia not in self.agencias:
            print(f'{conta.agencia} not in {self.agencias}')
            return False
        print(f'{conta.agencia} in {self.agencias}')
        return True

    def _checa_cliente(self, cliente):
        if cliente not in self.clientes:
            return False
        return True

    def _checa_conta(self, conta):
        if conta not in self.contas:
            return False
        return True

    def autenticar(self, cliente: clientes.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}\n{attrs}'


if __name__ == '__main__':
    c1 = clientes.Cliente('Luiz', 20)
    cc1 = contas.ContaCorrente('123', '321', 0)
    c1.conta = cc1
    c2 = clientes.Cliente('Fulano', 30)
    cp1 = contas.ContaPoupanca('1233', '4321', 0)
    c2.conta = cp1
    banco = Banco()
    # print(banco)
    banco.agencias.extend(['123', '121', '122'])
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    c2.conta.depositar(100)
    print(banco.autenticar(c1, c1.conta))
    print(banco.autenticar(c2, c2.conta))
