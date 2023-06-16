# csv.reader e csv.DictReader
# csv.reader le em formato de lista
# csv.DictReader le em formato de dicionario
import csv
from pathlib import Path

FILE_PATH = Path(__file__).parent / "aula179.csv"

with FILE_PATH.open(mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)

    for line in reader:
        print(line)


with FILE_PATH.open(mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for line in reader:
        print(line)
        print(line["Nome"])
        print(
            f"{line['Nome']} tem {line['Idade']} anos"
            f" e mora em: {line['Endereço']}"
        )
