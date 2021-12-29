from typing import IO, List, Tuple, Set
from adventofcode.util import print_solution


def find_all_corrupted(lines: List[str]) -> Tuple[List[str], Set[str]]:
    opens, closes = "{([<", "})]>"
    pairs = {k: v for k, v in zip(closes, opens)}

    errors = []
    error_lines = set()
    for line in lines:
        brackets = []
        for c in line:
            if c in opens:
                brackets.append(c)
            elif pairs[c] == brackets[-1]:
                brackets.pop()
            else:
                errors.append(c)
                error_lines.add(line)
                break

    return errors, error_lines


def main(input_file: IO):
    input_lines: List[str] = input_file.read().splitlines()

    errors = find_all_corrupted(input_lines)[0]

    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    total_score = sum([points[e] for e in errors])

    print_solution(str(total_score))
