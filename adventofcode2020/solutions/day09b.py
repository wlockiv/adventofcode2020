from typing import IO

from .day09a import Decryptor as DecryptorA


class Decryptor(DecryptorA):
    def find_weakness(self, target: int) -> int:
        """
        Finds a set of contiguous data points which add to the target value, then returns the suM of the min and
        max from that list.
        """
        for right_bound in range(len(self.data)):
            acc = 0
            values = []
            for ptr in range(right_bound, len(self.data)):
                if acc == target:
                    return max(values) + min(values)
                if acc > target:
                    break
                values.append(self.data[ptr])
                acc += self.data[ptr]

        return 0


def main(input_file: IO):
    input_lines = input_file.read().split('\n')
    decryptor = Decryptor(input_lines)

    print('The answer for Day 09 Part B :', decryptor.find_weakness(400480901))
