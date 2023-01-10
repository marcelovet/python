"""
Closure e funcoes que retornam outras funcoes
No exemplo a saudacao fica gravada na callstack e permite retornar outra função
"""
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

print(falar_bom_dia('Luiz'))
print(falar_boa_noite('Zé'))
