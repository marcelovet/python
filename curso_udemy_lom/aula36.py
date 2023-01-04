"""
Qual a letra que mais apareceu na frase?
"""

frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido von Rossum.'

i = 0
letra_mais_freq = ''
numero_ocorrencias = 0

while i < len(frase):
    letra_atual = frase[i].lower()
    
    if letra_atual == letra_mais_freq or letra_atual in ' ,.;/?*':
        i += 1
        continue
    
    numero_ocorrencias_atual = frase.lower().count(letra_atual)

    if numero_ocorrencias_atual > numero_ocorrencias:
        
        frase_print = f'{letra_atual} aparece {numero_ocorrencias_atual}, ' \
            f'enquanto {letra_mais_freq} apareceu {numero_ocorrencias}.'
        
        if i != 0: print(frase_print)
        
        numero_ocorrencias = numero_ocorrencias_atual
        letra_mais_freq = letra_atual

    i += 1

print(f'A letra que mais apareceu na frase ({numero_ocorrencias}) foi {letra_mais_freq}.')
