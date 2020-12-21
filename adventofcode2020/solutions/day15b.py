from collections import defaultdict
from typing import IO
from .day15a import solve


def main(input_file: IO):
    raw_input = input_file.read()
    result = solve(raw_input, 30000000)

    print('The answer for Day 15 Part B :', result)
