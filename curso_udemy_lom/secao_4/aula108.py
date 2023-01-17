# problema dos parametros mutaveis em python
# def adiciona_clientes(nome, lista=[]):
#     lista.append(nome)
#     return lista
# # lista por ser mutavel, e definida na primeira chamada e passa a ser reutilizada
# cliente1 = adiciona_clientes('marcelo')
# adiciona_clientes('joana', cliente1)
# cliente2 = adiciona_clientes('marcelo')
# adiciona_clientes('bretanha', cliente2)
# print(cliente1)
# print(cliente2)
# # uma solucao
# lista1 = []
# lista2 = []
# cliente1 = adiciona_clientes('marcelo', lista1)
# adiciona_clientes('joana', cliente1)
# cliente2 = adiciona_clientes('marcelo', lista2)
# adiciona_clientes('bretanha', cliente2)
# print(cliente1)
# print(cliente2)
# o melhor é resolver na propria funcao e nao colocar o valor padrao do parametro como um tipo mutavel
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('marcelo')
adiciona_clientes('joana', cliente1)
cliente2 = adiciona_clientes('marcelo')
adiciona_clientes('bretanha', cliente2)

print(cliente1)
print(cliente2)
