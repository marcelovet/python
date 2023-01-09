"""
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
"""

maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'

print(f"""
Operadores de comparação (relacionais)
OP      Significado         Exemplo     Resultado
>       maior               2 > 1       {maior}
>=      maior ou igual      2 >= 2      {maior_ou_igual}
<       menor               1 < 2       {menor}
<=      menor ou igual      2 <= 2      {menor_ou_igual}
==      igual               'a' == 'a'  {igual}
!=      diferente           'a' != 'b'  {diferente}
""")
