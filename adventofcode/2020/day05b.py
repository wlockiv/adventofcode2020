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
    my_seat_id = 0

    for idx, seat_id in enumerate(seat_ids):
        diff = (seat_ids[idx + 1] - seat_id)
        if diff == 2:
            my_seat_id = seat_id + 1
            break

    print('The answer for Day 05 Part B :', my_seat_id)
