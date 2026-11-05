# Function with inputs
def greet(name):
    print(f"Hello {name}")
    print(f"Namaste {name}")
    print("How are you?")

greet('Anush')


# Function to return how many weeks we have

def life_in_weeks(age):
    difference = 90 - age
    week = difference * 52
    print(f"You have {week} weeks left")

life_in_weeks(22)


# Positional vs Keyword Arguments
# Function with more than 1 input
def greet_with(name,location):
    print(f'Hello {name}')
    print(f'What is like in {location}?')


# Positional Argument take input based on input sequence if we did not specify the arguments
greet_with('Anush','Melbourne')

# Keyword Argument you put argument with keyword
greet_with(location='Sydney',name='Sonij')

# Love Calculator
def calculate_love_score(name1,name2):
    combine_name = name1 + name2
    # Assign the variable
    count_true = 0
    count_love = 0
    for i in 'true':
        count_true += combine_name.lower().count(i)
    for i in 'love':
        count_love += combine_name.lower().count(i)
    love_score = str(count_true) + str(count_love)
    print(f'Love Score =  {love_score}')

calculate_love_score('Angela Yu','Jack Bauer')
