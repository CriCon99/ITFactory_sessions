# seturile sunt colectii de elemente unice si neordonabile

# creare

fructe = {'mar', 'para', 'banana'}

masini = set()  # asa se creeaza un set fara elemente

# adaugare elemente
print(20 * '-', 'adaugare elemente', 20 * '-')

fructe.add('struguri')
print(fructe)

# stergere elemente
print(20 * '-', 'stergere elemente', 20 * '-')

fructe.remove('banana')
print(fructe)
# fructe.remove('cirese') - arunca eroare, pt ca nu exista elementul
fructe.discard('cirese')  # nu arunca eroare
fructe.pop()
print(fructe)
fructe.clear()
print(fructe)

# operatii speciale
# join
print(20 * '-', 'join', 20 * '-')
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
print(set1 | set2)

# intersectia
print(20 * '-', 'intersectia', 20 * '-')

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.intersection(y)
print(z)
print(x & y)

# diferenta
print(20 * '-', 'diferenta', 20 * '-')

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}

z = x.difference(y)
print(z)
print(x - y)

# diferenta simetrica
print(20 * '-', 'diferenta simetrica', 20 * '-')

x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}

z = x.symmetric_difference(y)
print(z)
print(x ^ y)
# toate elementele care nu sunt comune

# subset si superset
print(20 * '-', 'subset si superset', 20 * '-')

a = {1,2,3}
b = {5,4,3,2,1}
print(a.issubset(b)) # toate elementele lui a sunt in b
print(b.issuperset(a)) # b contine toate elementele lui a

