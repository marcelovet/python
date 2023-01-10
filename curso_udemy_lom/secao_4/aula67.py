"""
métodos uteis dos dicionarios em python
len - numero de chaves
keys - iteravel com as chaves
values - iteravel com os valores
items - iteravel com chaves e valores
setdefault - adiciona valor se a chave nao existe
copy - retorna uma shallow copy
get - obtem uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o ultimo item adicionado
update - atualiza um dicionario com outro
"""
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.7,
    'enderecos': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra tal', 'numero': 321}
    ]
}

print(pessoa.__len__()) # chamando o metodo do objeto
print(len(pessoa)) # chamando a funcao que chama o metodo __len__

