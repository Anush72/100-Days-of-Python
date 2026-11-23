from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
coffee_machine = True
while coffee_machine:
    list_item = menu.get_items()
    items = input(f"What would you like? {list_item}: ").lower()
    # checking the input
    if items == 'report':
        coffee_maker.report()
        money_machine.report()
    elif items == 'off':
        coffee_machine = False
        print('Thank You for Using me')
    else:
        item = menu.find_drink(items)
        # checking whether we have sufficient money or not
        if coffee_maker.is_resource_sufficient(item):
            if money_machine.make_payment(item.cost):
                coffee_maker.make_coffee(item)




