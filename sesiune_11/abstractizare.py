'''
O clasa abstracta care are cel putin o metoda abstracta.
O metoda abstracta este o metoda fara implementare (fara corp).
'''

from abc import ABC, abstractmethod  # abc = abstract base class


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def sleep(self):
        raise NotImplementedError

class Dog(Animal):
    def sleep(self):
        print('ZZZzzz')

    def sound(self):
        print('Woof!')