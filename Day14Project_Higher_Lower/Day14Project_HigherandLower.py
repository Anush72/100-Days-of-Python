# importing libraries
import random
from data import data_dic
from art import  logo, vs

# getting random person from data
person_a = random.choice(data_dic)
person_b = random.choice(data_dic)

higher_or_lower = True
print(logo)
score = 0
# while loop
while higher_or_lower:
    is_correct = False
    # Keep selecting another person if two have same followers
    while person_a['follower_count'] == person_b['follower_count']:
        person_b = random.choice(data_dic)
    print(f"Compare A :{person_a['name']}, a {person_a['description']}, from {person_a['country']}")
    print(vs)
    print(f"Compare B :{person_b['name']}, a {person_b['description']}, from {person_b['country']}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_choice == 'a':
        if person_a['follower_count'] > person_b['follower_count']:
            is_correct = True
        else:
            print(f"Sorry, that's wrong. Final Score: {score}")
            higher_or_lower = False
    elif user_choice == 'b':
        if person_b['follower_count'] > person_a['follower_count']:
            is_correct  =  True
        else:
            print(f"Sorry, that's wrong. Final Score: {score}")
            higher_or_lower = False
    else:
        print("Incorrect Input Please type 'A' or 'B': ")
    if is_correct:
        score += 1
        print(f"You are right! Current Score : {score}")
        person_a = person_b
        person_b = random.choice(data_dic)