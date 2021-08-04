from typing import IO, List, Callable


def calculate(expression: List[str]) -> str:
    current = int(expression[0])

    for idx, ex in enumerate(expression[1:], 1):
        if (op := expression[idx - 1]) == "+":
            current += int(ex)
        elif op == "*":
            current *= int(ex)

    return str(current)


def solve(expression: List[str], evaluator: Callable[[List[str]], str] = calculate) -> int:
    # Uniforming the expr and breaking it into
    expression = expression

    while '(' in expression:
        start = 0
        end = 0

        for idx, ex in enumerate(expression):
            if ex == '(':
                start = idx
            if ex == ')':
                end = idx
                total = evaluator(expression[start + 1:end])
                expression = expression[:start] + [total] + expression[end + 1:]
                break

    return int(evaluator(expression))


def main(input_file: IO):
    raw_input = input_file.read().splitlines()

    result = 0
    for line in raw_input:
        expression = [e for e in line.replace(" ", "")]
        result += solve(expression)

    print('The answer for Day 18 Part A :', result)
