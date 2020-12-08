from typing import IO, List, Tuple, Set, Dict, Callable

Instruction = Tuple[int, str, int]
CommandFunction = Callable[[], Instruction]


class Decoder:
    instructions: List[Instruction]
    current_instruction: Instruction
    accumulator: int
    visited: Set[Instruction]
    command_map: Dict[str, CommandFunction]

    def __init__(self, input_lines: List[str]):
        self.accumulator = 0
        self.instructions = []
        self.visited = set()

        self.command_map = {
            'acc': self.acc,
            'nop': self.nop,
            'jmp': self.jmp,
        }

        for idx, line in enumerate(input_lines):
            cmd, arg = line[:3], int(line[4:])
            self.instructions.append((idx, cmd, arg))

        self.current_instruction = self.instructions[0]

    def acc(self) -> Instruction:
        """Increments the accumulator value by 'n' then returns the next index."""
        idx, _, arg = self.current_instruction
        self.accumulator += arg
        next_instruction = self.instructions[idx + 1]
        return next_instruction

    def nop(self) -> Instruction:
        """Returns the index of the next instruction."""
        idx, _, _ = self.current_instruction
        next_instruction = self.instructions[idx + 1]
        return next_instruction

    def jmp(self) -> Instruction:
        """Returns the index of the next instruction."""
        idx, _, arg = self.current_instruction
        next_instruction = self.instructions[idx + arg]
        return next_instruction

    def execute_instructions(self):
        while (c_ins := self.current_instruction) not in self.visited:
            self.visited.add(c_ins)
            _, cmd, _ = c_ins
            cmd_function = self.command_map[cmd]
            next_instruction = cmd_function()
            self.current_instruction = next_instruction


def main(input_file: IO):
    input_lines = input_file.read().split('\n')
    decoder = Decoder(input_lines)
    decoder.execute_instructions()

    print('The answer for Day 08 Part A :', decoder.accumulator)
