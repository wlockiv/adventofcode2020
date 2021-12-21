from typing import IO


def main(input_file: IO):
    input_lines = input_file.read().split('\n')
    adapters = sorted([int(i) for i in input_lines])
    adapters.append(adapters[-1] + 3)
    adapters.insert(0, 0)
    diff_counts = {1: 0, 2: 0, 3: 0}

    for i, cur in enumerate(adapters):
        try:
            nxt = adapters[i + 1]
            diff_counts[nxt - cur] += 1
        except IndexError:
            break

    answer = diff_counts[1] * diff_counts[3]

    print('The answer for Day 10 Part A :', answer)
