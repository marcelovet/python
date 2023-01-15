# try, except, else e finally
# try:
#     a = 18
#     b = 0
#     print('Linha 1') # ate o erro executa
#     c = a / b
#     print('Linha 2') # aqui ja n executa
# except: # o correto é definir qual erro ira tratar no except
#     print('Divisão por zero')

try:
    a = 18
    b = 0
    #print(b[0]) # TypeError (int nao tem indice)
    c = a / b
    print('Linha 2')
except ZeroDivisionError as error: # as define um alias para receber a msg do erro
    print('Divisão por zero')
    print('Nome do erro:', error.__class__.__name__)
    print('MSG:', error)
except NameError:
    print('Não definiu um nome')
except (TypeError, IndexError):
    print('TypeError, IndexError')
except Exception: # é um erro geral, o maior na hierarquia
    # se cair aqui ocorreu um erro qualquer diferente dos anteriores
    print('Erro desconhecido')

print('continuar')
