# Randomization
# random module

# importing the random library

import random
import my_module

print(my_module.my_favorite)

# creating the random integer using random module
print(random.randint(1,10))

# modules - used for different function in program

# random floating point number using random()
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

# random floating generator
random_floating = random.uniform(0,10)
print(random_floating)

# printing heads or tails using random
heads_or_tails = random.randint(0,1)
if heads_or_tails == 0:
    print('Tail')
else:
    print('Head')

# Using choice
print(random.choice(['Head','Tail ']))

# Lists - Data Structure - stored many data
states_of_Australia = ['Sydney','Melbourne','Tasmania','South Australia','Western Australia','Queensland','Northern Territory']
print(states_of_Australia[0])
# - minus start from last
print(states_of_Australia[-1])

# changing the items in lists
states_of_Australia[0] = 'sydney'

print(states_of_Australia)

# Adding the item in state
states_of_Australia.append('Hello Land')
print(states_of_Australia)

# Adding the items in state
states_of_Australia.extend(["Anush","Giri"])
print(states_of_Australia)

# Printing the random Value from list
friends = ["Alice","Bob","Charlie","David","Emanuel"]
print(random.choice(friends))

# nested list
fruits = ['Apple','Orange','Grapes','Peaches','Cherries']
vegetables = ['Spinach','Kale','Tomatoes']

dirty_dozen = [fruits,vegetables]
print(dirty_dozen[1][1])