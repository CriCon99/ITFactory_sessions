def say_hello():
    return 'hello'
# o data ce am scris return functia se opreste din executie si se intoarce in locul de unde a fost apelata, dand inapooi valoarea hello
text = say_hello()

print(text)

print(say_hello())


def say_hi():
    print('hi')

text = say_hi()
print(text)