from typing import IO, List, Dict, Type

from adventofcode.util import print_solution

TimerCounts = Dict[str, int]


def be_fruitful(starting_timers: List[str], ticks=80) -> int:
    current_values: List[str] = starting_timers.copy()
    timer_counts: TimerCounts = {
        str(k): current_values.count(str(k)) for k in range(9)}

    for _ in range(ticks):
        next_counts: TimerCounts = {
            '0': timer_counts['1'],
            '1': timer_counts['2'],
            '2': timer_counts['3'],
            '3': timer_counts['4'],
            '4': timer_counts['5'],
            '5': timer_counts['6'],
            '6': timer_counts['7'] + timer_counts['0'],
            '7': timer_counts['8'],
            '8': timer_counts['0']
        }

        timer_counts = next_counts

    return sum(timer_counts.values())


def main(input_file: IO):
    input_lines: List[str] = input_file.readlines()
    timers: List[str] = [i for i in input_lines[0].split(',')]

    population = be_fruitful(timers, 80)

    print_solution(str(population))
