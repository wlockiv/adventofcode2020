from os import error
from typing import IO, List
from adventofcode.util import print_solution
from .day10a import find_all_corrupted


def main(input_file: IO):
    input_lines: List[str] = input_file.read().splitlines()

    error_lines = find_all_corrupted(input_lines)[1]

    points = {"(": 1, "[": 2, "{": 3, "<": 4}

    point_tallies = []
    for line in input_lines:
        if line in error_lines:
            continue

        brackets = []
        for c in line:
            if c in "{([<":
                brackets.append(c)
                continue

            brackets.pop()

        score = 0
        for i in range(len(brackets) - 1, -1, -1):
            score = (score * 5) + points[brackets[i]]
        point_tallies.append(score)

    point_tallies.sort()
    answer = point_tallies[(len(point_tallies) // 2)]

    print_solution(str(answer))
