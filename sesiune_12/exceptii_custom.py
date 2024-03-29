class CustomException(Exception):
    pass

'''
Sa se scrie o functie care verifica daca o lista de numere intregi contine numere negative.
daca da, sa se arunce o exceptie specifica.
'''



class ContainsNegativeNumberException(Exception):
    pass


def check_negative_numbers(numbers):
    for number in numbers:
        if number < 0:
            raise ContainsNegativeNumberException(f'Contine {number}')

check_negative_numbers([1,2,-1,-2,3,4,5,6])