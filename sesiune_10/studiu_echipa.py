'''
1.Clasa Cerc
    Atribute: rază, culoare
    Constructor pentru ambele atribute
    Metode:
descrie_cerc() - va PRINTA culoarea și raza
aria() - va RETURNA aria
diametru()
circumferinta()

'''




import math
class Cerc:
    def __init__(self,raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(self.raza,self.culoare)
    def aria(self):
        return math.pi*self.raza**2
    def diametru(self):
        return 2*self.raza
    def circumferinta(self):
        return 2*math.pi*self.raza


c = Cerc(2, 'galben')

c.descrie_cerc()
print(c.aria())
