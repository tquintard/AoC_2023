from typing import List
from .expansion import distance, add_offset, find_galaxies
from collections import defaultdict


def main(grid: List[str]) -> List[str]:
    galaxies = defaultdict(list)

    # First browse the grid to define the offset_y of each galaxy
    galaxies = find_galaxies(grid, galaxies, False)
    # Then browse the grid to define the offset_x of each galaxy
    grid = list(map(list, zip(*grid)))
    galaxies = find_galaxies(grid, galaxies, True)

    # Then calculate the distance between each galaxy
    sol = list()
    for part in (1, 2):
        factor = 1 if part == 1 else 999999
        d = 0
        list_gal = tuple(add_offset(point, offsets, factor)
                         for point, offsets in galaxies.items())

        for i, galaxy in enumerate(list_gal[:-1]):
            for next_gal in list_gal[i:]:
                d += distance(galaxy, next_gal)
        sol.append(d)

    return sol
