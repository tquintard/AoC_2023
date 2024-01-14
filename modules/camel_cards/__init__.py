MAP = {'2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
       'T': 'A', 'J': 'B', 'Q': 'C', 'K': 'D', 'A': 'E'}
OPT_HAND = {(25, 17, 13): 25, (11,): 17, (7,): 11, (5,): 7}


def handhex(hand: str) -> str:
    return ''.join([MAP[card] for card in hand if card in MAP.keys()])


def hand_value(hand: str) -> int:
    return sum([hand.count(card) for card in hand])


def hand_opt(hand: list) -> int:
    # when the hand is a two pairs, it can be optimised as a FOK or a full house
    if hand[2] == 9:
        return 17 if hand[0].count('1') == 2 else 13
    else:
        for key in OPT_HAND.keys():
            if hand[2] in key:
                return OPT_HAND[key]
