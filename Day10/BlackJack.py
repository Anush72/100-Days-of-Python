# importing the lists
import random
# function to calculate score
def calculate_score(cards):
    """

    :param cards: list
    :return: sum of list
    """
    total_sum = sum(cards)
    while total_sum > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        total_sum = sum(cards)
    return total_sum

#  Lists of cards and two empty hand
list_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_hand = []
computer_hand = []
game_on = True
# Distributing two random cards to each hand
for i in range(0,2):
    user_hand.append(random.choice(list_cards))
    computer_hand.append(random.choice(list_cards))
user_score = calculate_score(user_hand)
computer_score = calculate_score(computer_hand)
if len(user_hand) == len(computer_hand) == 2 and user_score == computer_score == 21:
    print("Its draw")
    game_on = False
elif len(user_hand) == 2 and user_score == 21:
    print("You hit blackjack")
    game_on = False
elif len(computer_hand) == 2 and computer_score == 21:
    print('Computer hit blackjack')
    game_on = False
while game_on:
    print(f'You have {user_hand} with score: {user_score}')
    print(f'Computer has first card {computer_hand[0]}')
    user_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    if user_choice == 'y':
        user_hand.append(random.choice(list_cards))
        user_score = calculate_score(user_hand)
        if user_score > 21:
            print("You went over 21.You lose!")
            game_on = False
        elif user_score == 21:
            game_on = False
    # checking the natural blackjack
    if len(user_hand) == len(computer_hand) and user_score == computer_score:
        print("Its draw")
    elif len(user_hand) == 2 and user_score == 21:
        print("You hit blackjack")
    elif len(computer_hand) == 2 and computer_score == 21:
        print('Computer hit blackjack')
