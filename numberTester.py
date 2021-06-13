#  numberTester.py
#  Samuel Robinson 05/28/2021
"""calculates the square and cubes of even numbers between 1-10"""
"""outputs result in a table"""

from evenNumber import EvenNumbers


number = EvenNumbers()
print("number\tsquare\t cube")

for x in [0, 2, 4, 6, 8, 10]:

    squaredNumber = number.squareNumber(x)
    cubedNumber = number.cubeNumber(x)
    number.cubeNumber(x)
    print(f'\t{x}\t\t{squaredNumber}\t\t{cubedNumber}')



