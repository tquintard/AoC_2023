import re
from typing import Set, Tuple
from collections import defaultdict


def get_partnumber(line_idx: int, line: str, part_numbers: dict) -> Set[Tuple[int]]:
    matches = re.finditer(r'\d+', line)
    for match in matches:
        start, end = match.start(), match.end()
        part_numbers[(int(match.group()), (line_idx, start))] = [(line_idx, col)
                                                                 for col in range(start, end)]


def get_symbols(line_idx: int, line: str, symbols: dict) -> Set[Tuple[int]]:
    matches = re.finditer(r'[^\d.]', line)
    for match in matches:
        position = match.start()
        symbols[(match.group(), (line_idx, position))] = list()
        for row in range(-1, 2):
            for col in range(-1, 2):
                symbols[(match.group(), (line_idx, position))].append(
                    (line_idx + row, position + col))


def sum_pn_or_gr(part_numbers: dict, symbols: dict, part: int) -> int:
    symbols_vicinity = set()
    for key, sub_set in symbols.items():
        for value in sub_set:
            if part == 1 or key[0] == '*':
                symbols_vicinity.add(value)

    gears = defaultdict(list)
    for key, value in list(part_numbers.items()):
        for pos in list(value):
            if pos not in symbols_vicinity:
                value.remove(pos)
            else:
                if part == 2:
                    # find which * is in the vicinity of the number
                    for position, viscinity_pos in list(symbols.items()):
                        if pos in viscinity_pos:
                            gears[position].append(int(key[0]))
                            # Delete a * position if there are more than 2 adjacents part number to optimise the research
                            if len(gears[position]) > 2:
                                del symbols[position]
                    break
        if len(value) == 0:
            del part_numbers[key]

    if part == 1:
        return sum([k[0] for k in part_numbers.keys()])
    else:
        return sum([v[0]*v[1] for v in gears.values() if len(v) == 2])
