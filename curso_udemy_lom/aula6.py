# Conversão de tipos, coerção, type conversion,
# typecasting, coercion, são todos o mesmo tipo de ação
# É o ato de converter um tipo em outro
# Como python é dinâmico, ele usa + com polimorfismo
# para int e float ele usa como soma,
# para str ele usa como concatenação
print(1 + 1)
print('1' + '1')

# Tipos imutáveis e primitivos: str, int, float, bool
# print('1' + 1) gera erro porque ele não converte automático str para int e str + int = erro
print(int('1'), type(int('1')))
print(float('1'), type(float('1')))
print(bool('')) # str vazio é False
print(bool(' ')) # str não vazio é True
print(str(11) + 'b')
