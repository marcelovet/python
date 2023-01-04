"""
Laço for / in

No while para iterar em palavra:

i = 0
tamanho_string = len(texto)

while i < tamanho_string:
    ...
    i += 1

while é mais comum de ser usado em condições que podem repetir infinitas vezes
enquanto uma certa validação não é atingida, por exemplo,

while True:
    numero = input('digite um numero')
    if numero.isdigit():
        print('Obrigado')
        break
    else:
        print('Isso não é um numero')
"""
texto = 'Python'
novo_texto = ''
# for itera em uma variavel
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')
