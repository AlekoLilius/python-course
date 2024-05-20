import random

print("Welcome to rock, paper scissors!")

possible_actions = ['rock', 'paper', 'scissors']
while True:
    computer_action = random.choice(possible_actions)
    usr_input = input("Enter a choice (rock, paper, scissors): ")

    print(f"The computer chose {computer_action} and you chose {usr_input}")

    if computer_action == usr_input:
        print("You chose the same, try again")
        continue
    elif usr_input == 'rock':
        if computer_action == 'paper':
            print("You lost")
        elif computer_action == 'scissors':
            print("You won!")
    elif usr_input == 'paper':
        if computer_action == 'scissors':
            print("You lost")
        elif computer_action == 'rock':
            print("You won!")
    elif usr_input == 'scissors':
        if computer_action == 'rock':
            print("You lost")
        elif computer_action == 'paper':
            print("You won!")
    else:
        print("You didn't follow the rules, try again")
        continue
    
    playing = input("Do you want to play again? (y/n): ")
    if playing == 'n':
        print("Thanks for playing!")
        break