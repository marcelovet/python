# dir, hasattr, getattr
# dir exibe os métodos para aquele objeto
# hasattr - verifica se tem um método
# getattr - disponibiliza o metodo
string = 'fulano'
metodo = 'uppr'

if hasattr(string, metodo):
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)
