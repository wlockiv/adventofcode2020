from typing import IO, Set

from .day08a import Decoder, Instruction


class DecoderB(Decoder):
    # TODO: Convert attempted_swaps to set()?
    attempted_swaps: Set[Instruction] = set()
    cmd_swap_map = {'jmp': 'nop', 'nop': 'jmp'}
    already_swapped = False

    def reset(self):
        self.accumulator = 0
        self.current_instruction = self.instructions[0]
        self.visited.clear()
        self.already_swapped = False

    def swap(self):
        self.attempted_swaps.add(self.current_instruction)
        self.already_swapped = True

        idx, cmd, arg = self.current_instruction
        new_cmd = self.cmd_swap_map[cmd]
        self.current_instruction = (idx, new_cmd, arg)

    def execute_instructions(self):
        while True:
            if self.current_instruction in self.visited:
                self.reset()

            idx, cmd, arg = self.current_instruction

            swappable = cmd in self.cmd_swap_map
            not_yet_attempted = self.current_instruction not in self.attempted_swaps

            if not self.already_swapped and swappable and not_yet_attempted:
                self.swap()
                cmd = self.current_instruction[1]

            self.visited.add(self.current_instruction)

            cmd_function = self.command_map[cmd]
            try:
                next_instruction = cmd_function()
                self.current_instruction = next_instruction
            except IndexError:
                break


def main(input_file: IO):
    input_lines = input_file.read().split('\n')
    decoder = DecoderB(input_lines)
    decoder.execute_instructions()

    print('The answer for Day 08 Part B :', decoder.accumulator)
