new_numbers = []

numbers = [1, 2, 3, 4, 5, 6]


def multiply_by_2(numbers):
    for x in numbers:
        new_numbers.append(x * 2)


multiply_by_2(numbers)
new_numbers


def multiply_by_2(numbers):
    new_numbers = []
    for x in numbers:
        new_numbers.append(x * 2)
    return new_numbers


multiply_by_2(numbers)

# Higher order functions
# map, filter, reduce, zip


def multiply_by_2(number):
    return number * 2


list(map(multiply_by_2, [1, 2, 3, 4, 5]))


def greater_than_3(number):
    return number > 3


list(filter(greater_than_3, [1, 2, 3, 4, 5]))

from functools import reduce


def multiply_2_values(x, y):
    return x * y


reduce(multiply_2_values, [1, 2, 3, 4, 5])


list(map(lambda x: x * 2, [1, 2, 3, 4, 5]))

# Zip
liste_1 = ["a", "b", "c", "d"]
liste_2 = [1, 2, 3, 4]

list(zip(liste_1, liste_2))

