from typing import List
from .tilt import tilt, load_beam, cycle, find_rep, create_set_rocks


def main(inputs: List[str]) -> List[str]:
    # Create set for rounded rocks and cube rocks
    dim_x, dim_y = len(inputs[0]) + 1, len(inputs) + 1
    rounds, cubes = create_set_rocks(inputs, dim_x, dim_y)

    # Part 1
    rounds_ = tilt(rounds, cubes, 'N')
    sol1 = load_beam(rounds_)[1]
    # Part 2
    loads = list()
    while True:
        rounds = cycle(rounds, cubes)
        load = load_beam(rounds)
        if load in loads:
            sol2 = find_rep(load, loads)
            break
        loads.append(load)
    return sol1, sol2
