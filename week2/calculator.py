
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return 'DIV ERROR'
    return num1 / num2

num1, num2 = input('Numbers to calculate (num1 num2): ').split(' ')

operation = input('Select operation to perform (+, -, /, *): ')

result = ''

if operation == '+':
    result = addition(float(num1), float(num2))
elif operation == '-':
    result = subtraction(float(num1), float(num2))
elif operation == '/':
    result = division(float(num1), float(num2))
else:
    result = multiplication(float(num1), float(num2))

if (result == 'DIV ERROR'):
    print('Cannot perform division by 0')
else:
    print('Result:', result)