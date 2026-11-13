# importing the libraries
from random import choice
from art import logo

# checking whether the card list contain ace


def blackjack():
    # List of all cards value
    print(logo)
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    user_card = []
    computer_card = []
    user_sum = 0
    computer_sum = 0
    for i in range(0, 2):
        user_card.append(choice(cards))
        computer_card.append(choice(cards))

    for card in user_card:
        user_sum += card
    for card in computer_card:
        computer_sum += card
    game_on = True
    # Random Two Cards from Deck
    while game_on:
        print(f"Your Cards : {user_card},current score: {user_sum}")
        print(f"Computer's first card: {computer_card[0]}")
        user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_choice == 'y':
            new_card_user = choice(cards)
            new_card_computer = choice(cards)
            user_card.append(new_card_user)
            computer_card.append(new_card_computer)
            user_sum += new_card_user
            computer_sum += new_card_computer
            if 11 in user_card and 21 < user_sum:
              user_sum -= 10
            elif user_sum > 21:
                print(f'You go over 21. You score is {user_sum}')
                wanna_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
                if wanna_play == 'y':
                    blackjack()
                else:
                    game_on = False
                    print('Thank you for game')
        else:
            # Either Ace value 1 or 11 depends upon the sum
            if 11 in computer_card and 21 < computer_sum:
                computer_sum -= 10
            if 11 in user_card and 21 < user_sum:
              user_sum -= 10
            while computer_sum < 16:
                new_card = choice(cards)
                computer_card.append(new_card)
                computer_sum += new_card
            print(f"Your final hand : {user_card},final score: {user_sum}")
            print(f"Computer's final hand: {computer_card}, final score: {computer_sum}")
            if user_sum == computer_sum:
                print("Draw")
            elif user_sum == 21:
                print('You hit blackjack you won game')
            elif computer_sum == 21:
                print('Computer hit blackjack. You lose')
            elif computer_sum > 21:
                print("Computer went over. You win")
            elif computer_sum > user_sum:
                print('You lose.')
            elif computer_sum < user_sum:
                print('You win')
            wanna_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


            if wanna_play == 'y':
                blackjack()
            else:
                game_on = False
                print('Thank you for game')
blackjack()