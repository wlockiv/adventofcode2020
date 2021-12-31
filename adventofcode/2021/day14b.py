from typing import IO, List
from adventofcode.util import print_solution
from collections import defaultdict
from .day14a import find_counts


def main(input_file: IO):
    input_lines: List[str] = input_file.read().splitlines()
    solution = find_counts(input_lines, 40)

    print_solution(str(solution))
