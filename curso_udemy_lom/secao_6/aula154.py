# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime

from pytz import timezone

data = datetime(2022, 4, 20, 12, 3, 7)
print(data)
data = datetime.strptime('01/12/2023', '%d/%m/%Y')
print(data)
str_data = '01/12/2023 às 7 horas'
fmt = '%d/%m/%Y às %H horas'
data = datetime.strptime(str_data, fmt)
print(data)
print(datetime.now(timezone('Asia/Tokyo')))
# falando explicitamente que é tz do brasil
data = datetime(2020, 2, 1, tzinfo=timezone('Asia/Tokyo'))
print(data)
# segundos desde 1970-00-00
print(data.timestamp())
print(datetime.fromtimestamp(data.timestamp(), tz=timezone('Asia/Tokyo')))
