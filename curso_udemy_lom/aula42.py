"""
Listas em python
tipo list - mutável
suporta vários valores de qualquer tipo
conhecimentos reutilizáveis - indices e fatiamento
métodos úteis - 
    append - adiciona um item ao final da lista
    insert - adiciona um item no indice escolhido
    pop - remove um elemento no indice escolhido. No final por padrão
    del - remove um elemento de um indice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Permite:
Create, Read, Update, Delete (CRUD)
Criar, ler, alterar, apagar
"""
# lista = list()
# print(lista, type(lista))
lista = [123, True, 'Nome', [], 1.2]
print(lista[1], type(lista[1]))
print(lista[2][1])

lista[2] = 2 # lista é mutável
print(lista)

del lista[0]
print(lista)
"""
Não é uma boa prática usar remover ou adicionar em outro local além do fim da lista,
pois o python precisa 'reindexar' os itens da lista
"""

lista.append(True) # adiciona ao fim
print(lista)
ultimo_valor = lista.pop() # remove do fim se não definido o valor indice dentro do método
print(lista, 'Removido,', ultimo_valor)

# limpar a lista
lista.clear()
print(lista)
lista = [123, True, 'Nome', [], 1.2]
print(lista)

# inserir um elemento em qualquer indice da lista
lista.insert(0, 'abc') # (indice, valor) se o indice é out of range, ele adiciona ao final
print(lista)

# append e concatenação
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
print("listas a + b", lista_a + lista_b)
print("lista a",lista_a)

lista_a.extend(lista_b)
print("lista a",lista_a)

"""
Cuidados com dados mutáveis
em imutáveis: = copia o valor
em mutáveis: = aponta para o mesmo valor na memória
"""
# imutavel - passa a apontar para outro local
str_a = "abc"
str_b = str_a
print(f'{str_a=}, {str_b=}')
str_a = "ab"
print(f'{str_a=}, {str_b=}')

# mutavel
lista_a = [1, 2, 3]
lista_b = lista_a
print(f'{lista_a=}, {lista_b=}')
lista_a.pop()
print(f'{lista_a=}, {lista_b=}')

# para apontar para outro local em lista simples (somente imutaveis dentro dela)
lista_a = [1, 2, 3]
lista_b = lista_a.copy()
print(f'{lista_a=}, {lista_b=}')
lista_a.pop()
print(f'{lista_a=}, {lista_b=}')
