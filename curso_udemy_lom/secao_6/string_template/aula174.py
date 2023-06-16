# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.
import locale
import string
from datetime import datetime
from pathlib import Path

locale.setlocale(locale.LC_ALL, "pt_BR")


def to_brl_currency(number: float | int) -> str:
    brl = 'R$ ' + locale.currency(val=number, symbol=False, grouping=True)
    return brl


client_data = dict(
    nome='João',
    valor=to_brl_currency(1_234_456),
    data=datetime(2022, 12, 28).strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)

default_text = """
Prezado(a) $nome,

Informamos que sua mensalidade será cobrada no valor de ${valor} no dia $data.
Caso deseje cancelar o serviço, entre em contato com a $empresa pelo telefone $telefone.

Atenciosamente,

${empresa},
Abracos
"""

template = string.Template(default_text)
print(template.substitute(client_data))

MSG_PATH = Path(__file__).parent / "aula174.txt"

with MSG_PATH.open(mode="r", encoding='utf-8') as file:
    default_text = file.read()
    template = string.Template(default_text)
    print(template.safe_substitute(client_data))
