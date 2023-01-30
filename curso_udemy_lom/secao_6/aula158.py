# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo
import calendar

# print(calendar.calendar(2022))
print(calendar.month(2022, 12))
print(
    calendar.monthrange(2022, 12),
    'dia da semana no dia 1 (começando em 0 o weekday) e ultimo dia do mes'
)

for value, day in enumerate(calendar.day_name):
    print(f'weekday value={value}, name={day}')

print(calendar.day_name[2])
print(calendar.weekday(2012, 12, 30))
print(calendar.day_name[calendar.weekday(2012, 12, 30)])
print(list(enumerate(calendar.monthcalendar(2022, 12))))

month = []

for week_num, week in enumerate(calendar.monthcalendar(2022, 12)):
    # print(list(enumerate(week)))
    minhas_semanas = [
        {'weekday': calendar.day_name[weekday], 'monthday': month_day}
        for weekday, month_day in enumerate(week)
        if month_day > 0
    ]
    month.append({'week': week_num, 'days': minhas_semanas})

# print(*month[0].get('days'), sep='\n')

for month_lb in month:
    w = month_lb['week']
    print(f'Semana: {w + 1}')
    print(*month_lb['days'], sep='\n')
