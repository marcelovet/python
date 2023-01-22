# Criando Exceptions em Python Orientado a Objetos
# Para criar uma exceção em python, voce so precisa herdar de alguma
# exececao da linguagem.
# A recomendacao da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando excecoes (Comum colocar Error ao final)
# Levantando (raise) no python / lançando (throw) em algumas linguagens
# Relancando excecoes
# Adicionando notas em excecoes (3.11.0)
class MeuError(Exception):
    ...


class OutroError(Exception):
    ...


def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('Uma note 1')
    exception_.add_note('Voce gerrou esse erro aqui')
    raise exception_


try:
    levantar()
except MeuError as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('Vou lançar de novo')
    exception_.add_note('Mais uma informação')
    exception_.__notes__ += error.__notes__.copy()
    raise exception_ from error
