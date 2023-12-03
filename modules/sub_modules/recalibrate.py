import re
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
