"""
Repetições
while (enquanto)
Executa um bloco de código enquanto uma condição verdadeira
O importante é que while precisa de uma situacao interna que torne a condicao False
ou que interrompa o laço (break)
de modo a não cair em um loop infinito
"""
"""
condicao = True

while condicao:
    nome = input('Digite seu nome: ')
    
    if nome in 'sair':
        break
"""
contador = 0

while contador < 10:
    print('EITA')
    contador += 1
    print(contador)

print('Acabou')

"""
Operadores de atribuição com operadores aritmeticos
+= x, soma ou concatena x na variavel
-= x, subtrai x na variavel
*= x, multiplica x na variavel
/= x, divide x na variavel
//= x, divide inteiro x na variavel
**= x, potencia x na variavel
%= x, modulo x na variavel
"""
contador = 10

while contador != 100:
    print('EITA')
    contador **= 2
    print(contador)

print('Acabou', end='\n\n------\n')

"""
continue - pula as linhas do bloco abaixo dele e reinicia a avaliação da condição do laço
"""
contador = 0

while contador < 5:
    contador += 1
    
    if contador == 3:
        continue
    
    print(contador)

print('Acabou')

"""
laços internos while dentro de while
"""
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1    
    while coluna <= qtd_colunas:
        print(f'{linha=} - {coluna=}')
        coluna += 1
    linha += 1

print('Acabou')

"""
iterando strings com while
"""
nome = 'Luiz Otavio'
tamanho_nome = len(nome)
nova_string = ''
contador = 0

while contador < tamanho_nome:
    nova_string += f'{nome[contador]}*'
    contador += 1

print(nova_string)