from typing import List
from .bricks import Bricks as B


def main(inputs: List[str]) -> List[str]:
    B.bricks = [B(line) for line in inputs]
    B.bricks_fall()
    return B.desintegrate(), B.chain_reaction()
