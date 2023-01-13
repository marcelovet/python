# dict e set comprehension
produto = {
    'nome': 'Caneta azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}

print(dc)

lista =[
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('v', 'valor v'),
]
dc = {
    chave: valor
    for chave, valor in lista
}
print(dc)

s1 = {i for i in range(10)}
print(s1)
