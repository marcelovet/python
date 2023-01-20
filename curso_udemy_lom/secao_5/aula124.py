# Relacoes entre classes: associação, agregação, composicao
# Agregacao é uma forma mais especializada de associacao entre dois ou mais objetos
# Cada objeto tera seu ciclo de vida independente
# Geralmente é uma relacao de um para muitos (um objeto tem um ou muitos objetos)
# Os objetos podem viver separadamente, mas pode se tratar de uma relacao onde
# um objeto precisa de outro para fazer determinada tarefa
# (existem controversias sobre as definicoes de agregacao)
class Carrinho:
    def __init__(self):
        self._produtos = []
        self._total = None

    def inserir_produtos(self, *produtos):
        self._produtos.extend(produtos)

    def total(self):
        self._total = sum([p.preco for p in self._produtos])
        return self._total

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(f'Produto: {produto.nome}, Valor: {produto.preco}')
        print()


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produto('caneta', 1.20), Produto('camiseta', 20)
carrinho.inserir_produtos(p1, p2)

carrinho.listar_produtos()
carrinho.total()
