"""
Number guessing game
Pick a target, loop with while, compare each guess, break on match.
"""

import random

target = random.randint(1, 25)


while True:
    try:
        guess = int(input("Enter your guess"))
    except:
        print("Please enter a valid guess")
        continue
    if guess == target:
        print("Awesome!, You guessed")
        break
    elif guess > target:
        print("You guessed a greater number")
    else:
        print("You guessed a lower number")
