# generator expression, iterables e iterators
# iterable = ['Eu', 'Tenho', '__iter__']
# iterator = iterable.__iter__() # tem __iter__ e __next__
# print(next(iterator))
# generator, em geral, sao funcoes que sabem pausar
import sys

lista = [n for n in range(100)]

# ele nao salva todos os valores na memoria, ele entrega um por vez
generator = (n for n in range(1000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

# for n in generator:
#     print(next(generator))

# def generator(n=0):
#     yield 1 # Pausar
#     print('Continuando')
#     yield 2 # Pausar
#     yield 3 # Pausar
#     return 'Acabou'

def generator(n=0, max=10):
    while True:
        yield n
        n += 1
        if n > max:
            return
        

gen = generator()

print('next(gen) > 1', next(gen) > 1)
print(next(gen))
for n in gen:
    print(f'n dentro do for', n)