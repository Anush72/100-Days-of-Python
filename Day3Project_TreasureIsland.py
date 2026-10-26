# Treasure Island

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_or_right = input("You are cross road. Where do you want to go?\n\t Type 'left' or 'right' ").lower()

# if condition
if left_or_right == 'right':
    print("It's game over you fall into a hole.")
elif left_or_right == 'left':
    print("You have come to a lake. There is island in middle of the lake.")
    boat = input('\t Type "wait" to wait for a boat. Type "swim" to swim across ').lower()
    if boat == 'swim':
        print("You have been eaten by shark game over.")
    elif boat == 'wait':
        print("You have arrived at island")
        door = input("\t There are three door (yellow, Red, Blue) Type one ").lower()
        if door == 'blue' and door == 'red':
            print("Game Over")
        elif door == 'yellow':
            print('You win the game')
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
else:
    print('Invalid Input')