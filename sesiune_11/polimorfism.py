class Animal:
    def __init__(self, age, species):
        self.age = age
        self.species = species

    def eat(self):
        return f'Eu sunt un {self.__class__.__name__} mancacios'


class DomesticAnimal(Animal):
    def __init__(self, age, species, owner):
        super().__init__(age, species)
        self.owner = owner


class WildAnimal(Animal):
    def __init__(self, age, species, location):
        super().__init__(age, species)
        self.location = location


def animals_eat(animals):
    for a in animals:
        print(a.eat())

animals_eat([
    DomesticAnimal(5, 'vaca', 'Ion'),
    DomesticAnimal(4,'Caine', 'Ion'),
    WildAnimal(25,'Urs','Padure'),
    WildAnimal(40, 'Girafa', 'Jungla')
])

'''
polimorfismul se refera la abilitatea unui obiect de a se comporta in mai multe moduri, in functie de context.
In esenta, polimorfismul permite obiectelor de acelasi tip sa aiba comportamente diferite, fara a fi necesar sa se stie
tipul lor inainte de executie.
'''