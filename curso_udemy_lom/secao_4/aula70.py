"""
Exercicio
Crie uma funcao que encontra o primeiro duplicado considerando o segundo numero como a duplicacao.
Retorne a duplicacao considerada.
Requisitos:
    A ordem do numero duplicado é considerada a partir da segunda ocorrencia do numero
    ex.:
        [1, 2, 3, ->3<-, 2, 1] -> retorne 3
        [1, 2, 3, 4, 5, 6] -> não tem duplicados, retorne -1
        [1, 4, 9, 8, ->9<-, 4, 8] -> retorne 9
"""
lista_de_lista_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


for lista_de_inteiros in lista_de_lista_de_inteiros:
    set_de_inteiros = set(lista_de_inteiros)
    print(lista_de_inteiros)

    if len(lista_de_inteiros) == len(set_de_inteiros):
        print('-1')
        continue

    idx_item_duplicado = []

    for item in set_de_inteiros:
        idx_item = None

        for idx, inteiro in enumerate(lista_de_inteiros):
            if item == lista_de_inteiros[idx] and idx_item is None:
                idx_item = idx
            elif item == lista_de_inteiros[idx] and idx_item is not None:
                idx_item_duplicado.append(idx)

    indice = None

    for i in idx_item_duplicado:
        if indice is None:
            indice = i
        elif i < indice:
            indice = i

    print(lista_de_inteiros[indice])
