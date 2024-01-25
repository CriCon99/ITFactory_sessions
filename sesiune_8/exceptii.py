# print(1/0)
# print(x)
try: # testeaza un bloc de cod dupa erori
    print(x)
except: # trateaza diferite tipuri de erori
    print('A aparut o eroare')
########################################################
try:
    print(str.values)
    print(1 / 0)
    print(x)

except NameError:
    print('Variabila x nu este definita')
except ZeroDivisionError as ex:
    print(f'eroarea : {ex}')
except:
    print('A aparut o alta eroare')

######################################################

try:
    print(1)
except:
    print('a aparut o eroare')
else:
    print('nu a aparut nicio eroare')

######################################################
try:
    print(1)
except:
    print('a aparut o eroare')
finally:
    print('Eu sunt executat mereu')
#####################################################
x =-1
if x<0:
    raise Exception('Fara numere negative')

"""
try: (Blocul try)
    bloc de cod unde ar putea aparea o eroare
    (Sfarsitul blocului try)
except NumeEroare: <-- Prinderea tuturor exceptiilor de tipul NumeEroare
    se executa doar daca se prinde NumeEroare
except (AltNumeEroare, IncaUnNumeEroare): <-- Gruparea mai multe tipuri de Exceptii
    se executa daca se prinde AltNumeEroare sau IncaUnNumeEroare
except Eroarea4 as ex: <-- Stocarea mesajului unei erori intr-o variabila (exemplul variabilei 'ex')
    se poate accesa mesajul de Eroarea4 prin variabila ex
except:
    se executa la orice alt tip de eroare nespecificat
else:
    se executa doar daca nu se arunca eroare in blocul try
finally:
    se executa indiferent daca se arunca eroare sau nu
"""