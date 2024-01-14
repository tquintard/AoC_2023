from typing import List
from .winning_cards import nb_winning_cards
import numpy as np


def main(inputs: List[str]) -> List[int]:

    # Initialise the lists
    sol = [0, 0]
    card_instance = np.array([1 for _ in range(len(inputs))])
    # Iterate trhough all the lines (1 scratchcard per line)
    for i, line in enumerate(inputs):
        # Calculate the nb of winning numbers in actual card
        nb_wins = nb_winning_cards(line)
        if nb_wins != 0:
            # If at least 1 win then add the points to solution 1
            # and increment, by actual card instance,
            # the instances of the next nb_wins cards to calculate solution 2
            sol[0] += 2**(nb_wins-1)
            card_instance[i + 1: i + nb_wins + 1] += 1 * card_instance[i]
    sol[1] = sum(card_instance)
    return sol
