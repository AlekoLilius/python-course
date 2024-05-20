num_1 = 2

num_2 = 5 # assignment operator

# arithmetic operators
print(num_1 + num_2)

print(num_1 - num_2)

print(num_1 * num_2)

print(num_1 / num_2)

print(num_1 ** num_2)

# modulo

print(num_1 % num_2)

# floor division

print(num_1 // num_2)

# comparison

print(num_1 == num_2)

print(num_1 >= num_2)

print(num_1 <= num_2)

print(num_1 != num_2)

# Floats

print(0.01 + 0.09, (0.01 + 0.09) == 0.1)

from decimal import Decimal

print(Decimal(0.01) + Decimal(0.09))

import math
print(math.isclose(0.1 + 0.2, 0.3))

# exact precision

print(round(0.01 + 0.09, 2))

# Relational operators logical
# and, or, not

print(1 and 1)

print(1 and 0)

# and, or, not = >

if (2 != 0):
    print('A lie (the truth)')
else:
    print('A truth')

name = 'Tom'
age = 45

if name == 'Tom' and age == 45: # both conditions need to be satisfied
    print('Hello, tutor!')
else:
    print("Hello", name)

if name == 'Nada' or age == 45: # one condition needs to be satisfied
    print('Hello', name)
else:
    print('Something is wrong')

if not name:
    print('Name is missing')
else:
    print(name)

# Comments

# User Input
user_input = input('Say something: ')

area = 3 * 4  # area of a rectangle

'''
Can be
good for
longer comments
'''