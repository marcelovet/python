"""
Métodos split e join em strings
split - divide a string
join - une uma string
strip (lstrip, rstrip) - remove espaços em branco
"""
frase = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus dolor ligula, euismod eu lacinia sit amet, volutpat quis eros. Fusce tincidunt eros vel ultrices dapibus. Integer egestas, arcu at dictum lobortis, tellus felis consectetur nisl, eget tincidunt dolor libero quis nibh. Mauris ut maximus dolor. Nunc et mi cursus, bibendum mi ut, iaculis est. Vestibulum tincidunt imperdiet turpis, sit amet ullamcorper nulla auctor eu. Nulla vehicula ultrices sapien, vitae blandit nunc efficitur et. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nullam vitae risus finibus, dapibus sapien vitae, tempus quam. Donec vel quam augue. Donec molestie mi nisl. Curabitur lacinia nulla vel dapibus sagittis. Nulla facilisi.'''
lista_frases_cruas = frase.split('.')
lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

for i, frase in enumerate(lista_frases):
    print(f'{frase}.')

frases_unidas = '-'.join('doc')
print(frases_unidas)

frases_unidas = '. '.join(lista_frases)
print(frases_unidas)
