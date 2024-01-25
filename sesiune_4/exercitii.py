'''
X poate fi inițializat direct în cod sau citit de la tastatură, după preferințe.
X este un int.

1. Declară o listă note_muzicale în care să pui do re mi etc până la do
Afișeaz-o.
Inversează ordinea folosind slicing și suprascrie această listă.
Printează varianta actuală (inversată).
Pe această listă aplică o metodă care bănuiești că face același lucru, adică să îi inverseze ordinea.
Nu trebuie să o suprascrii în acest caz, deoarece metoda face asta automat.
Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta inițială.

Concluzii: slicing e temporar, dacă vrei să păstrezi nouă variantă va trebui să suprascrii lista sau să o salvezi într-o listă nouă.
Metoda găsită de tine face suprascrierea automat și permanentizează aceste modificări. Ambele variante își găsesc utilitatea în funcție de ce ne dorim în acel moment.

2. De câte ori apare ‘do’?

3. Transforma lista de mai sus intr-o tupla. Incearca sa adaugi o nota noua.

4. Declara un dictionar cu notele muzicale de mai sus. Cheia va fi nota, iar valoarea un numar care arata de cate ori apare nota in gama. Afiseaza-l.
'''

# 1
note_muzicale = ['do', 're', 'mi', 'fa', 'sol']

x = note_muzicale[::-1]
print(x)

x.reverse()
print(x)

# 2
print(x.count('do'))

# 3
x = tuple(x)
print(type(x))

x += ('la',)
print(x)

# 4
x_dictionar = {'do': 1,
               're': 2,
               'mi': 3,
               'fa': 4,
               'sol': 5,
               }
print(x_dictionar)
