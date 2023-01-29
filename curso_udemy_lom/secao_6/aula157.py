# Maria pegou um emprestimo de 1.000.000
# para realizar o pagamento em 5 anos
# A data em que ela pegou o emprestimo foi
# 20/12/2020 e o vencimento de cada parcela é no dia
# 20 de cada mes.
# Crie a data do emprestimo
# Cria a data do final do emprestimo
# Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime

from dateutil.relativedelta import relativedelta

fmt = 'Vencimento %d/%m/%Y'
valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

data_parcelas = []
data_parcela = data_emprestimo + relativedelta(months=1)

while data_parcela <= data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=1)

numero_parcelas = len(data_parcelas)
valor_parcelas = valor_total / numero_parcelas

for data in data_parcelas:
    print(f'{data.strftime(fmt)}, valor a pagar: R${valor_parcelas:,.2f}')

print(
    f'Você emprestou R${valor_total:,.2f} para pagar '
    f'em {delta_anos.years} anos ({numero_parcelas} meses), com '
    f'parcelas de R${valor_parcelas:,.2f}'
)
