from typing import IO

from .day17a import evolve


def main(input_file: IO):
    raw_input = input_file.read().splitlines()
    grid = tuple(map(str.rstrip, raw_input))

    hypercube = set()

    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == '#':
                hypercube.add((x, y, 0, 0))

    for _ in range(6):
        hypercube = evolve(hypercube)

    total_alive = len(hypercube)
    print('The answer for Day 17 Part B :', total_alive)
