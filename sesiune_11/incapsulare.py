'''
3 tipuri de metode si atribute:
1. -> public - accesibile peste tot
2. -> private - accesibile doar in clasa (__atribute)
3. -> protected - accesibil doar in ierarhia de mostenire (_atribute)
'''


class Char:
    __model = 'Dacia'

    def get_model(self):  # getter pt a returna modelul
        return self.__model

    def set_model(self, value):  # setter pt a schimba valoarea curenta din __model
        self.__model = value


c = Char()

print(c.get_model())

c.set_model('BMW')
print(c.get_model())

class Plane:
    __color = 'Red'
    @property # fucntioneaza ca si un getter
    def color(self):
        print('setting as property')
        return self.__color

    @ color.getter
    def color(self):
        print('getting value')
        return self.__color
    @color.setter
    def color(self, value):
        print('Setting value')
        self.__color = value

    @color.deleter
    def color(self):
        print('Deleting value')
        self.__color = None
    @ property
    def is_painted(self):
        return self.__color is not None
p = Plane()
print(p.color)
p.color = 'Blue'
print(p.color)
del p.color
print(p.color)
print(p.is_painted)