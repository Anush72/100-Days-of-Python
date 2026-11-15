# Personal Expenses Tracker

# asking user to store the expenses name, amount and category
def add_expenses():
    """
    :return: expenses
    """
    # list to store expense of user
    expenses = []
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

expenses = [
    {"name": "Coffee", "amount": 5.50, "category": "Food"},
    {"name": "Groceries", "amount": 45.00, "category": "Food"},
    {"name": "Transport", "amount": 12.00, "category": "Travel"}
]



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
    for expense in expenses:
        if expense['amount'] > highest_amount:
            highest_amount = expense['amount']
            highest_expense = expense
    return highest_expense
