"""
Validação do primeiro dígito do CPF
CPF: 746.824.890-70
Como validar os dígitos após o - no CPF?
Primeiro digito (o valor 7 desse exemplo)

Colete a soma do produto dos 9 primeiros digitos do cpf e uma contagem regressiva
começando em 10

contagem 10  9  8  7  6  5  4  3 2
     cpf  7  4  6  8  2  4  8  9 0
    prod 70 36 48 56 12 20 32 27 0
    soma 70+36+48+56+12+20+32+27+0 = 301

Multiplique por 10 e obtenha o resto da divisão por 11

(301 * 10) % 11 = 7
Se o resultado for maior que 9:
    o primeiro digito é 0
Se não:
    o primeiro digito é o resultado da conta

Validação do segundo dígito do CPF
CPF: 746.824.890-70
Segundo digito (o valor 0 desse exemplo)

Colete a soma do produto dos 9 primeiros digitos do cpf + o primeiro digito
e uma contagem regressiva
começando em 11

contagem 11 10  9  8  7  6  5  4  3  2
     cpf  7  4  6  8  2  4  8  9  0  7
    prod 77 40 54 64 14 24 40 36  0 14
    soma 77+40+54+64+14+24+40+36+0+14 = 363

Multiplique por 10 e obtenha o resto da divisão por 11

(363 * 10) % 11 = 0
Se o resultado for maior que 9:
    o primeiro digito é 0
Se não:
    o primeiro digito é o resultado da conta
"""
import re
import sys

cpf_informado = '746.824.894-01'

"""
cpf_sem_simb = cpf_informado.split('.')
cpf_sem_simb = ''.join(cpf_sem_simb)
"""
cpf_sem_simb = cpf_informado.replace('.', '')

cpf_so_dig = re.sub(
    r'[^0-9]', # o padrão que quero identificar
    '', # pelo que vou substituir
    cpf_informado # onde vou procurar
)

entrada_e_igual = cpf_so_dig == cpf_so_dig[0] * len(cpf_so_dig)

print(f'{cpf_so_dig}') # também poderia usar regex para ter somente digitos

if entrada_e_igual:
    print('O CPF é inválido')
    sys.exit()

# processamento do segundo digito
cpf_inicial = enumerate(cpf_sem_simb[:-3])
prim_digito_informado = int(cpf_sem_simb[-2])
soma_cpf = 0

for i in range(10, 1, -1):
    x = next(cpf_inicial)
    soma_cpf += (i * int(x[1]))

int_validador = (soma_cpf * 10) % 11
prim_digito_correto = prim_digito_informado if int_validador <= 9 else 0
prim_validado = prim_digito_informado == prim_digito_correto

print(f'O primeiro digito correto para essa sequência de números é: {prim_digito_correto}')

# processamento do segundo digito
cpf_inicial = enumerate(cpf_sem_simb[:-3] + cpf_sem_simb[-2])
seg_digito_informado = int(cpf_sem_simb[-1])
soma_cpf = 0

for i in range(11, 1, -1):
    x = next(cpf_inicial)
    soma_cpf += (i * int(x[1]))

int_validador = (soma_cpf * 10) % 11
seg_digito_correto = seg_digito_informado if int_validador <= 9 else 0
seg_validado = seg_digito_informado == seg_digito_correto

print(f'O segundo digito correto para essa sequência de números é: {seg_digito_correto}')

if prim_validado and seg_validado:
    print('O primeiro e segundo digitos do cpf informado são válidos')
elif prim_validado and not seg_validado:
    print('Somente o primeiro digito do cpf informado é válido')
elif not prim_validado and seg_validado:
    print('Somente o segundo digito do cpf informado é válido')
else:
    print('Ambos os digitos são inválidos')
