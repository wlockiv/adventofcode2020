import math
from typing import IO, List


def get_tree_hits(dy: int, dx: int, base_field_rows: List[str]):
    field_height = len(base_field_rows)
    total_steps = math.ceil(field_height / dy)
    field_repeats = math.ceil((total_steps * dx) / len(base_field_rows[0]))

    full_field = [base_field_rows[idx] * field_repeats for idx in range(len(base_field_rows))]

    trees_hit = 0

    for step in range(total_steps):
        x, y = (step * dx, step * dy)
        if full_field[y][x] == '#':
            trees_hit += 1

    return trees_hit


def main(input_file: IO):
    dy, dx = 1, 3
    rows = input_file.read().splitlines()

    print('The answer for Day 03 Part A :', get_tree_hits(dy, dx, rows))
