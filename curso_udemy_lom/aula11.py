# Precedencia de operadores
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = 1 + 1 ** 5 + 5 # 1 elevado a 5, somado a 1 e depois somado a 5
print(conta_1)

conta_2 = (1 + 1) ** (5 + 5) # 2 elevado a 10
print(conta_2)
