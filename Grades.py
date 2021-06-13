#  Grades.py
#  Samuel Robinson 05/28/2021

import math

class Student:

    """gathers grades and creates an average"""
    @staticmethod
    def semester_grade(exam1, exam2, exam3, final):
        average = (exam1 + exam2 + exam3 + final + final) / 5
        average = math.ceil(average)
        return average

    """assigns a letter grade for the average"""
    @staticmethod
    def semester_letter(average):
        if (average >= 90):
            grade = 'A'
        elif (average >= 80):
            grade = 'B'
        elif (average >= 70):
            grade = 'C'
        elif (average >= 60):
            grade = 'D'
        else:
            grade = 'F'
        return grade
