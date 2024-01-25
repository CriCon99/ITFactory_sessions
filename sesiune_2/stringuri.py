# lungimea unui string

name = 'Dragos '
print(len(name))

# convertire la uppercase

print(name.upper())

# convertire la lowercase
name = 'DrAgoS'
print(name.lower())

# numar de apartitii

nume = 'Ana Maria'

print(nume.count('a'))
print(nume.count('i'))
print(nume.count('s'))

# inlocuire de text

prop = ' - oare vreau sa merg acolo! \n - unde sa mergi!'
# \n -> caracter pt linia noua

print(prop)

print(prop.replace('!', '?'))

print(prop)  # functia replace nu modifica stringul initial

# index

name = 'john'
print(name.index('o'))  # gaseste indexul primei potriviri cu caracterul din []

print(name[0])

print(name[-1])  # ultimul caracter

# slicing

b = 'Hello, World!'
print(b[2:5])  # de la 2 la 5 (fara 5)
print(b[:5])  # de la inceput la 5 (fara 5)
print(b[2:])  # de la 2 la final
print(b[-5:-2])  # indexare negativa
