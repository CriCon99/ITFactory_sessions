'''
1. Sa se scrie un program care citeste un text de la tastatura si afiseaza o lista
 cu fiecare caracter in ordinea inversa a aparitiei in text.
'''
# cuvant = input('Introdu un cuvant: ')
#
# l = list(cuvant)
#
# print(l[::-1])

'''
2. Sa se scrie un program care citeste numele, emailul si
varsta unei persoane de la tastatura si adauga toate datele intr-un dictionar pe care il afiseaza.
Daca persoana nu este multumita cu datele introduse
va putea specifica daca vrea sa modifice maxim o valoare din dictionar.
'''
nume = input('introdu numele: ')
email = input('introdu mail: ')
varsta = int(input('introdu varsta: '))

data = {
    'nume': nume,
    'email': email,
    'varsta': varsta,
}

print(data)

modifica = input('vrei sa modifici datele? (y/n): ')

if modifica == 'y':
    cheie_de_modificat = input('introdu informatia pe care vrei sa o modifici: ')
    if cheie_de_modificat not in data:
        print('nu exista aceasta valoare')
    else:
        valoare_de_modificat = input('introdu noua valoare: ')
        valoare_de_modificat = int(valoare_de_modificat) if cheie_de_modificat == 'varsta' else valoare_de_modificat
        data[cheie_de_modificat] = valoare_de_modificat

print(data)