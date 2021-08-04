from typing import IO, List


def main(input_file: IO):
    raw_input = input_file.read().splitlines()

    instructions = {}

    instruction_toggle = False
    for line in raw_input:
        if not line:
            instruction_toggle = True

        if not instruction_toggle:
            number, value = line.split(': ')
            instructions[number] = value
        else:
            break

    print(instructions['0'])

    print('The answer for Day 19 Part A :', 0)
