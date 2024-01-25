# tuplul este o colectie de elemente, nemodificabila, ordonabila, nemutabila
# creare
fructe = ('mar', 'para', 'banana')
print(fructe)

# indexare
print(20 * '-', 'indexare', 20 * '-')
print(fructe[0])
print(fructe[-1])

# numarare aparitii
print(20 * '-', 'numarare aparitii', 20 * '-')
print(fructe.count('para'))

# adaugare elemente
print(20 * '-', 'adaugare elemente', 20 * '-')
fructe += ('struguri',)
print(fructe)

# daca vrem sa stergem, se transforma inapoi in lista, si iar inapoi in tuplu
