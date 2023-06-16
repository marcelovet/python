# secrets gera numeros aleatorios seguros
import secrets
import string as s
from secrets import SystemRandom as Sr

# criando um senha forte aleatoria
print(s.ascii_letters + s.digits + s.punctuation)
print(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12))
print(
    "".join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12))
)

# print(secrets.randbelow(100))
# print(secrets.choice([1, 5, 8]))
# usando o secrets.SystemRandom() podemos conseguir as mesmas
# funcionalidades do random (modulo), mas com mais seguranca
random = secrets.SystemRandom()

random.seed(0)  # nao trava a 'aleatoriedade'

r_range = random.randrange(10, 20, 2)
print(r_range)

r_int = random.randint(10, 20)
print(r_int)

r_uniform = random.uniform(10, 20)
print(r_uniform)

nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
random.shuffle(nomes)

novos_nomes = random.sample(nomes, k=2)
print(nomes)
print(novos_nomes)

novos_nomes = random.choices(nomes, k=3)
print(nomes)
print(novos_nomes)

print(random.choice(nomes))
