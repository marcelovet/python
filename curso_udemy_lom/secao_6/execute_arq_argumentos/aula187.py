# sys.argv - executando arquivos com argumentos no sistema
# Fonte = Fira Code
import sys

# recebe os argumentos de execucao do arquivo (ex python -u aula.py)
args = sys.argv
len_args = len(args)

if len_args <= 1:
    print("Você não passou argumentos")
