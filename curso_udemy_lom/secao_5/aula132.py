# classes abstratas - Abstract Base Class (abc)
# ABC são usadas como contratos para a definição de novas classes. Elas podem forçar
# outras classes a criarem metodos concretos. Também podem ter metodos concretos por elas mesmas.
# @abstractmethods sao metodos que nao tem corpo.
# As regras para classes abstratas com metodos abstratos é que elas NAO PODEM ser instanciadas diretamente.
# Metodos abstratos DEVEM ser implementados nas subclassses (@abstractmethod).
# Uma classe abstrata em python tem sua metaclasse sendo ABCMeta.
# É possivel criar @property @setter @classmethod @staticmethod e @method como abstratos,
# para isso use @abstractmethod como decorador mais interno
# Formas de criar classes abstratas:
from abc import ABC, abstractmethod

# forma 1:
# class Log(metaclass=ABCMeta): ABCMeta deve ser importado de abc

# forma 2:


class Log(ABC):
    @abstractmethod
    def _log(self, msg): ...

    def log_error(self, msg):
        self._log(f'Error: {msg}')

    def log_success(self, msg):
        self._log(f'Success: {msg}')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} (class {self.__class__.__name__})')


# l = Log() agora gera erro por ser abstrata
l = LogPrintMixin()
l.log_error('oi')
