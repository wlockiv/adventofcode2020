from collections import defaultdict
from typing import IO, List

EMPTY, TAKEN, FLOOR = 'L', '#', '.'


def get_adjacent_coords(x: int, y: int, x_max: int, y_max: int) -> List[tuple]:
    dxy = ((0, -1), (1, 0), (0, 1), (-1, 0),
           (1, -1), (1, 1), (-1, 1), (-1, -1))

    results = []
    for dx, dy in dxy:
        new_x, new_y = x - dx, y - dy
        if 0 <= new_x <= x_max and 0 <= new_y <= y_max:
            results.append((new_x, new_y))
    return results


def run_model(all_rows: List[str], adjacency_map) -> List[str]:
    result = all_rows.copy()

    for y, row in enumerate(all_rows):
        for x, seat in enumerate(row):
            if seat in FLOOR:
                # Skip if FLOOR
                continue

            adjacent_seats = [all_rows[ay][ax] for ax, ay in adjacency_map[(x, y)]]

            if (taken_count := adjacent_seats.count(TAKEN)) == 0:
                # If no seats are taken, seat becomes taken
                row_list = list(result[y])
                row_list[x] = TAKEN
                result[y] = ''.join(row_list)
            elif taken_count >= 4:
                # If 4 or more seats are taken, seat becomes empty
                row_list = list(result[y])
                row_list[x] = EMPTY
                result[y] = ''.join(row_list)

    return result


def main(input_file: IO):
    # Input Parsing
    input_lines = input_file.read().split('\n')

    adjacency_map = defaultdict(list)
    for y, row in enumerate(input_lines):
        for x, seat in enumerate(row):
            adjacency_map[(x, y)] = get_adjacent_coords(x, y, len(row) - 1, len(input_lines) - 1)

    previous = []
    current = input_lines
    result = 0
    while True:
        previous = current
        current = run_model(current, adjacency_map)

        if (joined := ''.join(current)) == ''.join(previous):
            result = joined.count(TAKEN)
            break

    print('The answer for Day 11 Part A :', result)
