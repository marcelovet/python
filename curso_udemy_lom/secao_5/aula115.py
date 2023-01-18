# __dict__ e vars para atributos de instancia
import json
import os

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'pessoa.json')


class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


def salvar_pessoa(pessoa, path):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(pessoa, file, ensure_ascii=False, indent=2)


p1 = Pessoa('João', 35)

# print(p1.__dict__)
# print(vars(p1))

if __name__ == '__main__':
    print(f'{p1.nome} foi salvo')
    salvar_pessoa(p1.__dict__, SAVE_TO)
