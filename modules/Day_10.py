from typing import List
from .pipe_maze import update_pos, update_dir, ray_cast_light, fill_grid_find_start


def main(grid: List[str]) -> List[str]:
    # Find the start location
    polygon = list()
    fl_grid = list()
    x_start, y_start = fill_grid_find_start(grid, fl_grid)
    # based on the inputs, start position is a 7 and the next move is to go south
    direction = 'S'  # force the move to go south
    pipe = '|'  # force the move to go south
    grid[y_start] = grid[y_start][:x_start] + '7' + grid[y_start][x_start + 1:]
    # go through the edge of polygone until back to start - Part 1
    nb_pipes = 0  # the start pos
    x_next, y_next = x_start, y_start
    while not ((x_next, y_next) == (x_start, y_start) and direction == 'E'):
        direction = update_dir(direction, pipe)
        pipe, x_next, y_next = update_pos(grid, x_next, y_next, direction)
        polygon.append((x_next, y_next))
        fl_grid[y_next][x_next] = True
        nb_pipes += 1
    # count number of tiles inside the polygone - Part 2
    count = 0
    len_rows = len(grid[0])
    for y in range(len(grid)):
        is_in = False
        last_vertex = ''
        for x in range(len_rows):
            symbol = grid[y][x]
            fl_pt = fl_grid[y][x]
            is_in, count, last_vertex = ray_cast_light(
                symbol, fl_pt, is_in, count, last_vertex)

    return (nb_pipes) // 2, count
