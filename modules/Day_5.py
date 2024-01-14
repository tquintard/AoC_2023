from typing import Tuple, List
import re
from copy import deepcopy


def in_range(x, inf, sup): return inf <= x <= sup


def src_num(dest_num, start_src, start_dest):
    return dest_num + start_src - start_dest


def dest_num(src_num, start_src, start_dest):
    return src_num - start_src + start_dest


def rng_list(start_pt, rng):
    return [int(start_pt), int(start_pt) + int(rng) - 1]


def main(inputs: List[str]) -> Tuple[int]:

    # iterate until the seed-to-soil map
    pattern = r'(?: \n)?(\d+) (\d+) (\d+)\n?'
    for i, list_map in enumerate(inputs[-1:0:-1]):
        m = sorted(re.findall(pattern, list_map), key=lambda x: int(x[0]))
        if i == 0:
            # hypothese: la range optimale de location est celle entre 0 et le premier chiffre mappé avec humidity
            # de ce fait la rng optimal d'humidity est identique car non mappée avec location
            opt_rngs = [rng_list(0, m[0][0])]
        else:
            if m[0][0] != '0':
                m.insert(0, ("0", "0", str(int(m[0][0]))))
            temp_rng = list()
            for opt_rng in opt_rngs:
                start_op, end_op = opt_rng
                no_intersect = True
                for map_ in m:
                    rng = map_[2]
                    start_dest, end_dest = rng_list(map_[0], rng)
                    start_src, end_src = rng_list(map_[1], rng)
                    if end_dest < start_op or start_dest > end_op:
                        # if the destination range is outside the optimum range
                        # destination range remains unchanged for source range
                        # do nothing for the moment
                        pass

                    else:
                        no_intersect = False
                        if start_dest < start_op < end_dest <= end_op:
                            # if the destination range is intersecting the optimum range on the left
                            start_src = src_num(
                                start_op, start_src, start_dest)
                            temp_rng.append([start_src, end_src])
                        elif start_op <= start_dest < end_op < end_dest:
                            # if the destination range is intersecting the optimum range on the right
                            end_src = src_num(end_op, start_src, start_dest)
                            temp_rng.append([start_src, end_src])
                        elif start_op <= start_dest and end_dest <= end_op:
                            # if the destination range is a subset of optimum range
                            temp_rng.append([start_src, end_src])
                        elif start_dest <= start_op and end_op <= end_dest:
                            # if the optimum range is a subset of destination range
                            end_src = src_num(end_op, start_src, start_dest)
                            start_src = src_num(
                                start_op, start_src, start_dest)
                            temp_rng.append([start_src, end_src])
                            break
                if no_intersect:
                    # if entering this loop that means the dest range is in no opt range
                    # then append in temp rng the dest rng
                    # since destination range remains unchanged for source range
                    temp_rng.append([start_op, end_op])
            opt_rngs = deepcopy(temp_rng)
            # print(opt_rngs)

    # Part 1
    seeds = map(int, re.findall(r'\d+', inputs[0]))
    max_index = len(opt_rngs)
    seed_num_sol1 = 0
    for seed in seeds:
        for i, rng in enumerate(opt_rngs[:max_index]):
            if in_range(seed, rng[0], rng[1]):
                seed_num_sol1 = seed
                max_index = i

    # Part 2
    m = re.findall(r'(\d+) (\d+)', inputs[0])
    seed_num_sol2 = 0
    max_index = len(opt_rngs)
    for match in m:
        start_seed, end_seed = rng_list(match[0], match[1])
        for i, rng in enumerate(opt_rngs[:max_index]):
            start_op, end_op = rng
            if start_seed <= start_op <= end_seed:
                seed_num_sol2 = start_op
                max_index = i
            elif start_op <= start_seed <= end_op:
                seed_num_sol2 = start_seed
                max_index = i
    sol = []
    pattern = r'(?: \n)?(\d+) (\d+) (\d+)\n?'

    for seed_num in (seed_num_sol1, seed_num_sol2):
        corr_num = seed_num
        for list_maps in inputs[1:]:
            m = sorted(re.findall(pattern, list_maps), key=lambda x: int(x[1]))
            if m[0][1] != '0':
                m.insert(0, ("0", "0", str(int(m[0][1]))))
            for map_ in m:
                rng = map_[2]
                start_dest, end_dest = rng_list(map_[0], rng)
                start_src, end_src = rng_list(map_[1], rng)
                if in_range(corr_num, start_src, end_src):
                    corr_num = dest_num(corr_num, start_src, start_dest)
                    break
        sol.append(corr_num)

    return sol
