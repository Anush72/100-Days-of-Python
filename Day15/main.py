# Project Coffee Machine

from data import MENU,resources

# function to print resource
def print_report(resource):
    """

    :param resource:
    :return: report
    """
    water = resource['water']
    milk = resource['milk']
    coffee = resource['coffee']
    money = resource['money']
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}"



# function to check resource and check the ingredients is sufficient or not
def check_resources(menu,resource,ingredient):
    for item in menu[ingredient]["ingredients"]:
        required = menu[ingredient]["ingredients"][item]
        available = resource[item]

        if available < required:
            print(f"Sorry there is not enough {item}")
            return False

    return True

# process coin
def coin():
    """
    :return: total money
    """
    print("Please insert coins")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return total_money

# checking the transaction
def check_transaction(menu,ingredient,money):
    """

    :param menu:
    :param ingredient:
    :param money:
    :return: transaction successful or not
    """
    transaction = True
    required_money = menu[ingredient]['cost']
    if money < required_money:
        print("Sorry that's not enough money")
        transaction = False
    if money > required_money:
        back = round((money-required_money),2)
        print(f"Here is ${back} in change")
    return transaction

# Updating the resources
def update_resource(menu,resource,ingredient):
    for item in menu[ingredient]["ingredients"]:
        required = menu[ingredient]["ingredients"][item]
        resource[item] -=required
    resource["money"] += menu[ingredient]['cost']


# Coffee Machine
coffee_machine = True
while coffee_machine:
    user_item = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # checking input
    if user_item == 'report':
        print(print_report(resources))
    elif user_item == 'off':
        coffee_machine = False
        print("Thank You for Using me")
    elif user_item not in MENU:
        print("Invalid Choice")
    else:
        # checking for resources
        if check_resources(menu=MENU,resource=resources,ingredient=user_item):
        # telling user to insert coin if resource is available
           money_own =  coin()
        # checking for transaction
           if check_transaction(menu=MENU,ingredient=user_item,money= money_own):
                print(f'Here is your drink {user_item}. Enjoy')
                update_resource(menu=MENU,resource=resources,ingredient=user_item)





