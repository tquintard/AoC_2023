from typing import Tuple
from ..common import reverse

DIRECTION = {'N': (0, 1, lambda x: x[1], True),
             'W': (-1, 0, lambda x: x[0], False),
             'S': (0, -1, lambda x: x[1], False),
             'E': (1, 0, lambda x: x[0], True)}


def create_set_rocks(inputs: list, dim_x: int, dim_y: int) -> Tuple[set]:
    rounds, cubes = set(), set()
    for i in range(dim_y + 1):
        if i in (0, dim_y):
            for j in range(dim_x + 1):
                cubes.add((j, i))
        else:
            cubes.add((0, i))
            cubes.add((dim_x, i))

    for i, line in enumerate(reverse(inputs), 1):
        for j, col in enumerate(line, 1):
            if col == 'O':
                rounds.add((j, i))
            elif col == '#':
                cubes.add((j, i))
    return rounds, cubes


def tilt(rounds: set, cubes: set, direct: str) -> set:
    temp = cubes - set()
    dx, dy, sort_fct, sort_dir = DIRECTION[direct]
    _rounds = sorted(rounds, key=sort_fct, reverse=sort_dir)
    for r_rock in _rounds:
        while True:
            r_rock = (r_rock[0] + dx, r_rock[1] + dy)
            if {r_rock}.issubset(temp):
                temp.add((r_rock[0] - dx, r_rock[1] - dy))
                break
    temp -= cubes
    return temp


def cycle(rounds: set, cubes: set) -> set:
    for direct in DIRECTION.keys():
        rounds = tilt(rounds, cubes, direct)
    return rounds


def load_beam(rounds: set) -> int:
    h_loads, v_loads = zip(*rounds)
    return sum(h_loads), sum(v_loads)


def find_rep(load: tuple, loads: list) -> int:
    idx = loads.index(load)
    init, rep = loads[:idx], loads[idx:]
    rem_rep = int(1e9 - len(init)) % len(rep) - 1
    return rep[rem_rep][1]
