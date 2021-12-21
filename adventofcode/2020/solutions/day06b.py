from typing import IO


def main(input_file: IO):
    declarations = input_file.read().split('\n\n')

    answer_counts = 0

    for group in declarations:
        response_counts = {}
        group_response = [list(p) for p in group.split('\n')]

        for individual_response in group_response:
            for letter in individual_response:
                if response_counts.get(letter):
                    response_counts[letter] += 1
                    continue
                response_counts[letter] = 1

        for letter, count in response_counts.items():
            if count == len(group.split('\n')):
                answer_counts += 1

    print('The answer for Day 06 Part B :', answer_counts)
