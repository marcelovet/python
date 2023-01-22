# Método __call__
# callable é algo que pode ser executado com parenteses
# Em classes normais, __call__ faz a instancia de uma classe ser "callable"
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, destino):
        print(self.phone, 'ligando para', destino)


call1 = CallMe('12345')
call1('4312')
