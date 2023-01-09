"""
O método .format permite referenciar a variável:
1 - pela ordem de declaração dentro do ()
string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)
2 - pelo índice da ordem de declaração dentro do ()
string = 'a={0} b={1} c={2:.2f}'
formato = string.format(a, b, c)
3 - pelo nome do parametro declarado dentro do ()
string = 'a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)
"""
a = 'A'
b = 'B'
c = 1.1
string = 'a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)
