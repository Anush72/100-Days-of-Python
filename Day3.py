# Control Flow and Logical Operator

# Conditional (if and else)
print("Welcome to the Roll Coaster!")

height = int(input("What is your height?"))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride")


# Modulo Operator - gives the remainder
print(10 % 6)


# Checking whether the number is odd or even using modulo operator
number = int(input("Write the number:\t"))

# Checking whether the number is odd or even

if number % 2 == 0:
    print("This is even number")
else:
    print("This is odd number")

# Nested if else condition
print("Welcome to the Roll Coaster!")

height = int(input("What is your height? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("You have to pay $5.")
    elif age <=18:
        print("You have to pay $5.")
    else:
        print("You have to pay $12.")
else:
    print("Sorry you have to grow taller before you can ride")

# BMI calculator with interpretation
weight = 85
height = 1.85

bmi = weight / height

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal Weight")
else:
    print("Overweight")


#Multiple if
#Nested if else condition
print("Welcome to the Roll Coaster!")

height = int(input("What is your height? "))
bill = 8

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <=18:
        print("Youth tickets are $7.")
        bill = 7
    else:
        print("Adult tickets are $12.")
        bill = 12
    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
    if wants_photo == 'y':
        # Add $3 to their bill
        bill += 3
    print(f"You have to pay {bill}")
else:
    print("Sorry you have to grow taller before you can ride")


print("Welcome to Python Pizza Deliveries")
bill = 0
size = input("What size pizza do you want? S,M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")


# Size of Pizza and Price
if size == 'S':
    bill = 15
    # Adding the pepperoni
    if pepperoni == 'Y':
        bill +=2
elif size == 'M' :
    bill = 20
    if pepperoni == 'Y':
        bill +=3
elif size == 'L':
    bill = 25
    if pepperoni == 'Y':
        bill +=3
else:
    print("You typed wrong inputs")

if extra_cheese =='Y':
    bill +=1
print(f'You have to pay ${bill}')

# Logical Operator
# Multiple if
# Nested if else condition
print("Welcome to the Roll Coaster!")

height = int(input("What is your height? "))
bill = 8

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <=18:
        print("Youth tickets are $7.")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Everything is going to ok. Have a free ride on us ")
    else:
        print("Adult tickets are $12.")
        bill = 12
    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.")
    if wants_photo == 'y':
        # Add $3 to their bill
        bill += 3
    print(f"You have to pay {bill}")
else:
    print("Sorry you have to grow taller before you can ride")


