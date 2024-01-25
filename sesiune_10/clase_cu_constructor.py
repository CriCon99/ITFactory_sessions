class Dog:
    species = 'mamifer'  # acest tip de atribut este unul special -> class attribute (are aceeasi valoare pt toate obiectele din aceasta clasa)
    age = 8
    name = 'Bruno'


d = Dog()
print(d.name)

d2 = Dog()

d2.name = 'Pufi'  # name devine atrubut de instanta pt obiectul d2 (nu se mai modifica decat la d2)
print(d.name, d2.name)

Dog.name = 'Rexi'
print(d.name, d2.name)


# atributele de clasa sunt in general folosite pt a defini constante intr-o clasa)

class Cat:
    species = 'mamifer'

    def __init__(self, age, name):  # functie constructor, self este o referinta catre obiectul curent

        self.age = age
        self.name = name


c = Cat(12, 'Leo')
c2 = Cat(10, 'Mitza')
print(c.age, c2.age)

# Cat.name -> incorect deoarece atributul name este un atribut de instanta si poate fi accesat doar printr-un obiect din aceasta clasa
