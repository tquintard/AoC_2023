import sys
import re
from functools import partial
from get_aoc import get_input

# Regular expressions and their associated color maximums
COLORS = {'red': 12, 'green': 13, 'blue': 14, }


def max_cubes_in_game(line: str, color: str) -> int:
    """
    Calculates the maximum number of cubes per game and per color.

    Args:
    - line (str): A line containing game information about set of cubes and colors.
    - color (str): Specifies the color for which the maximum of cubes is calculated.

    Returns:
    - int: The maximum number of cubes per game and per color.
    """
    # Extract the number of cubes per set for a specific color
    cubes_per_set = re.findall(r"(\d+) " + color, line)
    # Extract the maximum count of cubes for a specific color
    return max(map(int, cubes_per_set))


def games(line: str, part: int) -> int:
    """
    Calculates game IDs or powers based on cube colors for a given game.

    Args:
    - line (str): A line containing information about set cubes and colors.
    - part (int): Specifies whether to calculate game IDs (part 1) or game power (part 2).

    Returns:
    - int: The game ID or the game power calculated based on number of cube colors per set.
    """
    # Extract the game ID from the line
    game_id = int(re.search(r"Game (\d+):", line).group(1))
    # Initialise the game power
    game_power = 1

    # Iterate through each color
    for color, max_value in COLORS.items():
        max_color_cubes = max_cubes_in_game(line, color)
        # Return different value based on the day's puzzle part
        if part == 1:
            # If one of the set have more cubes than the authorized maximum cube then return 0
            if max_color_cubes > max_value:
                return 0
        else:
            # Calculate game power based on the maximum count of cubes for each color
            game_power *= max_color_cubes
    # For part 1, returns the game id if all colors on all sets have less than the authorized maximun cube
    # For part 2, returns the game power
    return game_id if part == 1 else game_power


def main():
    # Fetch input data
    lines = get_input(day=2, sample=False)

    # Iterate through each part of the day's puzzle
    for part_num in [1, 2]:
        # Calculate the solution for the current part
        sol = sum(map(partial(games, part=part_num), lines))

        # Print the solution for the current part
        print(f'Solution for part {part_num} is {sol}')


if __name__ == '__main__':
    sys.exit(main())
