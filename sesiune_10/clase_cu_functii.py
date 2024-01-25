class Dog:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def bark(self):
        print('wof')

    def print_name(self):
        print(self.name)

d = Dog(2,'Rexi')

d.bark()

d.print_name()
