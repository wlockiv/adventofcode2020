from typing import IO


# My brute force solution wasn't ideal. This one is taken from:
# https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gfa8gtm?utm_source=share&utm_medium=web2x&context=3

def main(input_file: IO):
    input_lines = input_file.read().split('\n')
    adapters = sorted([int(i) for i in input_lines])

    ways_to = {0: 1}

    for adapter in adapters:
        count = 0
        for i in [1, 2, 3]:
            if (diff := adapter - i) in ways_to:
                count += ways_to[diff]
        ways_to[adapter] = count

    print('The answer for Day 10 Part B :', ways_to[adapters[-1]])
