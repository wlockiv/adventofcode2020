import itertools
from typing import IO


def main(input_file: IO):
    input_lines = input_file.read().splitlines()

    mask = []
    memory = {}
    for line in input_lines:
        instruction, val = line.split(' = ')
        if instruction == 'mask':
            mask = [(pos, m) for pos, m in enumerate(val)]
        elif 'mem' in instruction:
            base_address = list('{:036b}'.format(int(instruction[4:-1])))

            x_positions = [pos for pos, m in mask if m == 'X']
            floaters = itertools.product([0, 1], repeat=len(x_positions))

            for pos, m in mask:
                if m in 'X1':
                    base_address[pos] = m

            for f in floaters:
                zipped = list(zip(x_positions, f))
                new_address = base_address.copy()
                for pos, m in zipped:
                    new_address[pos] = str(m)
                memory[''.join(new_address)] = int(val)

    print('The answer for Day 14 Part B :', sum(memory.values()))
