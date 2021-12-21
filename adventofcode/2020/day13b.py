from typing import IO


# Inspired by:
# https://www.reddit.com/r/adventofcode/comments/kc4njx/2020_day_13_solutions/gfth69h?utm_source=share&utm_medium=web2x&context=3


def main(input_file: IO):
    # Input Parsing
    input_lines = input_file.read().split('\n')
    buses = input_lines[1].split(',')
    ids = [(int(buses[i]), i) for i in range(len(buses)) if buses[i] != 'x']

    lcm = 1
    time = 0
    for i in range(len(ids) - 1):
        bus_id = ids[i + 1][0]
        offset = ids[i + 1][1]
        lcm *= ids[i][0]
        while (time + offset) % bus_id != 0:
            time += lcm

    print('The answer for Day 13 Part B :', time)
