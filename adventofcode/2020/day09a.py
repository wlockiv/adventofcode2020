import itertools
from typing import IO, List, Set


class Decryptor:
    data = List[int]
    _pointer: int

    def __init__(self, input_lines: List[str]):
        self.data = [int(i) for i in input_lines]
        self._pointer = 25

    @property
    def preamble_sums(self) -> Set[int]:
        """Returns all the possible sums for the current preamble."""
        right, left = self._pointer - 25, self._pointer
        preamble = self.data[right:left]
        combinations = itertools.combinations(preamble, 2)
        sums = [sum(c) for c in combinations]

        return set(sums)

    def find_error(self):
        """Finds the first data point that cannot be derived from the preamble."""
        while self.data[self._pointer] in self.preamble_sums:
            self._pointer += 1

        return self.data[self._pointer]


def main(input_file: IO):
    input_lines = input_file.read().split('\n')
    decryptor = Decryptor(input_lines)

    print('The answer for Day 09 Part A :', decryptor.find_error())
