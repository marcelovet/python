"""
lista de listas e seus indices
"""

salas = [
    ['José', 'Maria Helena', ],
    ['Elaine', ],
    ['Luiz', 'João', 'Fulano', (1, 2, 3, 4)]
]

print(salas[2][3][2])

salas[2].pop()

for n_sala, sala in enumerate(salas):
    print(f'Sala {n_sala + 1}')
    for n_aluno, aluno in enumerate(sala):
        print(f'Aluno {n_aluno + 1}: {aluno}')
