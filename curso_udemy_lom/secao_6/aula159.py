# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
import calendar
import locale

# primeiro argumento é a categoria que pretende mudar
# o segundo é o locale que ao deixar '' define pelo locale do sistema
# no shell:
# locale -a retorna as locales do sistema
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
locale.setlocale(locale.LC_ALL, '')

print(calendar.calendar(2022))
