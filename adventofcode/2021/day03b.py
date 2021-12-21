
from itertools import compress
from os import X_OK
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
    masks = [2 ** n for n in reversed(range(bin_width))]

    # Start looping over each column's "mask"
    gamma, epsilon = 0, 0
    final_candidates = [0, 0]
    oxy_list = input_list.copy()
    co2_list = input_list.copy()

    while True:
        for mask in masks:
            if len(oxy_list) > 1:
                mask_results = [i & mask for i in oxy_list]
                count_of_matching_masks = sum(mask_results) // mask
                min_count_to_be_majority = len(oxy_list) / 2

                if count_of_matching_masks >= min_count_to_be_majority:
                    # 1 is in the majority or 1 and 0 are tied
                    oxy_list = list(compress(
                        oxy_list, mask_results))
                else:
                    # 0 is in the majority
                    oxy_list = list(compress(
                        oxy_list, [not r for r in mask_results]))

            if len(co2_list) > 1:
                mask_results = [i & mask for i in co2_list]
                count_of_matching_masks = sum(mask_results) // mask
                min_count_to_be_majority = len(co2_list) / 2

                if count_of_matching_masks < min_count_to_be_majority:
                    # 1 is in the minority
                    co2_list = list(compress(
                        co2_list, mask_results))
                else:
                    # 0 is in the majority or equal
                    co2_list = list(compress(
                        co2_list, [not r for r in mask_results]))

        if not len(oxy_list) > 1 and not len(co2_list) > 1:
            break

    print('The answer for Day 03 Part A :', oxy_list[0] * co2_list[0])
