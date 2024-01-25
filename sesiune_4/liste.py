'''
listele sunt folosite pentru a stoca mai multe valori intr-o singura variabila

elementele dintr-o listas sunt ordonabile, modificabile si permit valori duplicate

listele sunt indexate si primul element are indexul 0

cand spunem ca o lista este ordonata, ne referim la faptul ca elementele au o ordine predefinita si acea ordine nu se va mai schimba
'''

# creare
fructe = ['mere', 'pere', 'banane']
numere = [1, 2, 3, 4, 5, 6, 7, 8, 9]
masini = list(('audi', 'tesla', 'dacia'))
print(type(numere))
print(len(numere))

# indexare

print(20 * '-', 'indexare', 20 * '-')
print(numere[0])
print(numere[-1])
print(numere[:2])
print(numere[::2])

# adaugare element
print(20 * '-', 'adaugare element', 20 * '-')

numere.append(10)
print(numere)
numere.insert(2, 9)  # index, element
print(numere)

# stergere element
print(20 * '-', 'stergere element', 20 * '-')

elem = numere.pop()  # elimina de la final si il returneaza
print(elem)
print(numere)

numere.pop(0)  # elimina de la indexul specificat
print(numere)

numere.remove(3)  # elimina prima aparitie a valorii date
print(numere)

# stergere toate elementele
print(20 * '-', 'stergere toate elementele', 20 * '-')

numere.clear()
print(numere)

# inlocuire element
print(20 * '-', 'inlocuire element', 20 * '-')

print(fructe)
fructe[1] = 'struguri'
print(fructe)

# numarare aparitii
print(20 * '-', 'numarare aparitii', 20 * '-')

numere = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numere.count(2))

# adunarea a doua liste
print(20 * '-', 'adunarea a doua liste', 20 * '-')

numere2 = [20, 21, 22]

numere.extend(numere2)

print(numere)

numere3 = [1, 2, 3]

print(numere2 + numere3)  # nu se modifica niciuna din cele doua liste

# inversare
print(20 * '-', 'inversare', 20 * '-')
#1
print(fructe[::-1]) # nu modifica varianta initiala
#2
fructe.reverse() # modifica lista initiala (operatiuine in place)
print(fructe)

# sortare
print(20 * '-', 'sortare', 20 * '-')

numere.sort()
print(numere)
numere.sort(reverse=True)
print(numere)