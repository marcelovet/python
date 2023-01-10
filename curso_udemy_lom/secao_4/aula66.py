"""
Dicionários em python (tipo dict)
Dicionarios sao estruturas de dados do tipo par 'chave' e 'valor'.
Chaves podem ser consideradas como o 'indice', que podem ser de tipos
imutáveis: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro dict.
Usamos as chaves - {} - ou a classe dict para criar dicionarios.
Imutáveis: str, int, float, bool, tuple
Mutáveis: dict, list
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

pessoa = dict(nome='Fulano', sobrenome='sicrano')

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

# print(pessoa, type(pessoa))
print(pessoa['nome'], end='\n\n')

for chave in pessoa:
    print(chave, pessoa[chave])

# Manipulando chaves e valores em dicionarios

pessoa = {}

pessoa['Nome'] = 'Luiz Otávio'
print(pessoa['Nome'])

pessoa['Nome'] = 'Maria'
print(pessoa['Nome'])

# ou ainda
pessoa = {}
chave = 'nome'

pessoa[chave] = 'Maria'
print(pessoa[chave])

# o metodo get avalia se existe a chave e retorna o segundo valor se não (por padrão None)
# se existe retorna o valor da chave
if pessoa.get('sobrenome') is None:
    print('Essa chave não existe')
