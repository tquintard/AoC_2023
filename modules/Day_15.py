from typing import List
from .hash import hash
from collections import defaultdict


def main(steps: List[str]) -> List[str]:
    sol1, sol2 = 0, 0
    boxes = defaultdict(dict)
    for step in steps:
        # Part 1
        sol1 += hash(step)
        # Part 2
        if step[-1] == '-':
            try:
                label = step[:-1]
                del boxes[hash(label)][label]
            except KeyError:
                pass
        else:
            label, focal = step.split('=')
            boxes[hash(label)][label] = int(focal)
    for box, labels in boxes.items():
        for i, focal in enumerate(labels.values(), start=1):
            sol2 += (box + 1) * i*focal
            i += 1
    return sol1, sol2
