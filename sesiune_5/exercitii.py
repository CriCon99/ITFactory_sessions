'''
3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
Găsește 2 variante să le unești într-o singură listă.
'''
# a = [3, 1, 0, 2]
# b = [6, 5, 4]
#
# d = a + b
# print(d)
#
# a.extend(b)
# print(a)  # aceasta varianta a modificat lista initiala
# a.append(b)  # varianta neacceptata deoarece, adauga lista b ca element in lista a, si nu face reuniunea celor doua
# print(a)

'''
4.
Sortează și afișează lista generată la exercițiul anterior.
elimina numărul 0 folosind o funcție.
Afișaza iar lista.
'''
# a = [3, 1, 0, 2]
# b = [6, 5, 4]
# d = a + b
#
# d.sort()
# print(d)
#
# d.remove(0)
# print(d)

'''
Folosind un if verifică lista generată la exercițiul 3 și afișează:
Lista este goală.
Lista nu este goală.
'''

a = [3, 1, 0, 2]
b = [6, 5, 4]
d = a + b

# if len(d) == 0:  # varianta 1
#     print('lista este goala')
# if d == []:  # varianta 2
#     print('lista este goala')
# if not d:  # varianta acceptata si cea mai buna
#     print('lista este goala')

# ------------------------------

# if len(d) > 0:  # varianta 1
#     print('lista nu este goala')
# if d != []:  # varianta 2
#     print('lista nu este goala')
# if d:  # varianta acceptata si cea mai buna
#     print('lista nu este goala')

'''
8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
'''

# dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
#
# print(list(dict1.keys()))

'''
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
'''

# dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
#
# name = input('introdu un nume: ')
# nota = dict1.get(name)
# if nota is None:
#     print('ai introdus o valoare incorecta')
# else:
#     print(f'{name} a luat nota {dict1[name]}')

'''
10. Dorel a făcut contestație și a primit 6
Modifică nota lui Dorel în 6
Printează nota după modificare
'''
# dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
#
# dict1['Dorel'] = 6
# print(dict1['Dorel'])

'''11. Gigel se transferă din clasă
Căuta o funcție care să îl șteargă
Vine un coleg nou. Adaugă Ionică, cu nota 9
Printează noii elevi
'''
# dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
#
# dict1.pop('Gigel')
# print(dict1)
#
# dict1['Ionica'] = 9
# print(dict1)

'''
13.
Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
Adaugă în zilele_sapt ‘luni’
Afișează zile_sapt
'''

# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
#
# zile_sapt.add('luni')  # nu se adauga pt ca deja exista in set
# print(zile_sapt)


'''
14.Folosește un if și verifică dacă:
Weekend este un subset al zilelor din săptămânii.
Weekend nu este un subset al zilelor din săptămânii.
'''

# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
#
#
# if weekend.issubset(zile_sapt):
#     print('Weekend este un subset al zilelor din săptămânii.')
# else:
#     print('Weekend nu este un subset al zilelor din săptămânii.')

'''
15. Afișează diferențele dintre aceste 2 seturi.
'''
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
#
#
# print(zile_sapt.difference(weekend))
# print(zile_sapt - weekend)

'''
16. Afișează intersecția elementelor din aceste 2 seturi.
'''

# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# print(zile_sapt.intersection(weekend))
# print(zile_sapt & weekend)