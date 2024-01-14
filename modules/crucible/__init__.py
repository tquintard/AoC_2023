from heapq import heappop as get, heappush as put


def is_valid(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def min_heat(grid: list, min_fwd: int, max_fwd: int):
    rows, cols = len(grid), len(grid[0])
    seen = set()
    queue = [(0, 0, 0, 0, 0)]

    while queue:

        heat, x, y, px, py = get(queue)
        if (x, y) == (cols - 1, rows - 1):
            return heat
        if (x, y, px, py) in seen:
            continue
        seen.add((x, y, px, py))

        for dx, dy in {(1, 0), (0, 1), (-1, 0), (0, -1)}-{(px, py), (-px, -py)}:
            new_x, new_y, new_heat = x, y, heat
            for i in range(1, max_fwd + 1):
                new_x, new_y = new_x + dx, new_y + dy
                if is_valid(new_x, new_y, grid):
                    new_heat += grid[new_y][new_x]
                    if i >= min_fwd:
                        put(queue, (new_heat, new_x, new_y, dx, dy))
