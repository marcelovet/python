import json
import os

pessoas = [
    {
        'nome': 'José',
        'sobrenome': 'Miranda',
        'enderecos': [
            {'rua': 'R1', 'numero': 32},
            {'rua': 'R2', 'numero': 55},
        ],
        'altura': 1.8,
        'numeros_preferidos': (2, 4, 6, 8, 10),
        'dev': True,
        'nada': None,
    },
    {
        'nome': 'Luiz 2',
        'sobrenome': 'Miranda',
        'enderecos': [
            {'rua': 'R1', 'numero': 32},
            {'rua': 'R2', 'numero': 55},
        ],
        'altura': 1.8,
        'numeros_preferidos': (2, 4, 6, 8, 10),
        'dev': True,
        'nada': None,
    },
    {
        'nome': 'Siclano',
        'sobrenome': 'Miranda',
        'enderecos': [
            {'rua': 'R1', 'numero': 32},
            {'rua': 'R2', 'numero': 55},
        ],
        'altura': 1.4,
        'numeros_preferidos': (2, 4, 6, 8, 10),
        'dev': False,
        'nada': None,
    },
]

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'aula107.json')

with open(SAVE_TO, 'w', encoding='utf-8') as file:
    json.dump(pessoas, file, ensure_ascii=False, indent=2)

with open(SAVE_TO, 'r', encoding='utf-8') as file:
    pessoas = json.load(file)
    print(pessoas)
