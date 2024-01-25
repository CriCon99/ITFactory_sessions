class Car:
    def go(self):
        print('vrum vrum')

    def start(self):
        print('Starting car')


class Flyable:
    def fly(self):
        print('flew flew')

    def start(self):
        print('Starting flyable')


class FlyingCar(Car, Flyable):
    pass


c = FlyingCar()
c.go()
c.fly()
c.start()

# MRO -> method resolution order: se decide care functie din clasa Car sau Flyable se va apela (de la stanga, la dreapta)
