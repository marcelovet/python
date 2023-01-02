# Exercicio de IMC
# ... é um placeholder que pode ser usado no código, por exemplo, em uma variável ainda sem um valor certo
# ... não gera erros
nome = 'Fulano de Tal'
altura = 1.8
peso = 95
imc = peso / (altura ** 2)

print(nome, 'tem', altura, 'de altura,\npesa', peso, 'quilos e seu IMC é', imc)
# usando o f-strings
linha_1 = f'{nome}, tem {altura:.2f} de altura,\npesa {peso} quilos e seu IMC é {imc:.2f}.'
print(linha_1)
