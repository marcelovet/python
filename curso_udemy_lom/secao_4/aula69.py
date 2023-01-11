"""
Sets - conjuntos em python (tipo set)
Conjuntos são ensinados na matemática
https://brasilescola.uol.com.br/matematica/definicao-conjunto.htm
Representados graficamente pelo diagrama de Venn
Sets em python são mutáveis, porem aceitam apenas tipos imutaveis como valor interno
"""
# Criando um set
# set(iteravel) ou {1, 2, 3}
s1 = set() # para criar set vazio s1 = {} cria um dict vazio
print(s1)

s1 = set('Marcelo') # com dados e itera em cada elemento
print(s1)

s1 = {'Marcelo'} # com dados, mas o elemento é a str total
print(s1)

# sets são eficientes para remover valores duplicados de iteraveis
# - seus valores são sempre unicos
# exemplo de remoção de duplicados em lista
s1 = [1, 1, 3, 3, 3, 4, 5, 2]
print(s1)
s1 = list(set(s1))
print(s1)

# - não aceitam valores mutaveis
try:
    s1 = {1, 2, [1, 2,]}
except:
    print('set não permite valor mutavel')

# - nao tem indices
try:
    s1 = {1, 2, 3}
    print(s1[0])
except:
    print('set não possui indice')

# - nao garantem a ordem por nao ter indices
s1 = set('Marcelo')
print(s1)

# - sao iteraveis
s1 = {1, 2, 3}
print('2 está no set') if 2 in s1 else print('2 não está no set')

for elemento in s1:
    print(f'Passo {elemento}')

# métodos uteis em sets
# add, update, clear, discard
s1 = set()
s1.add('luiz') # adiciona um elemento por vez
s1.add(1)
print(s1)

s1.update(('Olá mundo', 1, 2, 3, 4)) # permite adicionar mais de um elemento
print(s1)

s1.clear() # limpa o set
print(s1)

s1.update(('Olá mundo', 1, 2, 3, 4))
s1.discard('Olá mundo') # descarta o elemento informado
s1.discard(99) # não gera erro se não há o elemento informado
print(s1)

# Operadores uteis
# união (|) união (union) - une set
# intersecção (&) (intersection) - itens que há em ambos
# diferença (-) - presente somente no set da esquerda
# diferenca simetrica (^) - ausente em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2
print(f'União de {s1} e {s2}: {s3}')

s3 = s1 & s2
print(f'Intersecção de {s1} e {s2}: {s3}')

s3 = s1 - s2
print(f'Diferença de {s1} e {s2}: {s3}')

s3 = s1 ^ s2
print(f'Diferença simétrica de {s1} e {s2}: {s3}')

s1 = set('marc')
s2 = set('marc')
s3 = s1 - s2
print(s1, s3, len(s3))

# Exemplo de uso do set
palavra = set('Banana')
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra)

    diff_palavras = palavra - letras
    if len(diff_palavras) == 0:
        print('Parabéns você acertou todas as letras')
        break
    else:
        print(f'Letras que você acertou: {palavra & letras}')