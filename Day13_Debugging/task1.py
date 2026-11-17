def my_function():
    for i in range(1,21):
        if i == 20:
            print("You got it")

my_function()

# problem is that the 20 is exclusive so range does not get 20


# reproduce bug
from random import randint

dice = [1,2,3,4,5,6]
dice_num = randint(0,5)

print(dice[dice_num])


# play and Evaluate Each Line

year = int(input("What's your year of birth?"))

if 1980 < year <= 1994:
    print("You are Millennial")
elif year > 1994:
    print("You are a Gen Z.")


# try and exception

try:
    age = int(input("How old are you? "))
except ValueError:
    print("You have typed in an invalid number. Please try again with numerical value")
    age = int(input("How old are you? "))

if age > 18:
    print(f"You can drive at age {age}.")