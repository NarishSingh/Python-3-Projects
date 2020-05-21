# Lucky Sevens (Game version)
# Date Created: 5/20/20
# Last Modified: 5/20/20

import random

best_earning = 0
best_round = 0


def roll_2_dice():
    """
    roll two 6-sided dice
    :return: {int} 2-12
    """
    return random.randint(2, 13)


def evaluate_round(roll, bet, pot):
    """
    Determine win or loss and award double the bet for win, or take bet from pot for loss
    :param roll: {int} 2-12 from rolling 2 dice
    :param bet: {float} player's round bet
    :param pot: {float} player's pot
    :return: {float} the player's pot after round
    """
    if roll == 7:
        pot += (2 * bet)
    else:
        pot -= bet

    return pot


def track_best(round_ct, pot):
    """
    Track which round player earned the highest amount
    :param round_ct: {int} round number
    :param pot: {float} current earning
    """
    global best_earning
    global best_round

    if pot > best_earning:
        best_earning = pot
        best_round = round_ct


def play_rounds(pot):
    """
    Main gameplay loop while player has money in their pot
    :param pot: {float} player's money
    """
    playing = True
    round_ct = 1

    while pot > 0 and playing:
        print("Round", round_ct)
        bet = round(float(input("Place your bet (0 for all-in): ")), 2)
        while bet > pot:
            print("Bet cannot be bigger than your pot.")
            bet = round(float(input("Place your bet: $")), 2)

        if bet == 0 or bet == pot:
            bet = pot
            print("All-in...")

        round_roll = roll_2_dice()
        print("You rolled", round_roll)

        pot = evaluate_round(round_roll, bet, pot)
        print("Pot: $", format(pot, ',.2f'), sep='')

        track_best(round_ct, pot)
        round_ct += 1

        if pot > 0:
            new_round = int(input("Play another round? (1 = yes | 2 = no): "))
            if new_round == 1:
                playing = True
            else:
                playing = False
        else:
            playing = False

        print("-------")


def main():
    global best_round
    best_round = 0
    global best_earning
    best_earning = 0

    print("Welcome to Lucky Sevens")
    pot = round(float(input("Enter buy-in: $")), 2)
    while pot < 0:
        print("Invalid buy-in")
        pot = round(float(input("Enter buy-in: $")), 2)

    play_rounds(pot)

    print("You peaked at round ", best_round, " with a maximum earning of $", format(best_earning, ",.2f"), sep='')


main()
