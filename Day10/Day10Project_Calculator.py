# importing module
from art import logo


# function for doing operation

def calculation(a,b,operation):
    """
    :param a: first number
    :param b: second number
    :param operation: calculation you want to perform
    :return: result after calculation
    """

    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    else:
        return 'Please put valid operator.'
def calculator():
    operate = ['+','-','*','/']
    print(logo)
    first_number = float(input("Whats the first number?:\t"))
    wanna_calculations = True
    while wanna_calculations:
        for i in operate:
            print(i)
        operations = input("Pick an operation:\t")
        second_number = float(input("Whats the second number?: \t"))
        output = calculation(first_number,second_number,operations)
        choice = input(f"Type 'y' to continue calculating with {output} or type 'n' to start a new calculations ")
        if choice == 'y':
            first_number = output
        else:
            print('\n'*20)
            wanna_calculations = False
            calculator()


calculator()