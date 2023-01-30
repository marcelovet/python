# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.
import os

caminho = os.path.join('/home/users', 'desktop', 'curso', 'arquivo.txt')
print(caminho)
diretorio, arquivo = os.path.split(caminho)
print(diretorio, arquivo)
print(os.path.splitext(arquivo))
print(os.path.splitext(caminho))
print(os.path.exists(caminho))
# caminho absoluto do diretorio onde estou
print(os.path.abspath('.'))
# caminho do diretorio em que esse arquivo esta
print(os.path.dirname(__file__))

# os.listdir para navegar em caminhos
novo_caminho = '/home/ubuntu-py/Desktop/curso/curso_udemy_lom/'

print(f'\nO que tem dentro de {novo_caminho}')
for pasta in os.listdir(novo_caminho):
    caminho_completo = os.path.join(novo_caminho, pasta)
    print(caminho_completo)

    for item in os.listdir(caminho_completo):
        print('|')
        print('---->', item)
