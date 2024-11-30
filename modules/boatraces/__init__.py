from math import sqrt
from typing import List
import re


def solvequad(a: float = 0, b: float = 0, c: float = 0) -> float:
    delta = b**2 - 4*a*c
    if delta < 0:
        return None
    elif delta == 0:
        return (-b/(2*a))
    else:
        return (-b+sqrt(delta))/(2*a), (-b-sqrt(delta))/(2*a)


def get_races_data(inputs: List[str], part: int) -> float:
    if part == 1:
        pattern = r'\b\d+\b'
    else:
        inputs = inputs.replace(" ", "")
        pattern = r'\d+'
    return list(map(int, re.findall(pattern, inputs)))
