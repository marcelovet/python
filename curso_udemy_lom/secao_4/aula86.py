# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html

# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
# import sys

# print(sys.platform)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo e pode acabar sobrescrevendo ela
# from sys import exit, platform
# platform = 'Minha plataforma'
# print(platform)

# alias 1 - import nome_modulo as apelido
# import sys as sistema
# print(sistema.platform)

# alias 2 - from nome_modulo import objeto as apelido
# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem
# from sys import exit, platform as plt
# platform = 'Minha plataforma'
# print(platform, plt)

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
# from sys import *