from typing import IO


def main(input_file: IO):
    declarations = input_file.read().split('\n\n')

    answer_counts = 0

    for group in declarations:
        answers = list(group.replace('\n', ''))
        unique_answers = set(answers)
        answer_counts += len(unique_answers)

    print('The answer for Day 06 Part A :', answer_counts)
