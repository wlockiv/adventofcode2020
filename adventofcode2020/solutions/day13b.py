import math
from typing import IO, Dict


def main(input_file: IO):
    # Input Parsing
    input_lines = input_file.read().split('\n')
    ids = [int(i) if i != 'x' else 0 for i in input_lines[1].split(',')]
    offsets = list(range(len(ids)))
    offset_map = {_id: offset for offset, _id in zip(offsets, ids) if _id != 0}
    ids = list(filter(lambda x: x != 0, ids))

    step = ids.pop(0)
    t = step
    finished = False
    while not finished:
        # print(t)
        for _id in ids:
            current_t = math.ceil(t / _id) * _id
            if t + offset_map[_id] != current_t:
                t += step
                finished = False
                break
            else:
                print(f'{t} - {current_t} == {offset_map[_id]}')
                finished = True

    offset_of_step = max(offset_map, key=offset_map.get)
    result = t - offset_of_step
    print('The answer for Day 13 Part B :', result)
