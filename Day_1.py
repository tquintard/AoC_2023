import sys
import re
from functools import partial
from get_aoc import get_input

# Constants for better readability and maintainability
NUMBERS_IN_LETTERS = ['zero', 'one', 'two', 'three',
                      'four', 'five', 'six', 'seven', 'eight', 'nine']


def recalibrate_line(line: str, part: int) -> int:
    """
    Recalibrates the line value based on the specified part of the puzzle.

    Args:
    - line: The input line to be recalibrated.
    - part: The puzzle part number for the recalibration.

    Returns:
    - The recalibrated integer value.
    """
    if part == 2:
        # Replace words with their corresponding digits in the line,
        # surrounded by first and last letter of number word
        for i, num_word in enumerate(NUMBERS_IN_LETTERS):
            line = line.replace(num_word, num_word[0] + str(i) + num_word[-1])

    # Extract all digits from the line using regex
    matches = re.findall(r'(\d)', line)

    # Return the recalibrated value of the line,
    # taking only first and last digit found by the regex
    return int(matches[0] + matches[-1])


def main():
    # Fetch input data
    lines = get_input(day=2, sample=False)

    # Iterate through each part of the day's puzzle for recalibration of values
    for part_num in [1, 2]:
        # Calculate the solution for the current part
        sol = sum(map(partial(recalibrate_line, part=part_num), lines))

        # Print the solution for the current part
        print(f'Solution for part {part_num} is {sol}')


if __name__ == '__main__':
    sys.exit(main())
