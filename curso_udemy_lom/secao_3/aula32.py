"""
Tipos built-in
https://docs.python.org/3/library/stdtypes.html
imutáveis já vistos: str, float, int, bool
"""

string = 'Marcelo paiva'
outra_variavel = string

# string[3] = 'ABC' não funciona por ser imutavel
# Precisaria ser feito assim:
outra_variavel = f'{string[:4]}ABC{string[4:]}'

print(outra_variavel.capitalize())
