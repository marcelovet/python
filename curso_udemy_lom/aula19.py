
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    string = f'{primeiro_valor=} é maior do que {segundo_valor=}'
elif primeiro_valor == segundo_valor:
    string = f'{primeiro_valor=} é igual ao {segundo_valor=}'
else:
    string = f'{segundo_valor=} é maior do que {primeiro_valor=}'

print(string)
