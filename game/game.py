# Guessing game.  Get input from user for the level must be positive integer then using random get a random number between 1 and the number
# that was inputed by the user. Then let the user guess the number letting the user
# know if the guess was over or under.  Let the user keep guessing until the correct number is guessed

import random

while True:
    try:
        l = int(input("Level: "))

        if l > 0:
            break
    
    except ValueError:
        pass

answer = random.randint(1, l)

while True:

    try:
        guess = int(input("Guess: "))

        if guess > 0:
            if guess == answer:
                print("Just right!")
                break
            elif guess < answer:
                print("Too small!")
            elif guess > answer:
                print("Too large!")

    except ValueError:
        pass

