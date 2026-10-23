# Project Tip Calculator

print("Welcome to the Tip calculator!")

# Getting Input from User
total_bill = input("How much the total bill? $")
tip_percentage = input("How much tip would you like to give? 10,12 or 15?")
people_split = input("How many people to split the bill? $")

# Calculation
tip  = float(total_bill) * int(tip_percentage)/100
total_bill_with_tip = float(total_bill) + tip
split = total_bill_with_tip / int(people_split)
print(f"Each person should pay: {round(split,2)}")
