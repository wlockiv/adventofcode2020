from os import getcwd, path
import re
import inspect
from shutil import copy, copyfile


def print_solution(solution: str):
    """Prints the solution with a bumper. This should only be called from files named something similar to "day01a.py".

    Args:
        solution (str): Formatted string representation of the solution.
    """
    filename = inspect.stack()[1].filename
    print(
        f'The answer for Day {filename[-6:-4]} Part {filename[-4:-3].upper()} : ', solution)


def copy_template_file(year: int, day: int, part: str):
    """Copies the solution_template.py file into the specified year's solution folder, naming it according to the 
    challenge's day and part. This will silently fail if the solution file already exists.

    Args:
        year: 4-digit year (YYYY).
        day: Day the solution file is for (1-25).
        part: Day's part the solution file is for (a or b).
    """
    dst = f'./adventofcode/{year}/day{str(day).zfill(2)}{part}.py'

    if path.exists(dst):
        return dst

    return copyfile('./adventofcode/solution_template.py', dst)
