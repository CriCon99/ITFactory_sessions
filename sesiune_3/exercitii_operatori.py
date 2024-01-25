'''
21. Având stringul '0123456789'
Afișează doar numerele pare
Afișează doar numerele impare
(hint: folosește slicing, controlează din pas)
'''

# string = '0123456789'
#
# print(string[::2])
# print(string[1::2])


'''
20.  Citește de la tastatură un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat
'''

# string = input('Introdu un string: ')
# assert string[0].lower() == string[-1].lower()


'''
19. Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Ia numărul ghicit de la utilizator
Verifică și afișează dacă utilizatorul a ghicit
Vei avea 3 opțiuni
Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
Ai ghicit. Felicitări! Ai ales x si zarul a fost y.
'''

# import random
#
# zar = random.randint(1, 6)
#
# incercare = int(input('introdu un numar intre 1 si 6: '))
#
# if incercare < zar:
#     print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {incercare} dar a fost {zar}.')
# elif incercare > zar:
#     print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {incercare} dar a fost {zar}.')
# else:
#     print('Ai ghicit!')

'''
18. Același string. 
Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
output: 'Coral is either the stupidest animal or the smartest' 
'''

# string = 'Coral is either the stupidest animal or the smartest rock'
#
# index = string.find("rock")
# print(index)
# print(string[:53])

'''
17. Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5.
'''
#
# string = 'Coral is either the stupidest animal or the smartest rock'
#
# string_nou = string[:5] + string[-5:]
# print(string_nou)

'''
16. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
Citește de la tastatură un int x
Afișează stringul fără ultimele x caractere
Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'
'''

# string = 'Coral is either the stupidest animal or the smartest rock'
#
# x = int(input('Introdu un numar: '))
#
# print(string[:-x])

'''
15. 
X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.
'''

# x, y, z = 60, 30, 90
#
# if x + y + z == 180:
#     print('Triunghiul este valid')
# else:
#     print('Triunghiul este invalid')


'''
14. x, y, z (int)
Afișează care este cel mai mare dintre ele?
'''

# x, y, z = 60, 30, 90
#
# if x > y and x > z:
#     print('x este cel mai mare')
# elif y > x and y > z:
#     print('y este cel mai mare')
# else:
#     print('z este cel mai mare')

'''
13.Verifică dacă x este număr par sau impar (x e int).
'''

# x = 9
#
# if x % 2 == 0:
#     print('x este par')
# else:
#     print('x este impar')

'''
12.Verifică dacă x are exact 6 cifre.
'''

# x= 1234567
#
# numar_exact = len(str(x))
#
# if numar_exact == 6:
#     print('x are exact 6 cifre')
# else:
#     print('x nu are exact 6 cifre')

'''
11.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
'''

# x = 12345678
#
# cifre_x = len(str(x))
#
# if cifre_x < 4:
#     print('x nu are minim 4 cifre')
# else:
#     print('x are minim 4 cifre')

'''
10.Transformă și printează notele din sistem românesc în  >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
'''

# nota_ro = 2
#
# if 1 <= nota_ro <= 4:
#     print('F')
# elif 4 < nota_ro <= 6:
#     print('E')
# elif 6 < nota_ro <= 7:
#     print('D')
# elif 7 < nota_ro <= 8:
#     print('C')
# elif 8 < nota_ro < 9:
#     print('B')
# else:
#     print('A')

'''
9. Citește o literă de la tastatură.
    Verifică și afișează dacă este vocală sau nu.
'''

# x = input('introdu o litera: ')
#
# if x in 'a,e,i,o,u,A,E,I,O,U':
#     print('litera introdusa este o vocala')
# else:
#     print('litera introdus nu este o vocala')


'''
8. 
X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
'''

x, y, z = 60, 70, 80

if x == y == z:
    print("Triunghiul este echilateral")
elif x == y or x == z or y == z:
    print("Triunghiul este isoscel")
else:
    print("Triunghiul este oarecare")
