
from typing import IO


def main(input_file: IO):
    input_lines = input_file.readlines()
    input_list = [int(i, 2) for i in input_lines]

    # Get the "width" of the binary - "00001" = 5
    bin_width = len(input_lines[0].strip())

    # Get the number where only one position is 1, up to the width
    # of the binary. These act as "masks". Using `width = 5` as an example:
    #   2**0 = 1 = "00001"
    #   2**1 = 2 = "00010"
    #   2**2 = 4 = "00100"
    #   ...
    masks = [2 ** n for n in range(bin_width)]

    # Start looping over each column's "mask"
    gamma, epsilon = 0, 0
    for mask in masks:
        # Check if the single bit for this mask has a zero on each input line.

        mask_results = [i & mask for i in input_list]

        count_of_matching_masks = sum(mask_results) // mask
        min_count_to_be_majority = len(input_list) / 2

        if count_of_matching_masks >= min_count_to_be_majority:
            # 1 is in the majority
            gamma = gamma + mask

        if count_of_matching_masks <= min_count_to_be_majority:
            # 0 is in the majority
            epsilon = epsilon + mask

    print('The answer for Day 03 Part A :', gamma * epsilon)
