"""
Exercicio para closure
Crie funções que duplicam, triplicam e quadruplicam o numero recebido como
parametro
"""


def multiplicador(numero_base):
    def multiplica(numero):
        return numero * numero_base
    return multiplica


retorna_dobro = multiplicador(2)
retorna_triplo = multiplicador(3)
retorna_quadruplo = multiplicador(4)

print(retorna_dobro(5))
print(retorna_triplo(5))
print(retorna_quadruplo(5))
