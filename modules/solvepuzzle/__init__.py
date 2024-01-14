from modules import Day_1, Day_2, Day_3, Day_4, Day_5, Day_6, Day_7, Day_8, Day_9, Day_10, Day_11, Day_12, Day_13, Day_14, Day_15, Day_16, Day_17, Day_18, Day_19, Day_20, Day_21, Day_22, Day_23, Day_24, Day_25
from modules.common import get_input
from typing import List

DAY_MODULES = {'1': (Day_1, '\n'), '2': (Day_2, '\n'), '3': (Day_3, '\n'), '4': (Day_4, '\n'), '5': (Day_5, '\n\n'),
               '6': (Day_6, ''), '7': (Day_7, ''), '8': (Day_8, '\n'), '9': (Day_9, '\n'), '10': (Day_10, '\n'),
               '11': (Day_11, '\n'), '12': (Day_12, ''), '13': (Day_13, '\n\n'), '14': (Day_14, '\n'), '15': (Day_15, ','),
               '16': (Day_16, '\n'), '17': (Day_17, '\n'), '18': (Day_18, '\n'), '19': (Day_19, '\n\n'), '20': (Day_20, '\n'),
               '21': (Day_21, ''), '22': (Day_22, '\n'), '23': (Day_23, '\n'), '24': (Day_24, '\n'), '25': (Day_25, '\n'),
               }


def solvepuzzle(day: int) -> List[int]:
    # Fetch input data
    module, separator = DAY_MODULES[day]
    inputs = get_input(day=day, separator=separator)
    return module.main(inputs)
