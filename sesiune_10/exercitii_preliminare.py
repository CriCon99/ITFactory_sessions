'''
6. Să se tipărească toate numerele prime aflate între doi întregi citiţi.
Programul va folosi o funcţie care testează dacă un număr este prim sau nu.
'''

import math

# def is_prime(nr):
#     if nr < 2:
#         return False
#     # for i in range(2, nr//2 + 1): optimizare 1 : reducerea spatiului de cautare al nr pana la jumatatea lui nr + 1
#     for i in range(2, int(math.sqrt(
#             nr)) + 1):  # optimizare 2 reducerea spatiului de cautare si mai mult, pana la radical din nr
#         if nr % i == 0:
#             return False
#     return True
#
#
# def print_primes_between(start, end):
#     for n in range(start, end + 1):
#         if is_prime(n):
#             print(n)
#
#
# print_primes_between(4, 50)

'''
7. Scrieţi un program care tipăreşte numerele întregi găsite între două valori citite, numere care se divid cu suma cifrelor lor.
Programul va utiliza o funcţie care returnează suma cifrelor unui număr întreg primit ca parametru.
'''


def sum_digits(nr):
    s = 0
    while nr != 0:
        ultima_cifra = nr % 10
        # print(f' ultima cifra: {ultima_cifra}')
        s += ultima_cifra
        # print(f' suma: {s}')
        nr = nr // 10
        # print(f' nr: {nr}')
    return s


def print_numbers_divisible_by_digit_sum(start, end):
    for n in range(start, end + 1):
        if n % sum_digits(n) == 0:
            print(n)


print_numbers_divisible_by_digit_sum(1, 70)

sum_digits(123)
