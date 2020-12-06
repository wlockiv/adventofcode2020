from typing import IO


def main(input_file: IO):
    declarations = input_file.read().split('\n\n')

    answer_counts = 0

    for group in declarations:
        response_counts = {}

        for person in group.split('\n'):
            for letter in list(person):
                if not response_counts.get(letter, None):
                    response_counts[letter] = 1
                else:
                    response_counts[letter] += 1

        for ans, count in response_counts.items():
            if count == len(group.split('\n')):
                answer_counts += 1

    print('The answer for Day 06 Part B :', answer_counts)
