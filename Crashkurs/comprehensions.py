# Comprehensions

numbers = [1, 2, 3, 4, 5]
result = []

for x in numbers:
    result.append(x * 2)

### Functional programming
result2 = list(map(lambda x: x * 2, numbers))
result2

# Comprehensions
result3 = [num * 2 for num in numbers]


set_numbers = {1, 2, 3, 4, 5}
{num * 2 for num in set_numbers if num < 3}

# Achtung!
tuple_numbers = (1, 2, 3, 4, 5)
(num for num in tuple_numbers)
tuple(num for num in tuple_numbers)

dict_numbers = {"a": 1, "b": 2, "c": 3, "d": 4}

{k: v * 2 for k, v in dict_numbers.items()}


# Advanced List comprehensions
numbers = [2, 3, 1, 5, 10]

# Filtern
[num * 2 for num in numbers if num > 2]

# Bedingungen
[num * 2 if num > 2 else num for num in numbers]


# mit Index
[num for index, num in enumerate(numbers) if index < 3]
