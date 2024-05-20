# num = float(input('Give me a number: '))

# print(type(num), num)

num1 = input('Give me a number: ')

if num1.isdigit():
    num1 = int(num1)
    print(num1)
else:
    print('This is not an integer number')

