from typing import IO


def main(input_file: IO):
    input_lines = input_file.read().splitlines()

    mask = []
    memory = {}
    for line in input_lines:
        instruction, val = line.split(' = ')
        if instruction == 'mask':
            mask = [(pos, m) for pos, m in enumerate(val) if m != 'X']
        elif 'mem' in instruction:
            address = int(instruction[4:-1])
            bin_list = list('{:036b}'.format(int(val)))
            for pos, m in mask:
                bin_list[pos] = m
            memory[address] = int(''.join(bin_list), base=2)

    result = sum(memory.values())

    print('The answer for Day 14 Part A :', result)
