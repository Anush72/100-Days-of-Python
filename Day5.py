# Python Loops

# Loops - Happen again and again

#Loop in List
fruits = ["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")


student_scores = [180,124,165,173,189,169,146]
# sum using for loop
a = 0
for i in student_scores:
    a +=i
print(a)
# Simple using sum function
b = sum(student_scores)
print(b)

# finding the max number from list
max_score = 0
for score in student_scores:
    if max_score < score:
        max_score = score
print(max)

# for loop and range
for number in range(1,11):
    print(number)

total_sum = 0
for number in range(1,101):
    total_sum += number
print(total_sum)

# FizzBuzz
# Program to print the number 1 to 100
# When Number is divisible by 3 then its Fizz
# When Number is divisible by 5 then its Buzz
# When Number is divisible by both then its FizzBuzz

# for loop with range from 1 to 100
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)
