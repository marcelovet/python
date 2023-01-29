# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'

data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:30', fmt)
print(data_inicio > data_fim)
print(data_fim - data_inicio)
diff1 = data_fim - data_inicio
print(diff1.days, diff1.seconds)
print(diff1.total_seconds())
delta = timedelta(days=10)
print(data_fim, " e ", data_fim + delta)
print(data_fim, " e ", data_fim + relativedelta(weeks=2))
print(data_fim, " e ", data_fim + relativedelta(months=2))
diff2 = relativedelta(data_fim, data_inicio)
print(diff2)
print(diff2.days, type(diff2.days))
