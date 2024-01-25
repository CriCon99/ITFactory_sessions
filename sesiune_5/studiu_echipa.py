'''
12. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:

Declară o Listă cu 5 jucători
Schimbari_efectuate = te joci tu cu valori diferite
Schimbari_max = 3

Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
Efectuează schimbarea
Șterge jucătorul scos din listă
Adaugă jucătorul intrat
Afișază a intrat x, a ieșit y, mai ai z schimbări

Dacă jucătorul nu e în teren:
Afișează ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
Afișează ‘mai ai z schimbări’

Testează codul cu diferite valori
'''

lista = ['Beckham', 'Figo', 'Zidane', 'Carlos', 'Sergio']
Schimbari_efectuate = 2
Schimbari_max = 3

schimb = input('Vrei sa faci un schimb? (y/n): ')

if schimb == 'y':
    jucator_scos = input('introdu jucatorul pe care vrei sa il scoti: ')
    if jucator_scos not in lista:
        print(f'nu se poate efectua schimbarea deoarece jucătorul {jucator_scos} nu e în teren, mai ai {Schimbari_max - Schimbari_efectuate} schimbari')
    else:
        lista.remove(jucator_scos)
        jucator_adaugat = input('introdu jucatorul pe care vrrei sa il adaugi: ')
        lista.append(jucator_adaugat)
        print(f'a iesit jucatorul {jucator_scos} si a intrat {jucator_adaugat}, mai ai {Schimbari_max - Schimbari_efectuate} schimbari')
print(lista)


'''
3. Fie seturile:
    
    set1 = {"Yellow", "Orange", "Black"}
    set2 = {"Orange", "Blue", "Pink"}
    
    
    1. Sa se afiseze toatele elementele care apar in `set1` si nu apar in `set2`
    2. Sa se afiseze toatele elementele care apar in ambele seturi
    3. Sa se afiseze toatele elementele care nu sunt comune
'''

# set1 = {"Yellow", "Orange", "Black"}
# set2 = {"Orange", "Blue", "Pink"}
#
# print(set1.difference(set2)) # 1
# print(set1 & set2) # 2
# print(set1.symmetric_difference(set2)) # 3
