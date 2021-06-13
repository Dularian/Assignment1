#   numberGuesser.py
#   Samuel Robinson 5/31/2021
import random
"""number guesser game in a range of 1-50 """
"""given three attempts to guess correct answer"""


guess = int
count = 0
play_again = 1

while(play_again == 1):
    correctnumber = random.randint(1, 50)
    print("Guess my number between 1-50 within three guesses.")

    "gathers three guesses and checks for a match"
    while(count < 3 and guess != correctnumber):

        guess = int(input())
        while (guess < 1 or guess > 50):
            print("Invalid range. guess a number between 1-50")
            guess = int(input())

        if(guess < correctnumber and count < 2):
            print("Too low. Try again.")
        elif(guess > correctnumber and count < 2):
            print("Too high. Try again.")

        count = count + 1

    "Output for after three guesses or correct answer"
    if(guess == correctnumber):
        print("Good job you guessed it correctly.")
        print("The answer was: ", correctnumber)
        print("You guessed: ", guess, "on try #", count)
    else:
        print("You did not guess the number correctly.")
        print("The answer was: ", correctnumber)
    print("Would you like to play again? type 'y' to retry.")
    if(str(input()) == 'y'):
        play_again = 1
        count = 0
    else:
        play_again = 0