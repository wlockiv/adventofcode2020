from typing import IO, List, Optional, Tuple
import re
import math
from .day04a import CardNumber, BingoCard, parse_raw_cards


def main(input_file: IO):
    input_raw = input_file.read()
    input_groups = input_raw.split('\n\n')
    numbers_to_call = [int(i) for i in input_groups[0].split(',')]
    raw_cards = input_groups[1:]

    cards: List[BingoCard] = parse_raw_cards(raw_cards)

    cards_in_play = cards.copy()
    bingod_cards: List[Tuple[BingoCard, int]] = []
    for call_num in numbers_to_call:
        if len(cards_in_play) == 0:
            break

        for card in cards_in_play:
            card.call_number(call_num)

        for idx, card in enumerate(cards_in_play):
            if card.has_bingo:
                bingod_cards.append((card, call_num))
                cards_in_play.pop(idx)
        else:
            continue
        break

    sum_of_unmarked_numbers = sum(
        [num.number for num in bingod_cards[-1][0].card_numbers if num.called == False])

    print('The answer for Day 04 Part B :',
          sum_of_unmarked_numbers * bingod_cards[-1][1])
