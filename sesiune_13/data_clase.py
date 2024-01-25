from dataclasses import dataclass, field
from typing import List

'''
Dataclass suprascrie automat 3 functii: 
1. __init__ (constructorul)
2. __repr__ (afisare)
3. __eq__ (qgalitatea - daca toate campurile sunt egale)
'''


@dataclass
class Student:
    name: str
    age: int


s = Student('Andrei', 20)
print(s)
s2 = Student('Andrei', 20)
print(s == s2)


@dataclass
class Teacher:
    name: str
    materie: str
    vechime: int = 0  # specificare valoare implicita (default)
    clase: List = field(default_factory=list)  # se creeaza o lista goala pt fiecare obiect nou
    cod_intern: int = field(init=False, repr=True,
                            default=123)  # acest atribut nu va fi introdus in contructor si nici in afisare


t = Teacher('Valeria', 'matematica')
print(t)
