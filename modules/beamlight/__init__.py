# dict that gives the dx,dy and next orientation based on the actual node element
NODE = {'.': {0: ((1, 0, 0),), 90: ((0, -1, 90),), 180: ((-1, 0, 180),), 270: ((0, 1, 270),)},
        '/': {0: ((0, -1, 90),), 90: ((1, 0, 0),), 180: ((0, 1, 270),), 270: ((-1, 0, 180),)},
        '\\': {0: ((0, 1, 270),), 90: ((-1, 0, 180),), 180: ((0, -1, 90),), 270: ((1, 0, 0),)},
        '-': {0: ((1, 0, 0),), 90: ((-1, 0, 180), (1, 0, 0)), 180: ((-1, 0, 180),), 270: ((-1, 0, 180), (1, 0, 0))},
        '|': {0: ((0, -1, 90), (0, 1, 270)), 90: ((0, -1, 90),), 180: ((0, -1, 90), (0, 1, 270)), 270: ((0, 1, 270),)}}


def vis_nodes(x: int, y: int, orient: int, seen: set, visited: set) -> tuple:
    seen.add((x, y, orient))
    visited.add((x, y))
    return seen, visited


def in_bound(x: int, y: int, dimx: int, dimy: int) -> bool:
    return 0 <= x < dimx and 0 <= y < dimy


def find_visited(grid: list, queue: list, dimx: int, dimy: int) -> list:
    seen, visited = set(), set()
    while queue:
        x, y, orient = queue.pop(0)
        node = grid[y][x]
        seen, visited = vis_nodes(x, y, orient, seen, visited)
        node_datas = NODE[node][orient]
        for data in node_datas:
            dx, dy, orient = data
            next_x, next_y = x+dx, y+dy
            if in_bound(next_x, next_y, dimx, dimy) and (next_x, next_y, orient) not in seen:
                queue.append((next_x, next_y, orient))
    return len(visited)


def edge(dimx: int, dimy: int) -> list:

    edge_nodes = list()
    for y in range(dimy):
        for x in range(dimx):
            if x in (0, dimx - 1):
                edge_nodes.append((x, y, x*180//(dimx - 1)))
            elif y in (0, dimy - 1):
                edge_nodes.append((x, y, 270-y*180//(dimy - 1)))
    return edge_nodes
