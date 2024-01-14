from typing import List
from .common import lcm
from .modules_com import Modules as M, last_flipflops
from operator import mul
from itertools import count


def main(inputs: List[str]) -> List[str]:
    M.create_modules(inputs)
    last_ff, cycle_rep = last_flipflops(M.all_modules), list()
    for cycle in count(1):
        bdcaster = M.all_modules['broadcaster']
        M.pulses[0] += 1
        M.queue = [(bdcaster, output, 0) for output in bdcaster.outputs]
        while M.queue:
            src, dest, sig = M.queue.pop(0)
            if src in last_ff and sig == 1:
                last_ff.remove(src), cycle_rep.append(cycle)
            M.process_sig(src, dest, sig)
        if cycle == 1000:
            sol1 = mul(*M.pulses)
        if not last_ff:
            return sol1, lcm(*cycle_rep)
