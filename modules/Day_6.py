from typing import List, Tuple
from .boatraces import solvequad, get_races_data


def main(inputs: List[str]) -> Tuple[int]:
    sol = []
    for part in (1, 2):
        races_data = get_races_data(inputs, part)
        nb_races = len(races_data)//2
        # f(t_hold) = t_hold * (time - t_hold) = -t_hold² + time* t_hold
        # target is to find -t_hold² + time* t_hold = dist
        # ==> -1*t_hold² + time*t_hold - dist = 0
        # assumption: delta of this 2nd degree equation is > 0
        # solution to this equation is x = (-b +/- sqr(delta))/2a
        nb_ways = 1
        for i in range(1, nb_races + 1):
            time, dist = races_data[i - 1], races_data[i + nb_races - 1]
            x1, x2 = solvequad(a=-1, b=time, c=-dist)
            nb_ways *= int(x2 - x1)
        sol.append(nb_ways)
    return sol
