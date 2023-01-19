# method vs @classmethod vs @staticmethod
# method - self, metodo de instancia
# @classmethod - cls, metodo de classe
# @staticmethod - metodo estatico (X self, X cls)
class Connection:
    # metodo de instancia
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    # se for definir algo de self, entao é metodo de instancia
    # esse é um exemplo de setter
    def set_user(self, user):
        self.user = user

    # metodo de instancia
    def set_password(self, password):
        self.user = password

    # metodo de classe
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.user = password
        return connection

    @staticmethod
    def log(msg):
        return print(f'Essa é a mensagem de log:\n{msg}')


c1 = Connection()
print(c1.user)
c1.set_user('usuario')
print(c1.user)
c1.set_password('senha')

c2 = Connection.create_with_auth('marcelo', '123')
print(c2.user)
print(c2.password)
Connection.log('Erro de acesso')
