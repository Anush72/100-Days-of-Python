# Import the game
import  random


# Assigning the random number from 0 to 100
number = random.randint(0,100)
print("Welcome to the Number Guessing Game.")
print("I'm thinking of a number between 1 and 100.")

# Asking user to choose the difficulty level
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
guess_time= 0
if difficulty == 'easy':
    guess_time = 10
elif difficulty == 'hard':
    guess_time = 5

number_game = True

while number_game:
    print(f"You have {guess_time} remaining to guess the number.")
    guess_time -= 1

    user_guess = int(input("Make a guess: "))
    # checking the condition
    if user_guess > number:
        print("Too high")
    elif user_guess < number:
        print("Too low")
    elif user_guess == number:
        print(f"You make it right {number}")
        number_game = False
    if guess_time == 0:
        print(f"The number I am thinking is {number}")
        print("Thank you for playing")
        number_game = False