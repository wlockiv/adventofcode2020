from typing import IO

from .day03a import get_tree_hits


def main(input_file: IO):
    rows = input_file.read().splitlines()
    slopes = [
        {'dx': 1, 'dy': 1},
        {'dx': 3, 'dy': 1},
        {'dx': 5, 'dy': 1},
        {'dx': 7, 'dy': 1},
        {'dx': 1, 'dy': 2},
    ]

    product_of_hits = 1

    for slope in slopes:
        trees_hit = get_tree_hits(slope['dy'], slope['dx'], base_field_rows=rows.copy())
        product_of_hits *= trees_hit

    print('The answer for Day 03 Part B :', product_of_hits)
