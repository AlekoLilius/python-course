# num1 = int(input('Number 1: '))
# num2 = int(input('Number 2: '))

# print(num1 + num2)

# num3 = int(input('Number 1: '))
# num4 = int(input('Number 2: '))

# print(num3 + num4)

#D.R.Y: Don't repeat yourself
#K.I.S.S: Keep it simple stupid

def function_name():
    f_name = input('What\'s your first name: ')
    print(f_name)

#function_name()

def add(num1, num2):
    return num1 + num2

print(add(1, 2))

def area(side_a, side_b):
    return side_a * side_b

print(area(4, 5))

def print_title(title='This is a default title'):
    print(title)

print_title()

def multiply(a, b=1, c=1):
    return a * b * c

print(multiply(2, 3))

print(multiply(2, 3, 5))

print(multiply(2))

def make_string(first, second, third):
    return first + second + third

print(make_string('Tom', 'is', 'here'))

print(make_string(third='here', second='is', first='Tom'))

def person(name, occupation, age):
    return f'Name: {name}, Age: {age}, Occupation: {occupation}'

print(person(name='Tom', age=45, occupation='Tutor'))
print(person('Tom', 45, 'Tutor'))

# Scope

name = 'Tom'
print(name)

def print_name(name):
    print(name)

print_name('Mario')
print(name)

points = 0

def add_points():
    global points
    points += 5

def reduce_points(p):
    p -= 5

add_points()

print(points)

reduce_points(points)

print(points)