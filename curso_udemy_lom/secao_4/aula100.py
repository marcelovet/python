# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemay', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'Joao', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

# alunos = ['a', 'a', 'a','b', 'c', 'a']
# grupos = groupby(alunos)
# for chave, grupo in grupos:
#     print(chave)
#     print(list(grupo))
# groupby precisa estar ordenado
def ordena(a):
    return a['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

alunos_a = []
alunos_b = []
alunos_c = []
alunos_d = []

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)
        if aluno['nota'] == 'A':
            alunos_a.append(aluno)
        elif aluno['nota'] == 'B':
            alunos_b.append(aluno)
        elif aluno['nota'] == 'C':
            alunos_c.append(aluno)
        elif aluno['nota'] == 'D':
            alunos_d.append(aluno)

print(f'Alunos nota A:', *alunos_a, sep='\n')
print(f'Alunos nota B:', *alunos_b, sep='\n')
print(f'Alunos nota C:', *alunos_c, sep='\n')
print(f'Alunos nota D:', *alunos_d, sep='\n')
