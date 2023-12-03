from typing import List
from functools import partial
from .sub_modules.cubes_game import games


def main(inputs: List[str]) -> List[str]:
    # Iterate through each part of the day's puzzle
    sol = []
    for part_num in [1, 2]:
        # Calculate the solution for the current part
        sol.append(str(sum(map(partial(games, part=part_num), inputs))))
    return sol
