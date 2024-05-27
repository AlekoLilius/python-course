import random

def choose_word():
    words = ['dog', 'cat', 'lion', 'giraffe', 'elephant', 'wolf', 'horse', 'beaver', 'snake', 'cheetah']
    return random.choice(words)

def displayword(word, guessed_letters):
    display = " "
    win = True
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
            win = False
    return display, win

number_of_guesses = 0
guessed_letters = set()
word = choose_word()

hangman_list = ['''
  x====x
  |    |
       |
       |
       |
       |
========
''',
'''
  x====x
  |    |
  o    |
       |
       |
       |
========
''',
'''
  x====x
  |    |
  o    |
  |    |
       |
       |
========
''',
'''
  x====x
  |    |
  o    |
 /|    |
       |
       |
========
''',
'''
  x====x
  |    |
  o    |
 /|\   |
       |
       |
========
''',
'''
  x====x
  |    |
  o    |
 /|\   |
 /     |
       |
========
''',
'''
  x====x
  |    |
  o    |
 /|\   |
 / \   |
       |
========
''']

print("Welcome to hangman!")
print(hangman_list[0])
current_word = list(len(word) * '_')
print('Word: ')
print(''.join(current_word))

while number_of_guesses != 6:
    guess = input('Guess a letter: ').lower()
    if len(guess) != 1 or not guess.isalpha():
        print('Invalid input!')
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        word_display, win = displayword(word, guessed_letters)
        print(word_display)
        continue

    guessed_letters.add(guess)
    print(guessed_letters)

    if guess not in word:
        number_of_guesses += 1
        print(hangman_list[number_of_guesses])
        print('Word: ')
        word_display, win = displayword(word, guessed_letters)
        print(word_display)
    else:
        print("Correct guess!")
        word_display, win = displayword(word, guessed_letters)
        print(word_display)
        if win:
            print("You win!")
            break

    if number_of_guesses == 6:
        print("You lost!")




