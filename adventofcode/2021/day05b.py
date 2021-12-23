from typing import IO
from collections import defaultdict


def main(input_file: IO):
    input_lines = input_file.readlines()
    point_pairs = [l.strip().split(' -> ') for l in input_lines]

    grid = defaultdict(int)
    for idx, point_strings in enumerate(point_pairs):
        x1, y1 = [int(x) for x in point_strings[0].split(',')]
        x2, y2 = [int(y) for y in point_strings[1].split(',')]

        dX, dY = x2 - x1, y2 - y1

        x_steps = list(range(
            x1,
            (x2 + 1) if dX > 0 else (x2 - 1),
            1 if dX > 0 else -1
        )) if dX else [x1] * (abs(dY) + 1)

        y_steps = list(range(
            y1,
            (y2 + 1) if dY > 0 else (y2 - 1),
            1 if dY > 0 else -1
        )) if dY else [y1] * (abs(dX) + 1)

        points = zip(x_steps, y_steps)

        for x, y in points:
            grid[f'{x},{y}'] = grid[f'{x},{y}'] + 1

    safe_points = list(filter(lambda v: v >= 2, grid.values()))

    print('The answer for Day 05 Part B :', len(safe_points))
