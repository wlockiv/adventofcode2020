from typing import IO, List, Dict, Tuple
from adventofcode.util import print_solution

# gfedcba
# 1110111 - 0
# 0100100 - 1
# 1011101 - 2
# 1101101 - 3
# 0101110 - 4
# 1101011 - 5
# 1111011 - 6
# 0100101 - 7
# 1111111 - 8
# 1101111 - 9


masks = {
    "a": 1,
    "b": 2,
    "c": 4,
    "d": 8,
    "e": 16,
    "f": 32,
    "g": 64
}


def deduce_key(input: str, knowns={}) -> dict:
    # edbfga begcd cbg(7) gc(1) gcadebf fbgde acbgfd abcde gfcbed gfec(4) |
    # fcgedb cgb(7) dgebacf(8) gc(1)

    key = {k: None for k in range(10)}
    patterns, output = [i.split(' ') for i in input.split(' | ')]
    patterns = [set(''.join(sorted([l for l in p]))) for p in patterns]
    output = []

    key = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0}

    return {}


def letters_to_bits(digit: str) -> int:
    wire_masks = {"a": 1, "b": 2, "c": 4, "d": 8, "e": 16, "f": 32, "g": 64}

    result = 0
    for letter in digit:
        result += wire_masks[letter]

    return result


def bit_count(number: int, one_or_zero='1') -> int:
    return bin(number).split('b')[1].count(one_or_zero)


def get_digits_by_length(digits: List[int], length) -> List[int]:
    return list(filter(
        lambda x: bit_count(x) == length,
        digits
    ))


def find_one(digits: List[int]) -> int:
    return get_digits_by_length(digits, 2)[0]


def find_four(digits: List[int]) -> int:
    return get_digits_by_length(digits, 4)[0]


def find_seven(digits: List[int]) -> int:
    return get_digits_by_length(digits, 3)[0]


def find_eight(digits: List[int]) -> int:
    return get_digits_by_length(digits, 7)[0]


def find_three(digits: List[int], one: int) -> int:
    # 3: 5 segments, has all segments of 1
    # 3 if 3 & 1 = 1
    # 0100100 - 1
    # 1101101 - 3
    # 0100100 - 1

    return [d for d in digits if bit_count(d) == 5 and (d & one == one)][0]


def find_nine(digits: List[int], four: int) -> int:
    # 9: 6 segments, has all segments of 4
    # 9 if 9 & 4 = 4
    # 0101110 - 4
    # 1101111 - 9
    # 0101110 - 4

    return [d for d in digits if bit_count(d) == 6 and (d & four == four)][0]


def find_zero_and_six(digits: List[int], one: int, nine: int) -> Tuple[int, int]:
    zero, six = 0, 0
    for d in get_digits_by_length(digits, 6):
        if d == nine:
            continue

        if d & one == one:
            zero = d
        else:
            six = d

    return zero, six


def find_two_and_five(digits: List[int], three: int, six: int) -> Tuple[int, int]:
    two, five = 0, 0
    for d in get_digits_by_length(digits, 5):
        if d == three:
            continue

        if d & six == d:
            five = d
        else:
            two = d

    return two, five


def main(input_file: IO):
    input_lines: List[str] = input_file.readlines()

    output_sum = 0
    for line in input_lines:
        segments, outputs = line.split(' | ')

        segments = segments.split(' ')
        digits = [letters_to_bits(seg) for seg in segments]

        outputs = [o.strip() for o in outputs.split(' ')]
        output_digits = [letters_to_bits(o) for o in outputs]

        # Simple, wire count-based
        one = find_one(digits)
        four = find_four(digits)
        seven = find_seven(digits)
        eight = find_eight(digits)

        # Comparison-based
        three = find_three(digits, one)
        nine = find_nine(digits, four)
        zero, six = find_zero_and_six(digits, one, nine)
        two, five = find_two_and_five(digits, three, six)

        digit_mappings = {zero: '0', one: '1', two: '2', three: '3',
                          four: '4', five: '5', six: '6', seven: '7', eight: '8', nine: '9'}

        output_number = ''
        for o in output_digits:
            output_number += digit_mappings[o]

        output_sum += int(output_number)

    print_solution(str(output_sum))
