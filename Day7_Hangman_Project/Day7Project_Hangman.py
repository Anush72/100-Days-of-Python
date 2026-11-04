# importing the random library
import random
# importing word and stages from module
from  hangman_words import  word_list
from hangman_art import stages

# choosing the random word from list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
# Creating blank based on letter
placeholder= ''
for i in range(word_length):
    placeholder += '_'
print(placeholder)
placeholder = list(placeholder)

# Ask user to guess a letter and if the letter is in chosen word then print
game_over = False
lives = 6
correct_letters = []
guess_letters = []
while not game_over:
    display = ''
    guess = input('Guess a letter: ').lower()
    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if not '_' in display:
        print("You won the game")
        game_over = True
    # checking the lives and print the hangman according to lives
    if guess not in chosen_word:
        if guess in guess_letters:
            print("You have already type this letter")
        else:
            lives -= 1
            print(f'Incorrect word and you have {lives} live left')
    if lives == 0:
        print("You have loss game")
        game_over = True
    # printing the art
    print(stages[lives])
    guess_letters.append(guess)