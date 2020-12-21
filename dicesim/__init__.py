import random as rand

MIN = 1
MAX = 6


def roll(numDice: int) -> int:
    """
    Roll any number of dice once

    :param numDice: {int} number of dice to roll
    :return: {int} roll result
    """
    return rand.randint(MIN * numDice, MAX * numDice)


def main() -> None:
    rolls = []

    numDice = int(input("Enter number of dice: "))
    numRolls = int(input("Enter number of rolls: "))

    for n in range(numRolls):
        rolls.append(roll(numDice))

    for r in rolls:
        print(r, end=' ')


main()
