# create

car = {
    'brand': 'ford',
    'model': 'mustang',
    'an': '1964'
}

# accesare elemente
print(20 * '-', 'accesare elemente', 20 * '-')

print(car['brand'])
print(car.get('model'))
print(car.get('is_new'))
print(car.get('is_new', True))

# adaugare elemente

print(20 * '-', 'adaugare elemente', 20 * '-')

car['is_new'] = True
print(car)

car.setdefault('is_new',
               True)  # retureneaza valoarea de la cheia data, iar daca aceasta nu exista, o adauga cu valoarea din paranteze
car.setdefault('price', 7910)
print(car)

# stergere element
print(20 * '-', 'stergere element', 20 * '-')
car.pop('is_new')
print(car)

car.popitem()  # elimina ultima cheie adaugata
print(car)

del car['an']
print(car)

# stergerea tuturor elementelor
print(20 * '-', 'stergerea tuturor elementelor', 20 * '-')

car.clear()
print(car)

# afisare toate cheile
print(20 * '-', 'afisare toate cheile', 20 * '-')

car = {
    'brand': 'ford',
    'model': 'mustang',
    'an': 1964
}

print(list(car.keys()))
# afisare toate valorile
print(list(car.values()))

# afisare toate valorile
print(20 * '-', 'afisare toate valorile', 20 * '-')
print(list(car.items()))
