class PresedinteRomania:

    def __str__(self):
        return "Eu sunt presedintele Romaniei"

    def say_hello(self):
        return f'Salut! {self}'

    _instance = None

    def __init__(self, filename):
        if hasattr(self._instance, 'filename'):
            return
        self.filename = filename

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print('Creating Object')
            cls._instance = super().__new__(cls)
        return cls._instance

a = PresedinteRomania('Iohannis')
b = PresedinteRomania('Basescu')

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Acelasi obiect? {a is b}')