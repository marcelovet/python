"""
while / else

o else só é executado se o laço while for executado por completo

"""
string = 'Um valor'
i = 0

while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('O else foi executado')

print('Fora do while')
