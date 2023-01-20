# Relacoes entre classes: associação, agregação, composicao
# Composição é uma especializacao da agregaçao.
# Mas nela, quando o objeto "pai" for apagado, todas as referências
# dos objetos filhos também sao apagadas.
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
    
    def inserir_enderecos(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
    
    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(f'{endereco.rua}, {endereco.numero}')

    def __del__(self):
        print('Apagando', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
    
    def __del__(self):
        print('Apagando', self.rua, self.numero)

cliente1 = Cliente('Maria')
cliente1.inserir_enderecos('uma rua', 1)
cliente1.inserir_enderecos('outra rua', 12)
cliente1.listar_enderecos()

endereco_externo = Endereco('mais uma rua', 12)

del cliente1

print('-' * 10, 'Aqui acaba o codigo')
