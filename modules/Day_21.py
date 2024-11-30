from typing import List
# from time import time
# from common import *
# from garden_plot import *


def main(grid: List[str]) -> List[str]:
    #     rocks = set()
    #     dim_x, dim_y = len(grid[0]), len(grid)
    #     for y, row in enumerate(grid):
    #         for x, col in enumerate(row):
    #             if col == '#':
    #                 rocks.add((x, y))
    #             elif col == 'S':
    #                 start_pos = (x, y)
    #                 actual_pos = {start_pos, }

    #     # Part 1 solution
    #     for _ in range(64):
    #         next_pos = set()
    #         for pos in actual_pos:
    #             next_pos.update(get_neighbors(pos, dim_x, dim_y))
    #         actual_pos = next_pos - rocks
    #     sol1 = len(actual_pos)

    #     # Part 2 solution
    #     for x in range(11):
    #         actual_pos = {(0, x), }
    #         len_history = [0, 0, len(actual_pos)]
    #         while len_history[-3] != len_history[-1]:
    #             next_pos = set()
    #             for pos in actual_pos:
    #                 next_pos.update(get_neighbors(pos, dim_x, dim_y))
    #             actual_pos = next_pos - rocks
    #             len_history.append(len(actual_pos))
    #         print(len_history[-1], len_history[-2])
    #         rep = len(len_history) - 2

    #     # old_lap = len(actual_pos)
    #     # lnp = len(next_pos)
    #     # lr = len(rocks)
    #     # actual_pos = next_pos - rocks
    #     # sol2 = len(actual_pos)
    #     # print_log(logger, f'Old pos: {old_lap}')
    #     # print_log(logger, f'New pos: {sol2}')
    #     # print_log(logger, f'New pos: {sol2}')
    #     # print_log(logger, (sol2, old_lap, lnp, lr, sol2  % lr, sol2 % lnp))
    #     # print_log(logger, (sol2, old_lap, lnp, lr, sol2  % lr, sol2 % lnp))
    #     # print_log(logger, (sol2, old_lap, lnp, lr, sol2  % lr, sol2 % lnp))
    #     # print_log(logger, '--------------------------')
    #     # for pos in actual_pos:
    #     #     if pos[0] == dim_x[0]:
    #     #         rocks, dim_x, dim_y = translate_rock(
    #     #             'x', -1, rocks, dim_x, dim_y)
    #     #     if pos[0] == dim_x[1] - 1:
    #     #         rocks, dim_x, dim_y = translate_rock(
    #     #             'x', 1, rocks, dim_x, dim_y)
    #     #     if pos[1] == dim_y[0]:
    #     #         rocks, dim_x, dim_y = translate_rock(
    #     #             'y', -1, rocks, dim_x, dim_y)
    #     #     if pos[1] == dim_y[1] - 1:
    #     #         rocks, dim_x, dim_y = translate_rock(
    #     #             'y', 1, rocks, dim_x, dim_y)

    #     # sol2 = len(actual_pos)
    return 'Not yet solved', 'Not yet solved'


# start = time()
# inputs = get_input(21, '\n', True)
# print(main(inputs))
# print(f'Time: {int((time()-start)*1000)}')
