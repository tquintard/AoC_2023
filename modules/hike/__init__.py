import networkx as nx
from collections import defaultdict


DIR = {0: (1, 0, '>'), 90: (0, -1, '^'), 180: (-1, 0, '<'), 270: (0, 1, 'v')}


def move_tile(grid, x, y, orient, dO) -> tuple:
    orient_ = (orient + dO) % 360
    dx, dy, slope = DIR[orient_]
    x_, y_ = x + dx, y + dy
    node = grid[y_][x_]
    return x_, y_, orient_, node == slope, node == '.'


def max_weight(graph, source, target):
    weight_max = -float('inf')
    for path in nx.all_simple_paths(graph, source=source, target=target):
        weight = sum(graph[u][v]['weight']
                     for u, v in zip(path[:-1], path[1:]))
        weight_max = max(weight_max, weight)

    return weight_max


def creat_graph(nodes: dict, part: int):
    G = nx.DiGraph() if part == 1 else nx.Graph()
    for node, neighbors in nodes.items():
        for neighbor in neighbors:
            neighbor, distance = neighbor
            G.add_edge(node, neighbor, weight=distance)
    return G


def create_nodes(grid: list, start: tuple, end: tuple):
    queue = [(*start, 270)]
    nodes = defaultdict(list)
    while queue:
        node_actual = x, y, orient = queue.pop(0)
        distance, new_link = 1, False
        while not new_link:
            for dO in (0, -90, 90):
                x_, y_, orient_, is_slope, is_tile = move_tile(
                    grid, x, y, orient, dO)
                if is_slope:
                    distance += 1
                    if distance != 2:
                        new_link = True
                        dx, dy, _ = DIR[orient_]
                        x, y, orient = x_ + dx, y_ + dy, orient_
                        nodes[node_actual[:2]].append(((x, y), distance))
                        if (x, y) not in nodes.keys():
                            nodes[(x, y)] = list()
                            for dO in (0, -90, 90):
                                _, _, _, is_slope, _ = move_tile(
                                    grid, x, y, orient, dO)
                                if is_slope:
                                    queue.append((x, y, (orient + dO) % 360))
                    else:
                        x, y, orient = x_, y_, orient_
                    break
                elif is_tile:
                    distance += 1
                    x, y, orient = x_, y_, orient_
                    break
            if y == end[1]:
                nodes[node_actual[:2]].append((end, distance))
                break
    return nodes
