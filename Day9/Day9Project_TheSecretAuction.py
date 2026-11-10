logo = r'''
         ___________
         \         /
          )_______(
          |"""""""|_.-._,.---------.,_.-._
          |       | | |               | | ''-.
          |       |_| |_             _| |_..-'
          |_______| '-' `'---------'` '-'
          )"""""""(
         /_________\\
       .-------------.
      /_______________\\
'''
auction_name = {}
print(logo)
bid_on = True
while bid_on:
    print('Welcome to the secret auction program.')
    name = input('What is your name?')
    money = int(input('What is your bid?$'))
    auction_name[name] = money
    game_continue = input("Are there any other bidders? Type 'yes' or 'no.\n").lower()
    if game_continue == 'no':
        bid_on = False
        bid = 0
        winner = ''
        for name,money in auction_name.items():
            if money > bid:
                bid = money
                winner = name
        print(f'The winner is {winner} with bid of $ {bid}')

