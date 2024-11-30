from typing import List
from ..common import reverse, is_power2


def convert_grid(map: List[str]) -> List[int]:
    for i, row in enumerate(map):
        row = ''.join(row).translate(str.maketrans('.#', '01'))
        map[i] = int(row, 2)
    return map


def find_mirror(map: List[int], orient: str = 'h', part: int = 1):
    for i in range(1, len(map)):
        left_map, right_map = reverse(map[:i]), map[i:]
        length = min(len(left_map), len(right_map))
        left_map, right_map = left_map[:length], right_map[:length]
        diff = [left ^ right
                for left, right in zip(left_map, right_map) if left != right]
        if left_map == right_map and part == 1 \
                or len(diff) == 1 and is_power2(sum(diff)) and part == 2:
            return i if orient == 'v' else 100*i
    return 0
