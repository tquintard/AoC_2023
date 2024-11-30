from typing import List, Tuple
import re
from typing import Tuple
from .camel_cards import handhex, hand_value, hand_opt


def main(inputs: List[str]) -> Tuple[int]:
    pattern = r'(?:(\b\w*\b)\s(\d+))\n?'
    hands = list(map(list, re.findall(pattern, inputs)),)
    sol = []
    for part in (1, 2):
        for i, hand in enumerate(hands):
            if part == 1:
                hands[i] = [handhex(hand[0]),
                            int(hand[1]), hand_value(hand[0])]
            else:
                if 'B' in hand[0]:
                    hand[0] = hand[0].replace('B', '1')
                    hands[i][2] = hand_opt(hand)
        hands = sorted(hands, key=lambda x: (x[2], x[0]))
        sol.append(sum([hand[1] * i for i, hand in enumerate(hands, start=1)]))
    return sol
