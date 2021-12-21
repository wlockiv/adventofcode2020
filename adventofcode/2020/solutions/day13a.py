import math
from typing import IO, Dict


def main(input_file: IO):
    # Input Parsing
    input_lines = input_file.read().split('\n')
    earliest_depart = int(input_lines[0])
    bus_ids = [int(b) for b in input_lines[1].split(',') if b != 'x']

    wait_times: Dict[int, int] = {}
    for b_id in bus_ids:
        multiple = math.ceil(earliest_depart / b_id)
        closest_time = multiple * b_id
        wait_times[closest_time - earliest_depart] = b_id
    shortest_wait = min(wait_times.keys())

    result = shortest_wait * wait_times[shortest_wait]
    print('The answer for Day 13 Part A :', result)
