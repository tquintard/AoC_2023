from typing import List
from .sub_modules.gondola import get_partnumber, get_symbols, sum_pn_or_gr


def main(inputs: List[str]) -> List[str]:

    # Initialise the list and dictionnaries
    sol = list()
    part_numbers = dict()
    symbols = dict()

    # Scan the input to find all the part number and symbols positions
    for i, line in enumerate(inputs):
        get_partnumber(i, line, part_numbers)
        get_symbols(i, line, symbols)

    # Sum all part number adjacent to a symbol (part 1) or sum all the gear ratio (part 2)
    for part_num in [1, 2]:
        sol.append(str(sum_pn_or_gr(part_numbers, symbols, part=part_num)))

    return sol
