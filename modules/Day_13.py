from typing import List
from .common import transpose
from .mirrors import find_mirror, convert_grid


def main(mirrors_valley: List[str]) -> tuple:
    sol = [0, 0]

    for mirrors_map in mirrors_valley:

        mirrors_map = [list(row) for row in mirrors_map.splitlines()]
        transposed_map = convert_grid(transpose(mirrors_map))
        mirrors_map = convert_grid(mirrors_map)
        for part in (1, 2):
            sol[part - 1] += find_mirror(mirrors_map, part=part) + \
                find_mirror(transposed_map, 'v', part)

    return sol
