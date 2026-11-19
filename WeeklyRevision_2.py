# Personal Expenses Tracker

# asking user to store the expenses name, amount and category
def add_expenses(expenses):
    """
    :return: expenses
    """
    # list to store expense of user
    asking = True

    while asking:
        expense = {}
        expense_name = input("Enter expense name: ")
        expense_amount = float(input("Enter expense amount: "))
        expense_category = input("Enter expense category: ")
        expense["name"] = expense_name
        while expense_amount <= 0:
            expense_amount = float(input("Invalid amount! Please enter an amount greater than zero."))
        expense["amount"] = expense_amount
        expense["category"] = expense_category
        expenses.append(expense)
        print("Expense added Successfully")
        add_expense = input("Do you want to add another expenses? (yes/no) ")
        while add_expense !='yes' and add_expense !='no':
            add_expense = input("Invalid Choice! Enter yes or no ")
        if add_expense == 'no':
            asking = False
    return expenses



# Function to View all Expenses
def view_expenses(a):
    """
    Display all expenses from the provided lists
    :param a: take expenses
    :return: None
    """
    i = 0
    for b in a:
        i += 1
        print(f"{i} {b['name']} - {b['amount']} - {b['category']}")

# Sum of total spending
def total_spending(amounts):
    """
    :param amounts: list of expenses
    :return: total sum and number of items
    """
    number_of_items= 0
    total = 0
    for amount in amounts:
        total += amount['amount']
        number_of_items += 1
    return total,number_of_items

# returning highest spending

def highest_spending(spend):
    """
    :param spend: list of expenses
    :return: highest amount spend on items
    """
    highest_expense = {}
    highest_amount = 0
    for expense in spend:
        if expense['amount'] > highest_amount:
            highest_amount = expense['amount']
            highest_expense = expense
    return highest_expense


# function to sum finding according to category

def total_category(expenses):

    category_spending = {}

    for expense in expenses:
            category = expense['category']
            if expense['category'] not in category_spending:
                amount = expense['amount']
                category_spending[category] = amount
            else:
                category_spending[category] += expense['amount']
    return category_spending


# Asking User for Adding Expenses and Looking
total_expenses = []
personal_tracker = True
while personal_tracker:
    print("--Personal Expense Tracker--\n")
    print("1. Add Expense\n2. View All Expense\n3. Total Spending\n4. Higest Expense\n5. Spending by Category\n6. Exit")
    user_choice = int(input("Enter Your Choice: "))
    if user_choice == 1:
        total_expenses = add_expenses(total_expenses)
    elif user_choice == 2:
        print("\n--ALL EXPENSES --")
        view_expenses(total_expenses)
    elif user_choice == 3:
        print("\n--TOTAL SPENDING--")
        totalspend,n = total_spending(total_expenses)
        print(f"You have spend {totalspend} with {n} items.")
    elif user_choice == 4:
        print("\n--HIGHEST SPENDING--")
        maxspend = highest_spending(total_expenses)
        print(f"Yu have spend {maxspend['amount']} in {maxspend['name']} on category of {maxspend['category']} ")
    elif user_choice == 5:
        print("\n--TOTAL EXPENSES BY CATEGORY--")
        categories = total_category(total_expenses)
        i = 0 
        for category, amount in categories.items():
            i += 1
            print(f"{i}. {category} - {amount: .2f}")
        
    elif user_choice == 6:
        personal_tracker = False
    else:
        print('Please enter from 1 to 6 according to option')
    




