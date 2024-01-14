import operator as op
from re import findall as fa
from typing import List
from copy import deepcopy

OPERATORS = {'<': op.lt, '>': op.gt}


class Workflow:
    nb_accepted = 0

    def __init__(self, name: str, conditions: str = ''):
        self.name = name
        self.range = None
        if conditions:
            self.rules = dict()
            conditions = conditions.split(',')
            for i, condition in enumerate(conditions[:-1]):
                c = condition.split(':')
                self.rules[c[0][0] +
                           str(i)] = (OPERATORS[c[0][1]], int(c[0][2:]), c[1])
            # add a last rules if none of the previous has been validated, condition is if x > 0 then ...
            self.rules[f'x{i+1}'] = (OPERATORS['>'], 0, conditions[-1])

    def pass_wf(self, part: dict, wfs: dict) -> int:
        for prop, cond in self.rules.items():
            ope, value, next_wf, prop = *cond, prop[0]
            if ope(part[prop], value):
                if next_wf == 'A':
                    # return 1
                    return sum([value for value in part.values()])
                elif next_wf == 'R':
                    return 0
                else:
                    return wfs[next_wf].pass_wf(part, wfs)

    def check_wf(self, wfs: dict) -> None:
        actual_range = deepcopy(self.range)
        for prop, cond in self.rules.items():
            ope, value, next_wf, prop = *cond, prop[0]
            # change range of next wf
            wfs[next_wf].range = deepcopy(actual_range)
            if ope == op.lt:
                wfs[next_wf].range[prop][1] = value - 1
                actual_range[prop][0] = value
            else:
                if value != 0:
                    wfs[next_wf].range[prop][0] = value + 1
                    actual_range[prop][1] = value
            # if next wf is A then compute the number of possibilities based on the range
            if next_wf == 'A':
                prod = 1
                for r in wfs['A'].range.values():
                    prod *= (r[1] - r[0] + 1)
                Workflow.nb_accepted += prod
            elif next_wf != 'R':
                wfs[next_wf].check_wf(wfs)


def create_wf(wf_list: List[str]):
    wfs = dict()
    for wf in wf_list:
        m = fa(r'(\w+){(.+)}', wf)
        wfs[m[0][0]] = Workflow(m[0][0], m[0][1])
    wfs['A'] = Workflow('A')
    wfs['R'] = Workflow('R')
    return wfs


def sum_prop_accepted_part(part: str, wfs: dict) -> int:
    m = fa(r'(\d+)', part)
    part = {'xmas'[i]: int(value)
            for i, value in enumerate(m)}
    return wfs['in'].pass_wf(part, wfs)
