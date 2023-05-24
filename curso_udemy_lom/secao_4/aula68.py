# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51', '43', '59'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    }
]

num_perguntas = len(perguntas)
num_acertos = 0
num_perguntas_respondidas = 0

while num_perguntas_respondidas < num_perguntas:
    questao_atual = perguntas[num_perguntas_respondidas]

    print('Pergunta:', questao_atual['Pergunta'], end='\n\n')

    print('Opções: ')
    for idx, valor in enumerate(questao_atual['Opções']):
        print(f'{idx}) {valor}')

    resposta_usuario = input('Escolha uma opção: ')

    try:
        idx_resposta = int(resposta_usuario)
    except ValueError:
        print('Escolha uma das opções fornecidas', end='\n\n')
        continue

    if idx_resposta not in range(0, len(questao_atual['Opções'])):
        print('Escolha uma das opções fornecidas', end='\n\n')
        continue

    if questao_atual['Opções'][idx_resposta] == questao_atual['Resposta']:
        print('Acertou', end='\n\n')
        num_acertos += 1
    else:
        print('Errou', end='\n\n')

    num_perguntas_respondidas += 1

print(f'Você acertou {num_acertos} de {num_perguntas} perguntas.')
