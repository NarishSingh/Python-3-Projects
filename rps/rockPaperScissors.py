# Rock, Paper, Scissors Game
# Date Created: 5/24/20
# Last Modified: 5/24/20

import random


def get_player_move():
    """
    Print UI for and get player's move, with validation
    :return: int 1-3 corresponding to Rock, Paper, Scissors
    """
    print("1 | Rock")
    print("2 | Paper")
    print("3 | Scissors")

    move = int(input("Your move: "))

    while move < 1 or move > 3:
        print("invalid move")
        move = int(input("Your move: "))

    return move


def get_comp_move():
    """
    Get a random move from computer
    :return: int randomized from 1-3 corresponding to Rock, Paper, Scissors
    """
    return random.randint(1, 3)


def move_to_string(move):
    """
    Convert move to string
    :param move: int 1-3
    :return: String where 1-3 correspond to Rock, Paper, Scissors
    """
    if move == 1:
        return "Rock"
    elif move == 2:
        return "Paper"
    elif move == 3:
        return "Scissors"
    else:
        return "Invalid move"


def evaluate_round(comp_move, player_move):
    """
    evaluate the round
    :param comp_move: int 1-3
    :param player_move: int 1-3
    :return: String indicating round win, loss, or tie for player
    """
    player_win = (player_move == 1 and comp_move == 3) or (player_move == 2 and comp_move == 1) or (
            player_move == 3 and comp_move == 2)

    if comp_move == player_move:
        print("Tied!")

        return "tie"
    elif player_win:
        print("Player's", move_to_string(player_move), "beats Comp's", move_to_string(comp_move), "!!!")

        return "win"
    else:
        print("Player's", move_to_string(player_move), "loses to Comp's", move_to_string(comp_move), "...")

        return "loss"


def play_again():
    """
    Print UI for and get player's choice to play again, with validation
    :return: boolean True to play again, false to end rounds
    """
    print("Play again?  1 - Yes | 2 - No")
    choice = int(input())

    while choice < 1 or choice > 2:
        print("Invalid choice")
        choice = int(input())

    if choice == 1:
        return True
    elif choice == 2:
        return False


def main():
    round_ct = 0
    playing = True
    player_win = 0
    comp_win = 0

    print("===Rock, Paper, Scissors===")
    while playing:
        round_ct += 1
        print("Round", round_ct)

        comp = get_comp_move()
        player = get_player_move()
        result = evaluate_round(comp, player)

        if result == "win":
            player_win += 1
        elif result == "loss":
            comp_win += 1

        playing = play_again()
        print("-------")

    print("Player = ", player_win, "| Comp = ", comp_win)


main()
