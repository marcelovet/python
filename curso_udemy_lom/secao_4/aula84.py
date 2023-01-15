# try, finally
# pode ser try - finally, ou try - except - finally
# HIERARQUIA DE EXCEÇÔES
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    print(1)
    a = 8 / 0
except ZeroDivisionError:
    print('erro aqui')
except Exception:
    print('erro')
else:
    print('Nao deu erro')
finally:
    print('Independe de dar ou não algum erro')
