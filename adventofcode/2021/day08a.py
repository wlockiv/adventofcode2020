from typing import IO, List
from adventofcode.util import print_solution


def main(input_file: IO):
    input_lines: List[str] = input_file.readlines()

    count = 0
    for i in input_lines:
        output = i.split(' | ')[1].strip().split(" ")
        # Find 1, 4, 7, and 8: 1 = 2, 4 = 4, 7 = 3, 8 = 7
        output = [o for o in output if len(o) in [2, 4, 3, 7]]
        count = count + len(output)

    print_solution(str(count))
