from itertools import product
from typing import IO


def neighbors(coords):
    ranges = ((c - 1, c, c + 1) for c in coords)
    yield from product(*ranges)


def alive_neighbors(cube, coords):
    alive = sum(p in cube for p in neighbors(coords))
    alive -= coords in cube
    return alive


def all_neighbors(cube):
    return set(n for p in cube for n in neighbors(p))


def evolve(cube):
    new = set()

    for p in all_neighbors(cube):
        alive = alive_neighbors(cube, p)

        if p in cube:
            # The point is alive
            if alive == 2 or alive == 3:
                new.add(p)
        elif alive == 3:
            # The point is not alive
            new.add(p)

    return new


def main(input_file: IO):
    raw_input = input_file.read().splitlines()

    grid = tuple(map(str.rstrip, raw_input))
    h, w = len(grid), len(grid[0])
    cube = set((x, y, 0) for x, y in product(range(h), range(w)) if grid[x][y] == '#')

    for _ in range(6):
        cube = evolve(cube)

    total_alive = len(cube)
    print('The answer for Day 17 Part A :', total_alive)
