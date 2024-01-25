import math

'''
1. Scrieţi o funcţie care primeşte ca parametru lungimea laturii unui pătrat şi returnează aria sa.
'''

# def area_of_square(l):
#     return l*l
#
# area = area_of_square(2)
# print(area)

'''
2. Scrieţi un subprogram care primeşte ca parametru lungimea laturii unui pătrat şi returnează atât lungimea diagonalei, cât şi perimetrul pătratului.
'''
# def perimeter(l):
#     return l*4
# def diagon(l):
#     return math.sqrt(2 * l)
# p = perimeter(4)
# d = diagon(4)
# print(p)
# print(d)

'''
3. Scrieţi o funcţie care primeşte ca parametri de intrare lungimile celor două catete ale unui triunghi dreptunghic şi returnează lungimea ipotenuzei.
'''


# def ipotenuza(c_1, c_2):
#     return math.hypot(c_1, c_2)
#
#
# ip = ipotenuza(3, 4)
# print(ip)

'''
4. Scrieţi o funcţie care primeşte 3 parametri de tip real, cu semnificaţia de lungimi pentru 3 segmente. Funcţia va returna 1 dacă cele trei segmente pot forma un triunghi şi 0, în caz contrar.
'''


def can_be_triangle(a, b, c):
    if a + b <= c or a + c <= c or b + c <= a:
        return 0
    else:
        return 1


tri = can_be_triangle(2,2,4)
print(tri)