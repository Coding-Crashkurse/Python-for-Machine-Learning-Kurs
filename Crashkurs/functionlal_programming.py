# Functional Programming

# Bad
new_numbers = []


def multiply_by_2(numbers):
    for x in numbers:
        new_numbers.append(x * 2)


# Good
def multiply_by_2(numbers):
    new_numbers = []
    for x in numbers:
        new_numbers.append(x * 2)
    return new_numbers


# Higher Order Functions
# map(function, iterable)


def multiply_by_2(number):
    return number * 2


map(multiply_by_2, [1, 2, 3])


def greater_than_5(number):
    return number > 5


filter(greater_than_5, [10, 6, 5, 4, 18])

import functools


def multiply_2_values(x, y):
    return x * y


### Lamdba operator

map(lambda x: x * 2, [1, 2, 3, 4])

