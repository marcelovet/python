import json

from aula115 import SAVE_TO, Pessoa


def carregar_pessoa(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            pessoa = json.load(file)
        return pessoa
    except FileNotFoundError:
        print('Não há arquivo de pessoa salvo')


p2 = carregar_pessoa(SAVE_TO)
p2 = Pessoa(**p2)
print(p2.nome, p2.idade)
