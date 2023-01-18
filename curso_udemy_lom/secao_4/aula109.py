# Fazer uma todo list
# ela deve ter as opções de listar tarefas,
# desfazer (remover o ultimo inserido)
# refazer (retorna à todo list o ultimo removido)
def create_function(func, x):
    def intern(y, str):
        return func(x, y, str)
    return intern

def undo_redo(list1, list2, str):
    if len(list2) == 0:
        return print(str)
    list1.append(list2[-1])
    return list2.pop()

todo_list = []
undo_redo_list = []

undo = create_function(undo_redo, undo_redo_list)
redo = create_function(undo_redo, todo_list)

def commands(input_command, todo_list):
    if input_command == 'listar' and len(todo_list) > 0:
        return print(*todo_list, sep=';\n', end='.\n\n')
    if input_command == 'listar' and len(todo_list) == 0:
        return print('Nada na lista ainda', end='\n\n')
    elif input_command == 'desfazer':
        return undo(todo_list, 'Nada a desfazer\n')
    elif input_command == 'refazer':
        return redo(undo_redo_list, 'Nada a refazer\n')
    return todo_list.append(input_command)

while True:
    print('Comandos: listar, desfazer, refazer')
    
    user_response = input('Digite uma tarefa ou comando: ')
    
    if user_response.lower() == 'fechar':
        break
    else: commands(user_response.lower(), todo_list)

