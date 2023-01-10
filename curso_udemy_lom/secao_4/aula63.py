"""
High order functions - Funções que podem receber e/ou retornar outras funções
First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args): # é parecido com o ... no R
    return funcao(*args)

v = executa(saudacao, "Bom dia", "Luiz")
print(v)
