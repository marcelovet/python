# Polimorfismo em Python Orientado a Objetos
# polimorfismo é o principio que permite que classes derivadas de uma
# mesma superclasse tenham metodos iguais (com mesma assinatura), mas
# mas comportamentos diferentes.
# Assinatura do metodo => mesmo nome e quantidade de parametros
# Opiniao + principios que contam:
# Assinatura do metodo => nome, parametros, retornos iguais
# SO"L"ID
# L de Liskov Substitution Principle - Principio da substituicao de liskov
# Objetos de uma superclasse devem ser substituiveis por objetos de uma
# subclasse sem quebrar a aplicacao
# Sobrecarga de metodos (overload) = python nao suporta
# Sobreposicao de metodos (override) = python suporta
from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print(f'E-mail\nEnviando: {self.mensagem}')
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print(f'SMS\nEnviando: {self.mensagem}')
        return True


# Aqui o exemplo do polimorfismo
# notificar é do tipo Notificar, entao, independente da subclasse
# utilizada, NotificacaoEmail ou NotificacaoSMS, o codigo deve
# continuar funcionando
def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()
    if notificacao_enviada:
        print('Notificacao Enviada')
        return

    return print('Notificacao Nao Enviada')


n_email = NotificacaoEmail('testando notificao')
notificar(n_email)

n_sms = NotificacaoSMS('testando notificao')
notificar(n_sms)
