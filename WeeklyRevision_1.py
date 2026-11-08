# creating the student performance report

# taking input from user
name = input('Write your name:\n')
# asking student to how many subject they want enter
number_of_subjects = int(input('Enter the number of Subjects you wanna put:\n'))

subjects = []
subjects_grades = []


# Asking student to enter three subject names and grades
for i in range(0,number_of_subjects):
    subject = input('Enter the Subject: \n')
    mark = int(input(f'Enter the Grade you obtain in {subject}:\n'))
    subjects.append(subject)
    subjects_grades.append(mark)

# defining function tp calculate average
def average_marks(scores):
    total = sum(scores)
    average_mark = total/ len(scores)
    return average_mark

# defining function to determine they pass or fail
def check_pass(scores):
    status = 'Pass'
    for score in scores:
        if score < 50:
            status = 'Fail'
    return status

# calculating the grades
def calculate_grade(average):
    grade = ''
    if average < 50:
        grade = 'F'
    elif 50 <= average < 70:
        grade = 'D'
    elif 70 <= average < 80:
        grade = 'C'
    elif 80 <= average < 90:
        grade = 'B'
    else:
        grade = 'A'
    return grade

# calculating all mark and grade
mark_average = average_marks(subjects_grades)
pass_or_fail = check_pass(subjects_grades)
total_grade = calculate_grade(mark_average)

# printing the student performance
print('''================================STUDENT PERFORMANCE REPORT================================''')
print(f'Student : {name}\n')

# printing each subject
print('Scores:')
for i in range(number_of_subjects):
    print(f'{subjects[i]}: {subjects_grades[i]}')

print(f'Average: {mark_average}')
print(f'Grade: {total_grade}')
print(f'Status: {pass_or_fail}')



