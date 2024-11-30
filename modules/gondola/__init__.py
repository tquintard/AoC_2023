import re
from typing import Set, Tuple
from collections import defaultdict


def get_partnumber(line_idx: int, line: str, part_numbers: dict, symbols_vicinity: set) -> Set[Tuple[int]]:
    matches = re.finditer(r'\d+', line)
    sum_parts = 0
    for match in matches:
        start, end = match.start(), match.end()
        if any((line_idx, col) in symbols_vicinity for col in range(start, end)):
            part_num = int(match.group())
            sum_parts += part_num
            part_numbers[(part_num, (line_idx, start))] = [(line_idx, col)
                                                           for col in range(start, end) if (line_idx, col) in symbols_vicinity]
    return sum_parts


def get_symbols(line_idx: int, line: str, symbols: dict) -> Set[Tuple[int]]:
    matches = re.finditer(r'[^\d.]', line)
    for match in matches:
        position = match.start()
        symbols[(match.group(), (line_idx, position))] = list()
        for row in range(-1, 2):
            for col in range(-1, 2):
                symbols[(match.group(), (line_idx, position))].append(
                    (line_idx + row, position + col))


def get_gears_ratio(part_numbers: dict, symbols: dict) -> int:
    # Update symbols dict
    symbols = {key: value for key, value in symbols.items() if key[0] == '*'}
    gears = defaultdict(list)
    for key, value in part_numbers.items():
        # find which * is in the vicinity of the number
        for position, viscinity_pos in list(symbols.items()):
            if any(pos in viscinity_pos for pos in value):
                gears[position].append(int(key[0]))
                # Delete a * position if there are more than 2 adjacents part number to optimise the research
                if len(gears[position]) > 2:
                    del symbols[position]
                break

    return sum([v[0]*v[1] for v in gears.values() if len(v) == 2])
