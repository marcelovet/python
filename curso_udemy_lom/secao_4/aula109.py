# Fazer uma todo list
# ela deve ter as opções de listar tarefas,
# desfazer (remover o ultimo inserido)
# refazer (retorna à todo list o ultimo removido)
import json
import os

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'aula109.json')


def create_function(func, x):
    def intern(y, str):
        return func(x, y, str)
    return intern


def undo_redo(list1, list2, str):
    if len(list2) == 0:
        return print(str)
    list1.append(list2[-1])
    return list2.pop()


def read_todo_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            todo_list = json.load(file)
        return todo_list
    except FileNotFoundError:
        print('Nenhuma lista de tarefa encontrada, inciando uma lista de tarefas...')
        todo_list = []
        return todo_list


def save_todo(path, todo_list):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(todo_list, file, ensure_ascii=False, indent=2)


todo_list = read_todo_file(SAVE_TO)
undo_redo_list = []

undo = create_function(undo_redo, undo_redo_list)
redo = create_function(undo_redo, todo_list)


def read_todo(todo_list):
    if not todo_list:
        print('Nenhuma tarefa na lista', end='\n\n')
        return
    print('Tarefas:')
    for i in todo_list:
        print(f'-  {i}')


def commands(input_command, todo_list):
    # if input_command == 'listar':
    #     return read_todo(todo_list)
    # if input_command == 'desfazer':
    #     return undo(todo_list, 'Nada a desfazer\n')
    # if input_command == 'refazer':
    #     return redo(undo_redo_list, 'Nada a refazer\n')
    # return todo_list.append(input_command)
    comandos_aceitos = ['listar', 'desfazer', 'refazer', 'clear']
    comandos = {
        'listar': lambda: read_todo(todo_list),
        'desfazer': lambda: undo(todo_list, 'Nada a desfazer\n'),
        'refazer': lambda: redo(undo_redo_list, 'Nada a refazer\n'),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: todo_list.append(input_command),
    }

    comando = comandos.get(input_command) if input_command in comandos_aceitos else \
        comandos['adicionar']

    if input_command not in ['listar', 'clear']:
        comando()
        return save_todo(SAVE_TO, todo_list)
    return comando()


while True:
    print('Comandos: listar, desfazer, refazer')

    user_response = input('Digite uma tarefa ou comando: ')

    if user_response.lower() == 'fechar':
        break
    else:
        commands(user_response.lower(), todo_list)
