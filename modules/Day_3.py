from typing import List
from .sub_modules.gondola import get_partnumber, get_symbols, get_gears_ratio


def main(inputs: List[str]) -> List[str]:

    # Initialise the list and dictionnaries
    sol = [0, 0]
    part_numbers = dict()
    symbols = dict()

    # Scan the input to find all the part number and symbols positions
    for i, line in enumerate(inputs):
        get_symbols(i, line, symbols)

    symbols_vicinity = {value for sub_set in symbols.values()
                        for value in sub_set}
    for i, line in enumerate(inputs):
        sol[0] += get_partnumber(i, line, part_numbers, symbols_vicinity)

    # Sum all the gear ratio (part 2)
    sol[1] = get_gears_ratio(part_numbers, symbols)

    return sol
