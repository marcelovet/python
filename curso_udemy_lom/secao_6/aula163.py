# os.path.getsize e os.stat para dados dos arquivos
import math
import os


def formata_tamanho(tamanho_em_bytes: int, base: int = 1024) -> str:
    """Formata uma tamanho, de bytes para o tamanho apropriado"""

    # Se o tamanho for menor ou igual a 0, 0B
    if tamanho_em_bytes <= 0:
        return "0B"
    abreviacao_tamanhos = ("B", "KB", "MB", "GB", "TB", "PB")
    # math.log vai retornar o logaritmo do tamanho_em_bytes
    # com a base (1024 por padrão), isso deve bater
    # com o nosso indice na abreviacao dos tamanhos
    indice_abreviacao_tamamanhos = int(math.log(tamanho_em_bytes, base))
    # por quanto nosso tamanho deve ser dividido
    # para gerar o tamanho correto
    potencia = base ** indice_abreviacao_tamamanhos
    # tamanho final
    tamanho_final = round(tamanho_em_bytes / potencia, 2)
    # abreviacao
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamamanhos]
    return f'{tamanho_final} {abreviacao_tamanho}'


caminho = '/home/ubuntu-py/Desktop/curso/curso_udemy_lom/'

for root, dirs, files in os.walk(caminho):
    print('Pasta atual', root)

    for file_ in files:
        path = os.path.join(root, file_)
        # tamanho = os.path.getsize(path)
        stat = os.stat(path)
        print('    ', 'File:', file_,
              'tamanho:', formata_tamanho(stat.st_size))
