from typing import List
from .hailstones import out_of_bound, path_cross, lin_eq
import re
import numpy as np


def main(inputs: List[str]) -> List[str]:
    # Part 1
    stones, stones_char = list(), list()
    bounds = (200000000000000, 400000000000000)
    for data in inputs:
        px, py, pz, vx, vy, vz = map(int, re.findall(r'[-]?\d+', data))
        stones.append((px, py, pz, vx, vy, vz))
        # all trajectories will be under the form y(x) = a*x + b
        # with a = dy/dx = dy/dt * dt/dx = vy/vx
        if not any(out_of_bound(p, v, bounds) for p, v in ((px, vx), (py, vy))):
            # do not take into account the stones if it is out of bounds initially
            a = vy / vx
            b = py - a*px
            stones_char.append((a, b, px, vx))
    sol1 = 0

    for i, stoneA in enumerate(stones_char):
        for stoneB in stones_char[i+1:]:
            sol1 += 1 if path_cross(stoneA, stoneB, bounds) else 0

    # Part 2
    stone_ref = stones[0]
    coef_mat, const_mat = list(), list()
    for stone in stones[1:3]:
        coef_mat, const_mat = lin_eq(stone_ref, stone, coef_mat, const_mat)
    coef_mat = np.array(coef_mat)
    const_mat = np.array(const_mat)
    eq_sol = np.linalg.solve(coef_mat, const_mat)
    sol2 = int(sum([p for i, p in enumerate(eq_sol) if i % 2 == 0]))
    return sol1, sol2
