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


def track_best(bank, round_num):
    """
    Track best earning and round number
    :param bank: {float} current earning
    :param round_num: {int} current round
    """
    global best_earning
    global best_round

    if bank > best_earning:
        best_earning = bank
        best_round = round_num


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
    round_ct = 0

    while bank > 0:
        round_ct += 1
        round_roll = roll_2_dice()
        bank = evaluate_roll(round_roll, bank)

        # print("Round ", round_ct, " | Rolled ", round_roll, " | Pot: $", format(pot, ',.2f'), sep='') # debug

        track_best(bank, round_ct)

    return round_ct


def main():
    global best_round
    best_round = 0
    global best_earning
    best_earning = 0

    print("Welcome to Lucky 7's simulator")
    buy_in = round(float(input("Enter buy-in amount: $")), 2)
    while buy_in < 0:
        print("Invalid amount")
        buy_in = round(float(input("Enter buy-in amount: $")), 2)

    total_rolls = roll_all(buy_in)

    print("You made it through", total_rolls, "rolls")
    print("You peaked at round ", best_round, " with $", format(best_earning, ',.2f'), sep='')


main()
