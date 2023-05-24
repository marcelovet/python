"""
Fatiamento de strings
 0 1 2 3 4 5 6 7 8
-9-8-7-6-5-4-3-2-1
Olá mundo
Fatiamento [i:f:p] [::]
i - inicio
f - fim
p - passo
Obs.: a função len retorna a quantidade de caracteres na str
"""
variavel = 'Olá mundo'
print(variavel[4:])  # se omitir o fim, ele vai até o fim da str
print(variavel[:5])  # o f é não incluso
print(variavel[-9:-2])  # o f é não incluso
print(len(variavel))
print(variavel[0:len(variavel):1])
# o passo inclui o indice anterior abc[::2] daria ac (a pula ab, c)
print(variavel[0:len(variavel):2])
# passo invertido, para i e f precisa usar os indices negativos
print(variavel[::-1])
# passo invertido, para i e f precisa usar os indices negativos
print(variavel[-1:-5:-1])
