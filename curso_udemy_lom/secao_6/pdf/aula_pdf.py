# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

ROOT_PATH = Path(__file__).parent
ORIGINAL_PATH = ROOT_PATH / "pdfs_originais"
NEW_DIR_PATH = ROOT_PATH / "arquivos_novos"
NEW_DIR_PATH.mkdir(exist_ok=True)

ORIGINAL_PDF = ORIGINAL_PATH / "bacen.pdf"

reader = PdfReader(ORIGINAL_PDF)

print(len(reader.pages))
print(reader.pages[0].extract_text())
print(reader.pages[0].images[0])

extracted_img_path = NEW_DIR_PATH / reader.pages[0].images[0].name

with extracted_img_path.open(mode="wb") as image:
    image.write(reader.pages[0].images[0].data)

writer = PdfWriter()
writer.add_page(reader.pages[0])

with open(NEW_DIR_PATH / "page1.pdf", mode="wb") as file:
    writer.write(file)
