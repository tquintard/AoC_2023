from math import gcd
from functools import reduce


def lcm(a, b):
    return a * b // gcd(a, b)


def find_lcm(next_nodes: dict, nodes: dict, all_steps: list, instructions: str) -> int:
    for next in next_nodes:
        steps = 0
        while next[-1] != 'Z':
            for instr in instructions:
                next = nodes[next][int(instr)]
                steps += 1
                if next[-1] == 'Z':
                    all_steps.append(steps)
                    break
    return reduce(lcm, all_steps)
