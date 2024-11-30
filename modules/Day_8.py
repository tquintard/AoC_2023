from typing import List
from .wasteland import find_lcm

import re


def main(inputs: List[str]) -> List[str]:
    instructions = inputs[0].translate(str.maketrans('LR', '01'))
    pattern = r'(\b\w{3}\b).*(\b\w{3}\b).*(\b\w{3}\b)'
    nodes = {nodes[0]: (nodes[1], nodes[2]) for line in inputs[2:]
             for nodes in re.findall(pattern, line)}
    sol = list()
    all_steps = list()
    next_nodes = ['AAA']
    for part in (1, 2):
        if part == 2:
            next_nodes += [key for key in nodes.keys()
                           if key[-1] == 'A' and key != 'AAA']
        sol.append(find_lcm(next_nodes, nodes, all_steps, instructions))

    return sol
