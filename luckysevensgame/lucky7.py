# Lucky Sevens (Game version)
# Date Created: 5/20/20
# Last Modified: 5/21/20

import random

best_earning = 0
best_round = 0


def roll_2_dice():
    """
    roll two 6-sided dice
    :return: {int} 2-12
    """
    return random.randint(2, 13)


def validate_bet(buy_type, cash_in):
    """
    Validate forms of betting by the player such that they are not negative. Customizable prompts for exact bet types
    :param buy_type: {str} type of bet to be printed in UI prompts
    :param cash_in: {float} cash amount entered by player
    :return: validated bet amount
    """
    while cash_in < 0:
        print("Invalid", buy_type)
        cash_in = round(float(input("Enter " + buy_type + ": $")), 2)

    return cash_in


def evaluate_round(roll, pot, bank):
    """
    Determine win or loss and award double the bet for win, or take bet from pot for loss
    :param roll: {int} 2-12 from rolling 2 dice
    :param pot: {float} player's round bet
    :param bank: {float} player's total pot
    :return: {float} the player's pot after round
    """
    if roll == 7:
        bank += (2 * pot)
    else:
        bank -= pot

    return bank


def track_best(round_ct, bank):
    """
    Track which round player earned the highest amount
    :param round_ct: {int} round number
    :param bank: {float} current earning
    """
    global best_earning
    global best_round

    if bank > best_earning:
        best_earning = bank
        best_round = round_ct


def play_rounds(bank):
    """
    Main gameplay loop while player has money in their pot
    :param bank: {float} player's money
    """
    playing = True
    round_ct = 1

    while bank > 0 and playing:
        print("Round", round_ct)
        pot = round(float(input("Place your bet (0 for all-in): $")), 2)
        if pot < 0:
            pot = validate_bet("bet", pot)

        while pot > bank:
            print("Bet cannot be bigger than your bank.")
            pot = round(float(input("Place your bet: $")), 2)

        if pot == 0 or pot == bank:
            pot = bank
            print("All-in...")

        round_roll = roll_2_dice()
        print("You rolled", round_roll)

        bank = evaluate_round(round_roll, pot, bank)
        print("Pot: $", format(bank, ',.2f'), sep='')

        track_best(round_ct, bank)
        round_ct += 1

        if bank > 0:
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
    bank = round(float(input("Enter buy-in: $")), 2)
    if bank < 0:
        bank = validate_bet("buy-in", bank)

    play_rounds(bank)

    print("You peaked at round ", best_round, " with a maximum earning of $", format(best_earning, ",.2f"), sep='')


main()
