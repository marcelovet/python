# isinstance - verificar se o objeto é determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'fulano'}
]

for item in lista:
    if isinstance(item, str):
        print(item.upper())
    if isinstance(item, int):
        print(item + item)
    if isinstance(item, float):
        print(f'{item * item:.2f}')
    if isinstance(item, list):
        item.pop()
        print(item)
    if isinstance(item, set):
        item.add(5)
        print(item)
