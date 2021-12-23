from typing import IO, List

from adventofcode.util import print_solution
from .day06a import be_fruitful


def main(input_file: IO):
    input_lines: List[str] = input_file.readlines()
    timers: List[str] = [i for i in input_lines[0].split(',')]

    population = be_fruitful(timers, 256)

    print_solution(str(population))
