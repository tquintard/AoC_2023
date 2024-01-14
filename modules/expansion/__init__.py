from typing import List
from collections import defaultdict


def distance(pos_x: List[int], pos_y: List[int]) -> int:
    return abs(pos_y[0] - pos_x[0]) + abs(pos_y[1] - pos_x[1])


def add_offset(pos: list, offsets: list, factor: int) -> tuple:
    return pos[0] + offsets[0]*factor, pos[1] + offsets[1]*factor


def find_galaxies(grid: list, galaxies: dict, transpose: bool) -> dict:
    offset = 0
    len_row = len(grid[0])
    nb_rows = len(grid)
    for y in range(len_row):
        is_empty = True
        for x in range(nb_rows):
            if grid[y][x] == '#':
                # it's a galaxy
                galaxies[(x, y) if transpose else (y, x)].append(offset)
                is_empty = False
        if is_empty:
            # it's an empty row -> increment offset
            offset += 1
    return galaxies
