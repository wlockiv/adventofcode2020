from typing import IO, List
from adventofcode.util import print_solution
from .day11a import Grid, flash


def main(input_file: IO):
    input_lines: List[str] = input_file.read().splitlines()

    grid: Grid = {}
    for y, row in enumerate(input_lines):
        for x, num in enumerate(row):
            grid[(x, y)] = int(num)

    target_flashes = len(input_lines) * len(input_lines[0])

    step = 0
    while True:
        for point in grid:
            grid[point] += 1

        if flash(grid) == target_flashes:
            break

        step += 1

    print_solution(str(step + 1))
