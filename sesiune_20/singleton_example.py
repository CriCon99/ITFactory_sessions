''''
singleton = este un sablon creational care se asigura ca o clasa are doar o singura instanta
si ofera acces universal catre aceasta instanta
Avantaje:
- poti sa fii sigur ca o clasa are o singura instanta
- acea instanta este accesibila de oriunde din cod
- acea instanta este initializata doar cand este folosita pt prima oara
Dezavantaje:
- acest sablon poate masca un Design slab exemplu (atunci cand componentele programului scriu prea multe una despre cealalta)
'''


class SingletonLogger:
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


logger = SingletonLogger('Hello.txt')
logger2 = SingletonLogger('Hello2.txt')
print(logger, logger2)
print(logger.filename, logger2.filename)
