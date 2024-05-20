
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
age = int(input('Enter your age: '))
country = input('Enter your country: ')
place = input('Enter your place: ')
hobbies = input('Enter your hobbies: ')
money = float(input('Enter your money: '))

print(f"Hello! I am {first_name} {last_name}.", end=' ')
print(f"I am {age}. I am living in {place}, {country}.", end=' ')
print(f"I love {hobbies}.", end=' ')
print(f"It has passed {age * 365} days since I was born.", end=' ')
print("I have $" + "{:.2f}".format(money) + " in my bank acccount.")