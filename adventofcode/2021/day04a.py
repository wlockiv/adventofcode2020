import enum
from typing import IO, List, Optional, Tuple
import re
import math


class CardNumber:
    row: int
    col: int
    number: int
    called: bool = False

    def __init__(self, row: int, col: int, number: int) -> None:
        self.row = row
        self.col = col
        self.number = number


class BingoCard:
    #   r0 1 2 3 4
    # c0 0 0 0 0 0
    #  1 0 0 0 0 0
    #  2 0 0 0 0 0
    #  3 0 0 0 0 0
    #  4 0 0 0 0 0

    card_numbers: List[CardNumber]
    called_row_counts: List[int]
    called_col_counts: List[int]

    def __init__(self, card_numbers: List[CardNumber]) -> None:
        self.card_numbers = card_numbers
        self.called_row_counts = [0 for _ in range(self.card_size)]
        self.called_col_counts = [0 for _ in range(self.card_size)]

    @property
    def card_size(self) -> int:
        return int(math.sqrt(len(self.card_numbers)))

    @property
    def has_bingo(self) -> Tuple[List[bool], List[bool]]:
        row_bingos = [i == self.card_size for i in self.called_row_counts]
        col_bingos = [i == self.card_size for i in self.called_col_counts]

        return row_bingos, col_bingos

    @property
    def col_sums(self) -> List[int]:
        result = [0 for _ in range(self.card_size)]
        for num in self.card_numbers:
            result[num.col] = result[num.col] + num.number

        return result

    @property
    def row_sums(self):
        result = [0 for _ in range(self.card_size)]
        for num in self.card_numbers:
            result[num.row] = result[num.row] + num.number

        return result

    def call_number(self, called_number: int):
        for card_num in self.card_numbers:
            if called_number == card_num.number:
                card_num.called = True
                row_num, col_num = card_num.row, card_num.col
                self.called_row_counts[row_num] = self.called_row_counts[row_num] + 1
                self.called_col_counts[col_num] = self.called_col_counts[col_num] + 1
                break


def main(input_file: IO):
    input_raw = input_file.read()
    input_groups = input_raw.split('\n\n')
    numbers_to_call = [int(i) for i in input_groups[0].split(',')]
    raw_cards = input_groups[1:]

    # Set up the bingo card
    cards: List[BingoCard] = []
    for raw_card in raw_cards:
        card_numbers: List[CardNumber] = []
        for row_num, row in enumerate(raw_card.split('\n')):
            for col_num, num in enumerate([int(n) for n in re.findall(r'\s?\d+', row)]):
                card_numbers.append(CardNumber(row_num, col_num, num))
        cards.append(BingoCard(card_numbers))

    bingod_card: Optional[BingoCard] = None
    bingod_call_num: Optional[int] = None
    for call_num in numbers_to_call:
        for idx, card in enumerate(cards):
            card.call_number(call_num)
            row_bingo, col_bingo = card.has_bingo

            if any(row_bingo) or any(col_bingo):
                bingod_card = card
                bingod_call_num = call_num
                break
        else:
            continue
        break

    if bingod_card and bingod_call_num:
        sum_of_unmarked_numbers = sum(
            [num.number for num in bingod_card.card_numbers if num.called == False])
        print('The answer for Day 04 Part A :',
              sum_of_unmarked_numbers * bingod_call_num)
    else:
        print('No solution was found :(')
