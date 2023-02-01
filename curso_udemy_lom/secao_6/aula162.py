# os.walk
# os.walk é uma função que permite percorrrer uma estrutura de diretórios de
# de maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla
# possui três elementos: o diretorio atual (root), uma lista de subdiretorios
# (dirs) e uma lista de arquivos do diretorio atual (files).
import os
from itertools import count

caminho = '/home/ubuntu-py/Desktop/curso/curso_udemy_lom/'
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('    ', the_counter, 'Dir:', dir_)

    for file_ in files:
        print('    ', the_counter, 'File:', file_)
