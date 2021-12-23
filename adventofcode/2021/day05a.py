from typing import IO
from collections import defaultdict


def main(input_file: IO):
    input_lines = input_file.readlines()
    point_pairs = [l.strip().split(' -> ') for l in input_lines]

    grid = defaultdict(int)
    for point_strings in point_pairs:
        x1, y1 = [int(x) for x in point_strings[0].split(',')]
        x2, y2 = [int(y) for y in point_strings[1].split(',')]

        dX, dY = x2 - x1, y2 - y1
        if dX != 0 and dY != 0:
            continue

        if dX:
            line_steps = range(*([x1, x2 + 1] if dX > 0 else [x2, x1 + 1]))
            for step in line_steps:
                grid[f'{step},{y1}'] = grid[f'{step},{y1}'] + 1
        elif dY:
            line_steps = range(*([y1, y2 + 1] if dY > 0 else [y2, y1 + 1]))
            for step in line_steps:
                grid[f'{x1},{step}'] = grid[f'{x1},{step}'] + 1

    safe_points = list(filter(lambda v: v >= 2, grid.values()))

    print('The answer for Day 05 Part A :', len(safe_points))
