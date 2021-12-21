from typing import IO, List, Set


def generate_messages(instructions: dict, num="0", memo={}):
    if isinstance(instructions[num], str):
        return instructions[num]

    if num in memo:
        return memo[num]

    result = []
    for options in instructions[num]:
        strs = []
        for rule in options:
            sub_opts = generate_messages(instructions, rule)

            if not strs:
                strs.extend(sub_opts)
            else:
                combined = []
                for so in sub_opts:
                    for s in strs:
                        combined.append(s + so)
                strs = combined.copy()

        result += strs

    memo[num] = result
    return result


def main(input_file: IO):
    raw_input = input_file.read().splitlines()

    # {#: [[1, 2], [2, 1] or #: "a"}
    instructions = {}
    messages = []

    instruction_toggle = False
    for line in raw_input:
        if not line:
            instruction_toggle = True

        if not instruction_toggle:
            number, raw_value = line.split(': ')

            if raw_value not in {'"a"', '"b"'}:
                value = [v.split(" ") for v in raw_value.split(" | ")]
                instructions[number] = value
            else:
                instructions[number] = raw_value[1:-1]

        else:
            messages.append(line)

    possibilities = set(generate_messages(instructions))

    count = 0
    for m in messages:
        if m in possibilities:
            count += 1

    print('The answer for Day 19 Part A :', count)
