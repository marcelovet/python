"""
for + range
range(start, end, step) => cria uma sequência
start = int inicial da sequencia (incluso)
end = int final da sequencia (exlusivo)
step = int passo da sequencia
"""
numeros = range(2, 12, 2)

for i in numeros:
    print(i)

for i in range(2, -10, -2):
    print(i)
