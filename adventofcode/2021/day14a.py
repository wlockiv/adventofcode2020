from typing import IO, List
from adventofcode.util import print_solution
from collections import defaultdict


def find_counts(input_lines: List[str], steps) -> int:
    template, rules = input_lines[0], input_lines[2:]

    template = [l for l in template]

    combo_counts = defaultdict(int)
    for i in range(1, len(template)):
        combo = template[i - 1] + template[i]
        combo_counts[combo] += 1

    rules = [r.split(' -> ') for r in rules]
    rules = {k: v for k, v in rules}

    for _ in range(steps):
        new_combo_counts = defaultdict(int)
        for combo, count in combo_counts.items():
            new_combo_counts[combo[0] + rules[combo]] += count
            new_combo_counts[rules[combo] + combo[1]] += count

        combo_counts = new_combo_counts

    letter_counts = defaultdict(int)
    for combo, count in combo_counts.items():
        letter_counts[combo[0]] += count
        letter_counts[combo[1]] += count

    counts = [(letter, (count + 1) // 2)
              for letter, count in letter_counts.items()]
    counts.sort(key=lambda x: x[1])
    least, most = counts[0][1], counts[-1][1]

    return most - least


def main(input_file: IO):
    input_lines: List[str] = input_file.read().splitlines()
    solution = find_counts(input_lines, 10)

    print_solution(str(solution))
