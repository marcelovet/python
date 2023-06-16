# csv.writer e csv.DictWriter para escrever o csv
import csv
from pathlib import Path

CSV_PATH = Path(__file__).parent / "aula180.csv"

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

with CSV_PATH.open(mode='w', encoding='utf-8') as file:
    writer = csv.writer(file, lineterminator="\n")

    col_names = lista_clientes[0].keys()
    writer.writerow(col_names)

    for line in lista_clientes:
        writer.writerow(line.values())


with CSV_PATH.open(mode='w', encoding='utf-8') as file:
    col_names = lista_clientes[0].keys()
    writer = csv.DictWriter(file, fieldnames=col_names, lineterminator="\n")

    writer.writeheader()

    for line in lista_clientes:
        writer.writerow(line)

    # ou
    # writer.writerows(lista_clientes)
