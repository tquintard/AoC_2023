from os.path import dirname, join
from typing import List


def get_input(day: int, separator: str = '\n', sample: bool = False) -> List[str]:
    """
    Read input data from a file for a given day of Advent of Code.

    Args:
    - day (int): The day for which input data is required.
    - separator (str, optional): The separator used to split lines in the file. Defaults to newline.

    Returns:
    - List[str]: A list containing lines from the input file.
    """

    # Construct the file path based on the day
    input_file_path = join(
        dirname(__file__), f'../../../input{"/sample" if sample else ""}/Day_{day}.txt')

    # Open the input file and read its contents
    with open(input_file_path, 'r') as file:
        # Read the file content, strip any trailing spaces or newlines, and split lines based on the separator
        content = file.read().rstrip().split(separator)
        return content
