# Grading Program
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# empty dictionary
student_grades = {}

# Loop through dictionary
for name in student_scores:
    score = student_scores[name]
    if 90 < score < 100:
        student_grades[name] = 'Outstanding'
    elif 80 < score <= 90:
        student_grades[name] = 'Exceeds'
    elif 70 < score <= 80:
        student_grades[name] = 'Acceptable'
    else:
        student_grades[name] = 'Fail'

print(student_grades)