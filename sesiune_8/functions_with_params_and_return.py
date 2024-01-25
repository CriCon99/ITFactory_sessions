def product(a, b):
    return a * b


p = product(2, 3)
print(p)


def is_even(number):
    # if number % 2 == 0:
    #     return True
    # return False
    return number % 2 == 0


nr = is_even(8)
print(nr)


def get_all_even_numbers(numbers):
    rezultat = []

    for elem in numbers:
        if is_even(elem):
            rezultat.append(elem)

    return rezultat


nr = get_all_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(nr)
