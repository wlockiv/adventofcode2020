from collections import defaultdict
from typing import IO, Dict, List


# Lots of this is copied:
# https://github.com/elvinyhlee/advent-of-code-2020-python/blob/master/day16.py

def parse_rules(rules) -> Dict[str, List[tuple]]:
    acceptable = defaultdict(list)
    for rule in rules.split('\n'):
        rule_name, ranges = rule.split(':')
        ranges = ranges.split(' or ')
        for r in ranges:
            lower, upper = r.split('-')
            acceptable[rule_name].append((int(lower), int(upper)))

    return acceptable


def main(input_file: IO):
    raw_input = input_file.read().split('\n\n')
    rules, my_ticket, nearby_tickets = raw_input

    rule_map = parse_rules(rules)
    my_ticket = [int(n) for n in my_ticket.split('\n')[1].split(',')]
    tickets = [row.split(',') for row in nearby_tickets.split('\n')][1:]
    possible_fields = [set()] * len(tickets[0])

    for ticket in tickets:
        for idx, num in enumerate(ticket):
            fields = set()

            for name, rule in rule_map.items():
                for from_num, to_num in rule:
                    if from_num <= int(num) <= to_num:
                        fields.add(name)

            if fields:
                possible_fields[idx] = \
                    possible_fields[idx].intersection(fields) \
                        if possible_fields[idx] else fields

    sorted_possible_fields = [
        [len(fields), idx, fields]
        for idx, fields in enumerate(possible_fields)
    ]
    sorted_possible_fields.sort()

    visited = set()
    ans = 1
    for idx, data in enumerate(sorted_possible_fields):
        length, index, fields = data
        field_name = list(fields - visited)[0]
        if 'departure' in field_name:
            ans *= my_ticket[index]
        visited = visited.union(fields)

    print('The answer for Day 16 Part B :', ans)
