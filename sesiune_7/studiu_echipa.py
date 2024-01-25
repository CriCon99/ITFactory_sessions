'''
13. Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
   User alege un număr
   Programul îi spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitări! Ai ghicit!
'''

import random

numar_secret = random.randint(1, 30)

numar_ghicit = 0


while numar_ghicit != numar_secret:
    numar_ghicit = int(input("Ghiceste numărul secret: "))
    if numar_ghicit < numar_secret:
        print("Numărul secret este mai mare.")
    elif numar_ghicit > numar_secret:
        print("Numărul secret este mai mic.")
    else:
        print("Felicitări! Ai ghicit!")



'''
14. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
'''

# nr = int(input('Introdu un numar de la tastatura: '))
# for i in range(1, nr + 1):
#     print(str(i) * i)

'''
15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterează prin listă 2d
Printează ‘Cifra curentă este x’
(hint: nested for - adică for în for)
'''
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]

