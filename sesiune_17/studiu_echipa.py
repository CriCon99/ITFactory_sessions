'''
1. Sa se genereze primele 100 de numere prime folosind liste, si apoi folosind generator. Comparati diferenta de timp necesara generarii.

2. Scrieti un decorator care primeste ca argument numele unui fisier si pentru orice functie apelata, el va scrie in acel fisier numele functiei, lista de argumente ca si string si rezultatul apelului. Fisierul este de tip csv. Functiile decorate pot primi oricate argumente

3.Sa se creeze un iterator care sa mimice functia enumerate.
ex:

for index, letter in enumerate('abc'):
    print(f"{index} : {letter}")
'''
from contextlib import contextmanager
from time import perf_counter

primes = []
număr = 2
while număr <= 100:
    este_prim = True
    for i in range(2, număr):
        if număr % i == 0:
            este_prim = False
            break
    if este_prim:
        primes.append(număr)
    număr += 1

@contextmanager
def timer():
    start = perf_counter()
    yield
    print(f'A durat {perf_counter() - start} secunde')

with timer():
    print(primes)