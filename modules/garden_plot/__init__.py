def translate_rock(axe: str, direction: int, rocks: set, dim_x: tuple, dim_y: tuple) -> set:
    new_rocks = set()
    off_x = dim_x[1] - dim_x[0]
    off_y = dim_y[1] - dim_y[0]

    if axe == 'x':
        for rock in rocks:
            new_rocks.add((rock[0] + direction*off_x, rock[1]))
        dim_x = (dim_x[0] - off_x, dim_x[1]) if direction == -1 \
            else (dim_x[0], dim_x[1] + off_x)
    else:
        for rock in rocks:
            new_rocks.add((rock[0], rock[1] + direction*off_y))
        dim_y = (dim_y[0] - off_y, dim_y[1]) if direction == -1 \
            else (dim_y[0], dim_y[1] + off_y)
    rocks.update(new_rocks)
    return rocks, dim_x, dim_y


MOV = ((1, 0), (-1, 0), (0, 1), (0, -1))


def get_neighbors(node: tuple, dim_x: tuple, dim_y: tuple, part: int = 1) -> tuple:
    neighbors = tuple()
    col, row = node

    # Check all possible movements
    for dx, dy in MOV:
        new_row, new_col = row + dx, col + dy

        # Check if the new position is within the grid boundaries
        if part == 1:
            if 0 <= new_row < dim_y and 0 <= new_col < dim_x:
                neighbors += ((new_col, new_row),)
        else:
            neighbors += ((new_col, new_row),)

    return neighbors
