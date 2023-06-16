# Abstracao
# a classe Log em si nao deve ser usada - ela sera uma heranca de outra, que sera a abstracao dela
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        self._log(f'Error: {msg}')

    def log_success(self, msg):
        self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} (class {self.__class__.__name__})\n'
        with LOG_FILE.open('a', encoding='utf-8') as file:
            file.write(msg_formatada)


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} (class {self.__class__.__name__})')


if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Um erro')
    lp.log_success('Um sucesso')
    lf = LogFileMixin()
    lf.log_error('Um erro')
    lf.log_success('Um sucesso')
