# ZIP compactando e descompactando arquivos com zipfile
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# paths
PATH_ROOT = Path(__file__).parent.parent
PATH_ZIP_DIR = PATH_ROOT / "aula186_diretorio_zip"
PATH_ZIPPED = PATH_ROOT / "aula186_compactado.zip"
PATH_UNZIPPED = PATH_ROOT / "aula186_descompactado"

shutil.rmtree(PATH_ZIP_DIR, ignore_errors=True)
Path.unlink(PATH_ZIPPED, missing_ok=True)
shutil.rmtree(str(PATH_ZIPPED).replace(".zip", ""), ignore_errors=True)
shutil.rmtree(PATH_UNZIPPED, ignore_errors=True)

PATH_ZIP_DIR.mkdir(exist_ok=True)


def create_empty_files(num: int, zip_dir: Path) -> None:
    for i in range(1, num + 1):
        filename = f"file_{i}.txt"
        file_path = zip_dir / filename
        file_path.touch(exist_ok=True)


create_empty_files(10, PATH_ZIP_DIR)

# creates zip and add files
with ZipFile(PATH_ZIPPED, mode="w") as zip:
    for root, dirs, files in os.walk(PATH_ZIP_DIR):
        for file in files:
            path_ = Path(root) / file
            zip.write(path_, file)

# reads zip files and extract contents to a Path
with ZipFile(PATH_ZIPPED, mode="r") as zip:
    for i in zip.namelist():
        print(i)
    zip.extractall(PATH_UNZIPPED)
