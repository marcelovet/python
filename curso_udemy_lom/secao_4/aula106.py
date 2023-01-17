# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final, de append), b (binário)
# t (modo texto), + (leitura e escrita)

# Context manager - with (abre e fecha)

# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
# pode usar caminho relativo ao venv ou absoluto
# https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/
import os

caminho_arquivo = 'curso_udemy_lom/secao_4/aula106.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()
with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    # print('Olá mundo')
    # print('Arquivo vai ser fechado')
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')
    arquivo.writelines(
        ('linha 3\n', 'linha 4\n')
    )

with open(caminho_arquivo, 'r') as arquivo:
    # strip remove whitespace e \n é considerado whitespace
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    # print(arquivo.read())
    for linha in arquivo.readlines():
        print(linha.strip(), '-')

# os.rename(caminho_arquivo, 'curso_udemy_lom/secao_4/aula106_a.txt')
os.remove(caminho_arquivo)
