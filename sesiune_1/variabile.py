# variabila - container din memorie pt a stoca valori

# 1 - crearea unei variabile

x = 5  # se ia o zona din memorie in care se pune valoarea 5
y = 'john'

print(x)
print(y)
# 2 - denumirea variabilelor
'''
reguli:
- numele unei variabile trebuie sa inceapa cu o litera sau _
- numele unuei variabile nu poate incepe cu un numar
- numele unei variabile poate contine doar caractere alfanumerice si _
- numele variabilelor sunt case sensitive (age, AGE, Age) sunt 3 variabile diferite

'''
# asa
myvar = 'Dina'
my_var = 'Dina'
_my_var = 'Dina'
myVar = 'Dina'
myvar2 = 'Dina'

#  asa nu

# 2myvar='Dina'
# my-var='Dina'
# my var='Dina'
# 3 - multiple valori la multiple variabile
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)
# 4 - o valoare multiple variabile
x = y = z = 'portocala'
print(x)
print(y)
print(z)
