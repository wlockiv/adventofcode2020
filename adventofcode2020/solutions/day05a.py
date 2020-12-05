import math
from typing import IO, Dict, Tuple


def binary_locate(binary_input: str, input_map: Dict, _range=Tuple[int]) -> int:
    if not _range:
        _range = (0, 2 ** len(binary_input) - 1)

    if len(i := binary_input) == 1:
        return _range[0] if i == input_map['down'] else _range[1]

    new_range = ()
    if binary_input[0] == input_map['down']:
        new_range = (
            _range[0],
            ((_range[1] - _range[0]) // 2) + _range[0])
    elif binary_input[0] == input_map['up']:
        new_range = (
            math.ceil((_range[1] - _range[0]) / 2) + _range[0],
            _range[1])

    return binary_locate(binary_input[1:], input_map, new_range)


def main(input_file: IO):
    boarding_passes = input_file.read().splitlines()

    greatest_seat_id = 0
    seat_ids = []

    for bp in boarding_passes:
        row_input, column_input = bp[:-3], bp[-3:]

        row = binary_locate(row_input, {'up': 'B', 'down': 'F'})
        column = binary_locate(column_input, {'up': 'R', 'down': 'L'})

        seat_ids.append(row * 8 + column)

        if (seat_id := row * 8 + column) > greatest_seat_id:
            greatest_seat_id = seat_id

    print('The answer for Day 05 Part A :', greatest_seat_id)
