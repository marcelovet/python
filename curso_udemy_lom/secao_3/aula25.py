"""
interpolação básica de strings
s - string
d e i - int
f - float
.<múmero de dígitos>f
x e X - hexadecimal (ABCDEF0123456789)
> - esquerda
< - direita
^ - centro
Sinal - + ou - -
Exemplo: 0>-100,.1f
conversion flags - !r !s !a são flags para chamar métodos:
__repr__ __str__ 
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel:-^10}')
print(f'{1000.45897643:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:06X}')
