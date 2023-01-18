# method vs @classmethod vs @staticmethod
# method - self, metodo de instancia
# @classmethod - cls, metodo de classe
# @staticmethod - metodo estatico (X self, X cls)
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    # se for definir algo de self, entao é metodo de instancia
    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.user = password


c1 = Connection()
c1.set_user()
c1.set_password()
