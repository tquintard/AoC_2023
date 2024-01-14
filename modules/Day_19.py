from typing import List
from .parts_wf import Workflow as W, create_wf, sum_prop_accepted_part


def main(inputs: List[str]) -> List[str]:
    # create a dict of Workflows
    wf_list = inputs[0].splitlines()
    wfs = create_wf(wf_list)
    # create a list of parts
    parts_list = inputs[1].splitlines()
    sol1 = 0
    for part in parts_list:
        sol1 += sum_prop_accepted_part(part, wfs)

    # init the range when first entering to wf 'in'
    wfs['in'].range = {prop: [1, 4000] for prop in 'xmas'}
    # define all the possibile workflow
    wfs['in'].check_wf(wfs)
    sol2 = W.nb_accepted
    return sol1, sol2
