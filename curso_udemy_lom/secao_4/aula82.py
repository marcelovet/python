# yield from
def gen1():
    print('Gen 1')
    yield 1
    yield 2
    yield 3

def gen3():
    print('Gen 3')
    yield 7
    yield 8
    yield 9

def gen2(gen):
    yield from gen
    yield 4
    yield 5
    yield 6

g1 = gen2(gen1())
g2 = gen2(gen3())
for numero in g1:
    print(numero)
for numero in g2:
    print(numero)
