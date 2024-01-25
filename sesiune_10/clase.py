'''
o clasa este o schita sau un prototip definit de programator din care
sunt create obiecte.
clasele ofera un mijloc de a grupa datele si functionalitatile.
crearea unei clase noi creeaza un nou tip de obiect, permitand instantierea
unor obiecte din acest tip.
Fiecare instanta de clasa poate avea atribute atasate pentru mentinerea
starii sale.
Instantele de clasa pot avea si metode pt modificarea starii lor.
Un obiect este instanta unei clase.
Diferenta dintre obiect si clasa: o clasa este ca o schita in timp ce un
obiect este o copie a clasei cu valori reale
'''


class Dog:
    species = 'mamifer'
    age = 8
    name = 'Rexi'


d = Dog()  # instantierea unui obiect (d -> obiect)

print(type(d))
print(d.species)
print(d.age)
print(d.name)
