# Lucky Sevens (Sim version)
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


def track_best(round_ct, bank):
    """
    Track which round player earned the highest amount
    :param round_ct: {int} round number
    :param bank: {float} current earning
    :returns: {float} highest earning so far
    :returns: {int} round of best earning so far
    """
    global best_earning, best_round

    if bank > best_earning:
        best_earning = bank
        best_round = round_ct

    return best_earning, best_round


def evaluate_roll(roll, pot):
    """
    Pay out or take money from player's bank based on the roll
    :param roll: {int} 2-12 for 2 dice
    :param pot: {float} player's total bank
    :return:
    """
    if roll == 7:
        pot += 4
    else:
        pot -= 1

    return pot


def roll_all(bank):
    """
    While sim has money in the bank, continue playing round (toggle debug statement to see individual round results)
    :param bank: {float} sim's cash
    :return: {int} the number of rolls it took before sim went broke
    """
    global best_earning, best_round
    round_ct = 0

    while bank > 0:
        round_ct += 1
        round_roll = roll_2_dice()
        bank = evaluate_roll(round_roll, bank)

        # print("Round ", round_ct, " | Rolled ", round_roll, " | Pot: $", format(pot, ',.2f'), sep='') # debug

        best_earning, best_round = track_best(bank, round_ct)

    return round_ct


def main():
    global best_round
    best_round = 0
    global best_earning
    best_earning = 0

    print("Welcome to Lucky 7's simulator")
    buy_in = round(float(input("Enter buy-in amount: $")), 2)
    if buy_in < 0:
        buy_in = validate_bet("buy-in", buy_in)

    total_rolls = roll_all(buy_in)

    print("You made it through", total_rolls, "rolls")
    print("You peaked at round ", best_round, " with $", format(best_earning, ',.2f'), sep='')


main()
