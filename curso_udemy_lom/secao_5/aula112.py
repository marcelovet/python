# escopo da classe e de metodos da classe
class Animal:
    def __init__(self, nome):
        self.nome = nome
        # variavel esta no escopo interno somente e nao podera mais ser acessado
        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        # nome será acessível por que sera definido no escopo da instancia
        def funcao(alimento):
            print(alimento)
        return f'{self.nome} está comendo {alimento}'

    def executar(self, *args, **kwargs):
        # comendo foi definido no escopo superior e consegue ser chamado
        # return self.funcao(*args, **kwargs) nao funcionaria
        return self.comendo(*args, **kwargs)


leao = Animal(nome='Leão')
print(leao.executar('maçã'))
