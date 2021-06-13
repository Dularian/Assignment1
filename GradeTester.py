#  Grades.py
#  Samuel Robinson 05/28/2021
"""gathers student grades, gets average, and assigns them a letter grade"""
"""Final will count twice"""

from Grades import Student

student = Student()
print('Please enter the first exam grade.')

try:
    examCheck = int(input())
    while(examCheck <= 0 or examCheck > 100):
        print("not valid range. Try again.")
        examCheck = int(input())
    exam1 = examCheck

except ValueError:
    print('not a valid number, run again.')
    exit()

print('Please enter the second grade.')

try:
    examCheck1 = int(input())
    while (examCheck1 <= 0 or examCheck1 > 100):
        print("not valid range. Try again.")
        examCheck1 = int(input())
    exam2 = examCheck1
except ValueError:
    print('please enter a number between 0-100. Run again.')
    exit()

print('Please enter the third grade.')

try:
    examCheck2 = int(input())
    while (examCheck2 <= 0 or examCheck2 > 100):
        print("not valid range. Try again.")
        examCheck2 = int(input())
    exam3 = examCheck2
except ValueError:
    print('not a valid number, run again.')
    exit()

print('Please enter the final grade.')

try:
    examCheck3 = int(input())
    while (examCheck3 <= 0 or examCheck3 > 100):
        print("not valid range. Try again.")
        examCheck3 = int(input())
    final = examCheck3
except ValueError:
    print('not a valid number, run again.')
    exit()

average = student.semester_grade(exam1, exam2, exam3, final)
letter = student.semester_letter(average)

print("You received a grade of: ", letter)
