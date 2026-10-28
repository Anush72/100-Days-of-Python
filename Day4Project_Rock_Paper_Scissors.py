# Rock Paper and Scissor Game
import random
rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)   '''

paper = '''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)   '''
scissors = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)   '''

# Storing all in list
game = [rock,paper,scissors]

# user input
user_choice = int(input('Welcome to the Rock Paper Scissor. What choice you made (O for Rock, 1 for Paper or 2 for Scissors:  '))
computer_choice = random.randint(0,2)
if 0 <= user_choice <= 2:
    print(f'You chose: {game[user_choice]}')
print(f'Computer Chose: {game[computer_choice]}')

# if condition to check win or lose
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose")
if user_choice == 0 and computer_choice == 2:
    print('You win')
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print('You lose')
elif computer_choice > user_choice:
    print('You win')
elif computer_choice == user_choice:
    print("It's draw")
