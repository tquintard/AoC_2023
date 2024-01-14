from typing import List
from .beamlight import edge, find_visited

# Peut etre ameliorer en utilisant des link lists


def main(grid: List[str]) -> List[str]:
    dimx, dimy = len(grid[0]), len(grid)
    edge_nodes = edge(dimx, dimy)
    for i, node in enumerate(edge_nodes):
        edge_nodes[i] = find_visited(grid, [node], dimx, dimy)
    return edge_nodes[0], max(edge_nodes)
