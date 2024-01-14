from typing import Tuple
DIR = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
PIPE = {'|': {'S': 'S', 'N': 'N'},
        '-': {'W': 'W', 'E': 'E'},
        'F': {'W': 'S', 'N': 'E'},
        'L': {'S': 'E', 'W': 'N'},
        'J': {'E': 'N', 'S': 'W'},
        '7': {'N': 'W', 'E': 'S'},
        }


def update_pos(grid: list, x: int, y: int, direction: str) -> Tuple[int]:
    x, y = x + DIR[direction][0], y + DIR[direction][1]
    return grid[y][x], x, y


def update_dir(direction: str, pipe: str) -> str:
    return PIPE[pipe][direction]


def ray_cast_light(symbol: str, fl_pt: bool, is_in: bool, count: int, last_vertex: str) -> tuple:
    if not fl_pt:
        if is_in:
            count += 1
    else:
        if symbol in '7' and last_vertex == 'F' \
                or symbol == 'J' and last_vertex == 'L' \
                or symbol in '|FL':
            last_vertex = symbol
            is_in = not is_in
    return is_in, count, last_vertex


def fill_grid_find_start(grid: list, fl_grid: list) -> list:

    for y, row in enumerate(grid):
        fl_grid.append([])
        for x, _ in enumerate(row):
            fl_grid[y].append(False)
            if grid[y][x] == 'S':
                x_start, y_start = x, y
    return x_start, y_start
