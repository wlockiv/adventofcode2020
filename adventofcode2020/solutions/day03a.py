import math
from typing import IO, List


def get_tree_hits(dy: int, dx: int, field_input_rows: List[str]):
    field_height = len(field_input_rows)
    total_steps = math.ceil(field_height / dy)
    field_repeats = math.ceil((total_steps * dx) / len(field_input_rows[0]))

    for idx in range(len(field_input_rows)):
        field_input_rows[idx] = field_input_rows[idx] * field_repeats

    trees_hit = 0

    for step in range(total_steps):
        x, y = (step * dx, step * dy)
        if field_input_rows[y][x] == '#':
            trees_hit += 1

    return trees_hit


def main(input_file: IO):
    dy, dx = 1, 3
    rows = input_file.read().splitlines()

    print('The answer for Day 03 Part A :', get_tree_hits(dy, dx, rows))
