from typing import List
from .common import create_grid
from .hike import create_nodes, creat_graph, max_weight


def main(grid: List[str]) -> List[str]:
    grid = create_grid(grid)
    dimx, dimy = len(grid[0]), len(grid)
    start, end = (1, 0), (dimx - 2, dimy - 1)
    nodes = create_nodes(grid, start, end)
    sol = list()
    for part in (1, 2):
        graph = creat_graph(nodes, part)
        sol.append(max_weight(graph, start, end) - 1)

    return sol
