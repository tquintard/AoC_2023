from typing import List
from .dig_site import build_polygone, polygon_area


def main(dig_plan: List[str]) -> List[str]:
    sol = list()
    for part in (1, 2):
        vertices, perim = build_polygone(dig_plan, part)
        aera = polygon_area(vertices)
        sol.append(aera + perim // 2 + 1)

    return sol
