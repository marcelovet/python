"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade
para o usuário digitar apenas uma letra
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
- Se a letra digitada estiver na palavra secreta, exiba a letra;
- Se não estiver, exiba *.
Faça a contagem de tentativas do seu usuário
"""
import os

palavra_secreta = 'Cachorro'
letras_acertadas = ''
tentativas = 0

print('Iniciando o jogo de adivinhação')

while True:
    letra_do_chute = input('Digite uma letra da palavra secreta: ')
    comprimento_str = len(letra_do_chute)

    while comprimento_str == 0 or comprimento_str > 1:
        if comprimento_str == 0:
            print('Preciso que você digite algo para que eu verifique se acertou.')
            letra_do_chute = input('Digite uma letra da palavra secreta: ')
            comprimento_str = len(letra_do_chute)
        elif comprimento_str > 1:
            print('Você só pode digitar uma letra.')
            letra_do_chute = input('Digite uma letra da palavra secreta: ')
            comprimento_str = len(letra_do_chute)

    tentativas +=1

    if tentativas == 1:
        print('Essa foi sua primeira tentativa de acerto')
    else:
        print(f'Você fez {tentativas} tentativas de acerto.')
    
    if letra_do_chute in palavra_secreta:
        letras_acertadas += letra_do_chute.lower()

    palavra_formada = ''
    
    for letra_secreta in palavra_secreta.lower():
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print(palavra_formada)
    if palavra_formada == palavra_secreta.lower():
        os.system('clear')
        print(f'Parabéns!\nVocê acertou a palavra secreta com {tentativas} tentativas.')
        
        finaliza_jogo = input('Deseja finalizar o jogo? [s]im: ')
        if finaliza_jogo.lower() == 's':
            print('Finalizando o jogo...')
            break
        else:
            letras_acertadas = ''
            tentativas = 0
