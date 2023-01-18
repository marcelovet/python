# @staticmethod (metodos estaticos) sao inuteis no python
# metodos estaticos sao metodos que estao dentro da classe
# mas que nao tem acesso ao self nem ao cls
# Em resumo, sao funcoes que existem dentro da sua classe
class Classe:
    @staticmethod
    def funcao_que_esta_na_classe():
        print('oi')


c1 = Classe()
c1.funcao_que_esta_na_classe()
Classe.funcao_que_esta_na_classe()
