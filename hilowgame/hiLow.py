# High-Low Game
# Date Created: 5/24/20
# Last Modified: 5/24/20

import random


def game_num():
    """
    return a random number for gameplay
    :return: int between 1-100
    """
    return random.randint(1, 100)


def main():
    guess = 0
    ct = 0

    print("Welcome to the High Low Game!!!")
    print("Computer is guessing...")
    goal = game_num()

    while guess != goal:
        guess = int(input("Enter a integer between 1-100: "))

        if guess < 0:
            print("No negative numbers")
        elif guess > 100:
            print("No numbers above 100")
        elif guess > goal:
            print("Too high!")
            ct += 1
        elif guess < goal:
            print("Too low!")
            ct += 1

    print("\nYou guessed it!")
    print("Number of Guesses = ", ct)


main()
