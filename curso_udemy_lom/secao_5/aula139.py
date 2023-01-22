# Context Manager com funcao - Criando e usando gerenciadores de contexto
from contextlib import contextmanager


@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    # except Exception as error:
    #     print('Ocorreu um erro', error, sep='\n')
    finally:
        print('Fechando arquivo')
        arquivo.close()


with my_open('aula150.txt', 'w') as arquivo:
    arquivo.write('Blablabla\n')
    arquivo.write('Linha 1', 123)
    print('WITH', arquivo)
