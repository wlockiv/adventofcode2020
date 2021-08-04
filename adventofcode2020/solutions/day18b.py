from typing import IO, List
from .day18a import solve


def calculate(expression: List[str]) -> str:
    while "+" in expression:
        for i, ex in enumerate(expression):
            if ex == "+":
                total = int(expression[i - 1]) + int(expression[i + 1])
                expression = expression[:i - 1] + [total] + expression[i + 2:]
                break

    return str(eval(''.join([str(x) for x in expression])))


def main(input_file: IO):
    raw_input = input_file.read().splitlines()

    result = 0
    for line in raw_input:
        expression = [e for e in line.replace(" ", "")]
        result += solve(expression, calculate)

    print('The answer for Day 18 Part B :', result)
