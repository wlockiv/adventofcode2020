from typing import IO


def id_from_binary(input_: str):
    map_ = [('B', '1'), ('F', '0'), ('L', '0'), ('R', '1')]
    for letter, number in map_:
        input_ = input_.replace(letter, number)

    row = int(input_[:7], 2)
    column = int(input_[7:], 2)

    return row * 8 + column


def main(input_file: IO):
    boarding_passes = input_file.read().splitlines()

    seat_ids = []

    for bp in boarding_passes:
        seat_ids.append(id_from_binary(bp))

    seat_ids.sort()
    cursor = seat_ids[0]
    my_seat_id = 0

    for seat_id in seat_ids:
        if cursor != seat_id:
            my_seat_id = cursor
            break
        cursor += 1

    print('The answer for Day 05 Part A :', my_seat_id)
