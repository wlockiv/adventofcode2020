from typing import IO


def solve(input_str: str, target: int = 2020) -> int:
    numbers = [int(n) for n in input_str.split(',')]
    number_positions = {}

    for idx, num in enumerate(numbers):
        number_positions[num] = idx

    current = numbers[-1]
    for i in range(len(number_positions) - 1, target - 1, 1):
        if current in number_positions:
            prev_turn = number_positions[current]
            number_positions[current] = i
            current = i - prev_turn
        elif current not in number_positions:
            number_positions[current] = i
            current = 0
        else:
            print('Meets neither criteria wtf :(')

    return current


def main(input_file: IO):
    raw_input = input_file.read()
    result = solve(raw_input)

    print('The answer for Day 15 Part A :', result)
