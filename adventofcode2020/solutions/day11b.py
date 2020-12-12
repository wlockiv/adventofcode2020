from typing import IO, List

# Heavily inspired by https://pastebin.com/KgkBmbxi

EMPTY, TAKEN, FLOOR = 'L', '#', '.'


def get_visible_coords(x: int, y: int, seating: List[str]) -> List[tuple]:
    visible = []

    x_max = len(seating[0]) - 1
    y_max = len(seating) - 1

    directions = {
        "N": lambda _x, _y, d: (_x, _y - d),
        "NE": lambda _x, _y, d: (_x + d, _y - d),
        "E": lambda _x, _y, d: (_x + d, _y),
        "SE": lambda _x, _y, d: (_x + d, _y + d),
        "S": lambda _x, _y, d: (_x, _y + d),
        "SW": lambda _x, _y, d: (_x - d, _y + d),
        "W": lambda _x, _y, d: (_x - d, _y),
        "NW": lambda _x, _y, d: (_x - d, _y - d),
    }

    delta = 1
    while dirs := list(directions):
        for d in dirs:
            new_x, new_y = directions[d](x, y, delta)
            if not (0 <= new_x <= x_max) or not (0 <= new_y <= y_max):
                del directions[d]
            elif (seat := seating[new_y][new_x]) == EMPTY:
                del directions[d]
            elif seat == TAKEN:
                visible.append((new_x, new_y))
                del directions[d]
        delta += 1
    return visible


def run_model(all_rows: List[str]) -> List[str]:
    result = all_rows.copy()

    for y, row in enumerate(all_rows):
        for x, seat in enumerate(row):
            if seat in FLOOR:
                # Skip if FLOOR
                continue

            visible_seats = get_visible_coords(x, y, all_rows)
            visible_seat_statuses = [all_rows[ay][ax] for ax, ay in visible_seats]

            if (taken_count := visible_seat_statuses.count(TAKEN)) == 0:
                # If no seats are taken, seat becomes taken
                row_list = list(result[y])
                row_list[x] = TAKEN
                result[y] = ''.join(row_list)
            elif taken_count >= 5:
                # If 4 or more seats are taken, seat becomes empty
                row_list = list(result[y])
                row_list[x] = EMPTY
                result[y] = ''.join(row_list)

    return result


def main(input_file: IO):
    # Input Parsing
    input_lines = input_file.read().split('\n')

    previous = []
    current = input_lines
    result = 0
    while True:
        previous = current
        current = run_model(current)

        if (joined := ''.join(current)) == ''.join(previous):
            result = joined.count(TAKEN)
            break

    print('The answer for Day 11 Part B :', result)
