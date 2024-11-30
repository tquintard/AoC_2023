from typing import List
import re

DIRECTION = {'R': lambda x, y, incr: (x + incr, y),
             'L': lambda x, y, incr: (x - incr, y),
             'D': lambda x, y, incr: (x, y + incr),
             'U': lambda x, y, incr: (x, y - incr), }


def build_polygone(dig_plan: List[str], part: int = 1) -> tuple:
    pattern = r'(R|L|D|U)\s(\d+)' if part == 1 else r'(\w{5})(\d{1})'
    nb_edges = 0
    x, y = 0, 0
    vertices = list()
    for instr in dig_plan:
        m = re.findall(pattern, instr)
        if part == 1:
            direct, incr = m[0][0], int(m[0][1])
        else:
            incr = int(m[0][0], 16)
            direct = m[0][1].translate(str.maketrans('0123', 'RDLU'))
        nb_edges += incr
        x, y = DIRECTION[direct](x, y, incr)
        vertices.append((x, y))
    return vertices, nb_edges


def polygon_area(v):
    n = len(v)
    area = 0

    # Calculate the area using the Shoelace formula
    for i in range(n):
        j = (i + 1) % n
        area += v[i][0] * v[j][1] - v[j][0] * v[i][1]

    return area // 2
