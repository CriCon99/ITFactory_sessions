'''
ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai probabil am colturi’
'''

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    PI = 3.14
    def aria(self):
        pass
    def descrie(self):
        print('Cel mai probabil am colturi')

'''
INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură
'''
class Patrat(FormaGeometrica):
    def __init__(self,latura):
        self.latura = latura

'''
ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)

Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
'''