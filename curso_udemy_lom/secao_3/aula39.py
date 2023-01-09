"""
Funcionamento do for
iterável => str, range, etc (objeto com método __iter__)
iterador => quem sabe entregar um valor por vez
next => me entregue o próximo valor
iter => me entregue seu iterador
"""
texto = 'Um texto'.__iter__()
"""
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__()) # após esgotar os valores ele lança um erro
"""
texto = 'Luiz' # iterável

# Basicamente o que o for faz:
iterador = iter(texto)
while True:
    try:
        print(next(iterador))
    except StopIteration:
        break

# que representa
for letra in texto:
    print(letra)
