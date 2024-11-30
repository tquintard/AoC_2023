from typing import List
from functools import partial
from .recalibrate import recalibrate_line


def main(inputs: List[str]) -> List[int]:
    # Iterate through each part of the day's puzzle for recalibration of values
    sol = list()
    for part_num in (1, 2):
        # Calculate the solution for the current part
        sol.append(
            str(sum(map(partial(recalibrate_line, part=part_num), inputs))))
    return sol
