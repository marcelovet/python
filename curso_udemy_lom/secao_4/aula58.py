"""
Escopo de funções em python
Escopo significa o local onde aquele código pode atingir
Existe escopo global e local
Escopo global é onde todo o código é alcançável
Escopo local é onde apenas nomes do mesmo local podem ser alcançados
Não temos acesso a nomes de escopos internos nos escopos externos
A palavra global faz uma variavel de escopo externo ser a mesma no escopo interno
"""
x = 3 # global

def escopo():
    def outra_funcao(): # funcao em escopo local
        y = 2
        print(x, y)
    x = 1 # local
    outra_funcao()

def novo_escopo():
    print(x)

def mais_um_escopo():
    # alterando o valor de x que está no escopo global
    global x
    x = 5
    print(x)

escopo()
novo_escopo()
mais_um_escopo()
print(x)