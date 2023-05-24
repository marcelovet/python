# variavel livre + nonlocal
# print(globals()) # exibe as variaveis definidas no escopo global
# def fora(x):
#     a = x

#     def dentro():
#         print(locals()) # exibe as variaveis disponiveis nesse escopo
#         return a # é variavel livre pq n esta definida em dentro desse escopo
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())
def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        # valor_final += valor_a_concatenar # UnboundLocalError, pq é variavel livre
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
c('c')
final = c('')

print(final)
