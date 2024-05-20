import random

print("Welcome to the Guess a Number!")
print("Do you want to guess or make the computer guess your number?")
usr_settings = int(input("Input \'1\' for you guessing or \'2\' for computer guessing: "))

if usr_settings == 1:
    rand_nbr = random.randint(1, 9)
    while True:
        usr_input = input("Pick a number between 0 and 10: ")

        if usr_input.isnumeric():
            if int(usr_input) == rand_nbr:
                print("That's correct, you win!")
                break
            elif int(usr_input) > 9 or int(usr_input) < 1:
                print("That's not a number between 0 and 10")
            else:
                print("Wrong number, try again!")
        else:
            print("That's not a number, try again!")
elif usr_settings == 2:
    usr_input = ''
    while True:
        usr_input = input("Pick a number between 0 and 10 for the computer: ")

        if usr_input.isnumeric():
            if int(usr_input) > 9 or int(usr_input) < 1:
                print("That's not a number between 0 and 10")
            else:
                usr_input = int(usr_input)
                break
        else:
            print("That's not a number, try again!")

    counter = 0
    while True:
        counter += 1
        rand_nbr = random.randint(1, 9)

        if rand_nbr == usr_input:
            print(f"The computer guessed right after {counter} tries!")
            break
        else:
            print(f"The computer guessed {rand_nbr}")
else:
    print("Not an option")