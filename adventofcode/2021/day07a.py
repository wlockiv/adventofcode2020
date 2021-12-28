from typing import IO, List
from adventofcode.util import print_solution


def main(input_file: IO):
    input_lines: str = input_file.read()
    numbers = [int(i) for i in input_lines.split(',')]

    pos_counts = {pos: numbers.count(pos) for pos in numbers}

    least_fuel = 0
    for alignment in range(max(numbers)):
        fuel_needed = sum(
            [abs(p - alignment) * c for p, c in pos_counts.items()])

        if not least_fuel:
            least_fuel = fuel_needed
        elif least_fuel > fuel_needed:
            least_fuel = fuel_needed

    print_solution(str(least_fuel))
