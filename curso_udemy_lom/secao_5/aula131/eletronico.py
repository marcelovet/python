from log import LogFileMixin, LogPrintMixin


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False


class Smartphone(Eletronico, LogFileMixin):
    def ligar(self):
        if self._ligado:
            msg = f'{self._nome} já está ligado'
            return self.log_error(msg)
        super().ligar()
        msg = f'{self._nome} foi ligado'
        return self.log_success(msg)

    def desligar(self):
        if not self._ligado:
            msg = f'{self._nome} já está desligado'
            return self.log_error(msg)
        super().desligar()
        msg = f'{self._nome} foi desligado'
        return self.log_success(msg)
