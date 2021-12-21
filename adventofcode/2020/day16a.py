from typing import IO


def parse_rules(rules) -> set:
    acceptable = set()
    for r in rules.split('\n'):
        ranges = r.split(':')[1].split(' or ')
        ranges = [r.strip().split('-') for r in ranges]

        for n in ranges:
            acceptable.update(set(range(int(n[0]), int(n[1]) + 1)))

    return acceptable


def main(input_file: IO):
    raw_input = input_file.read().split('\n\n')
    rules, _, nearby_tickets = raw_input

    acceptable = parse_rules(rules)

    errors = []
    for num_set in nearby_tickets.split('\n')[1:]:
        # print(num_set)
        nums = [int(n) for n in num_set.split(',')]
        errors.extend([n for n in nums if n not in acceptable])

    print('The answer for Day 16 Part A :', sum(errors))

