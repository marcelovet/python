"""
Flag (bandeira) - marcar um local
None = não valor
is ou is not = é ou não é
id = identidade
id é o local na memória onde o objeto aponta
"""
v1 = 'a'
print(id(v1))

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
