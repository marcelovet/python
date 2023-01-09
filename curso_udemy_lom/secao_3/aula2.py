# os valores abaixo são argumentos não nomeados
# enquanto sep é um argumento nomeado
print(12, 34, sep='')
print(56, 78, sep='-')
# Modos de quebra de linha
# \r\n -> CRLF, em windows mais antigos
# \n -> LF, em unix
print(9, 10, sep='-', end=', ')
print(11, 12, sep='-', end='\n')
