"""
Faça uma lista de compras
O usuário deve ter a possibilidade de:
inserir, apagar e listar itens de sua lista
Não permita que programa quebre com erros de indices inexistentes
"""
import os

lista_compra = []
opcoes_permitidas = ["i", "a", "l", "f"]

while True:
    tamanho_lista = len(lista_compra)

    print('Selecione uma opção:')
    opcao_do_usuario = input('[i]nserir [a]pagar [l]istar [f]inalizar ')

    if opcao_do_usuario.lower() not in opcoes_permitidas:
        os.system('clear')
        print('Você deve selecionar uma opção válida!')
        continue
    elif opcao_do_usuario.lower() in 'i':
        os.system('clear')        
        print(f'{"-" * 10}Inserir novo item na lista{"-" * 10}')
        novo_item = input("Digite o item que deseja inserir: ")
        lista_compra.append(novo_item)
    elif opcao_do_usuario.lower() in 'a':
        os.system('clear')
        if tamanho_lista > 0:
            print(f'{"-" * 10}Apagar item da lista{"-" * 10}')
            idx_p_apagar = input("Digite o indice que deseja apagar: ")
            try:
                idx_p_apagar = int(idx_p_apagar)
                lista_compra.pop(idx_p_apagar)
            except IndexError:
                print(f'{"-" * 10}Não há item nesse índice{"-" * 10}')
            except ValueError:
                print(f'{"-" * 10}Índices devem ser o números inteiros{"-" * 10}')
        else:
            print(f'{"-" * 10}Não há itens na sua lista para apagar{"-" * 10}')
            continue
    elif opcao_do_usuario.lower() in 'l':
        os.system('clear')
        print(f'{"-" * 10}Listar itens{"-" * 10}')
        if tamanho_lista == 0:
            print(f'{"-" * 10}Não há itens na sua lista{"-" * 10}')
        for indice, item in enumerate(lista_compra):
            print(indice, item)
    else:
        os.system('clear')
        print(f'Finalizando o programa, até mais.')
        break
