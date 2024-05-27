
lst = [1, 2, 3, 4, 5]

# map(function, iterable) - applies function to every item in iterable

def sq(x):
    return x**2

for element in lst:
    print(sq(element))

print(list(map(sq, lst)))
print(list(map(lambda x: x**2, lst)))

# filter(function, iterable) - returns a list of the elements of which function is true

def is_even(x):
    return x % 2 == 0

print(list(filter(is_even, lst)))
print(list(filter(lambda x: x % 2 == 0, lst)))

# reduce(function, iterable) - Apply a function of two arguments cumulatively to the items of a sequence or iterable, from left to right, so as to reduce the iterable to a single value.

from functools import reduce

print(reduce(lambda x, y: x + y, lst))