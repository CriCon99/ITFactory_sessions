'''
7. Citește de la tastatură:
lungimea;
lățimea.
   Afișează: 'Aria dreptunghiului este x'
   Formula arie: L*l
'''

# L = int(input('Lungimea: '))
# l = int(input('latimea: '))
#
# print(f'Aria dreptunghiului este  {l * L}')

'''
8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
afișează de câte ori apare cuvântul 'the';
'''
# string = 'Coral is either the stupidest animal or the smartest rock'
# #
# # print(string.count(' the '))

'''
9. Același string:
inlocuieste 'the' cu 'THE' peste tot
Printează rezultatul.
'''
# string = 'Coral is either the stupidest animal or the smartest rock'
#
# print(string.replace('the', 'THE'))


'''
10. Același string:
Folosește un assert ca să verifici dacă acest string conține doar numere.
'''
# string = 'Coral is either the stupidest animal or the smartest rock'
#
# assert string.isdigit()

'''
11. Exercițiu:
citește de la tastatură un string de dimensiune impară;
afișează caracterul din mijloc.
'''

# string = input('Introdu un string: ')
# # a b c d e
# # 0 1 2 3 4
#
# index_mijloc = len(string) // 2
# print(string[index_mijloc])


'''
12. Folosind o singură linie de cod :
citește un string de la tastatură (ex: 'alabala portocala');
salvează fiecare cuvânt într-o variabilă;
printează ambele variabile pentru verificare.
'''

# string = input('Introdu un string: ')
#
# s1,*s2 = string.split()
# print(s1)
# print(s2)

'''
13. Exercițiu:
citește un string de la tastatură (ex: alabala portocala);
salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.
'''

# string = input('Introdu un string: ')
#
#
# first = string[0]
# interior_modificat = string[1:-1].replace(first, first.upper())
# final_string = string[0] + interior_modificat + string[-1]
# print(final_string)


'''
14.Exercițiu:
citește un user de la tastatură;
citește o parolă;
afișează: 'Parola pt user x este ***** și are x caractere';
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.

eg: parola abc => ***
      parola abcd => ****
'''

# user = input('Introdu username: ')
# parola = input('Introdu parola: ')
#
# stelute = '*' * len(parola)
# print(f'Parola pentru user {user} este {stelute} si are {len(parola)} caractere')
