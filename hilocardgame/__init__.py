import random as r


def build_deck() -> list:
    """
    Create deck

    :return: {list} a deck of card objects
    """
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    ranks = [
        'A',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        'J',
        'Q',
        'K',
    ]
    deck = []

    for suit in suits:
        for j in range(len(suits)):
            card = {
                "suit": suit,
                "rank": ranks[j],
                "value": j
            }
            deck.append(card)

    return deck


def compare(card1: dict, card2: dict) -> int:
    """
    Compare two cards

    :param card1: {dict} current card
    :param card2: {dict} next card
    :return: {int} the difference in values
    """
    return card1['value'] - card2['value']


def guess(card1: dict, card2: dict) -> bool:
    """
    Have player make a guess and evaluate

    :param card1: {dict} current card
    :param card2: {dict} next card
    :return: {bool} true is guess right, false if not
    """
    print(f"The current card is {card1['rank']} of {card1['suit']}")
    selection = str(input('Will the next card be higher h or lower l?: '))
    if selection == 'h':
        return compare(card1, card2) < 0
    elif selection == 'l':
        return compare(card1, card2) > 0
    else:
        print("Type h or l")
        return False


def play_game() -> None:
    """
    Main game loop

    :return: void
    """
    deck = build_deck()
    # print(deck)
    r.shuffle(deck)

    name = str(input("What's your name?: "))
    print(name)

    current_card = deck.pop()

    score = 0
    while score < 5 and 0 < len(deck):
        next_card = deck.pop()
        print("-----------------------")
        if guess(current_card, next_card):
            score += 1
            print(f"Congrats {name}! Score = {score}")
        else:
            print(f"Wrong. Score = {score}")
        current_card = next_card

    if len(deck) > 0:
        print("You won")
    else:
        print("You lost")


def main() -> None:
    play_game()


main()
