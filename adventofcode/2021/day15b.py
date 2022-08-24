from typing import IO, List
from adventofcode.util import print_solution
from .day15a import NodeDict, dijkstras


def main(input_file: IO):
    input_lines: List[str] = input_file.read().splitlines()
    tile_w, tile_h = len(input_lines[0]), len(input_lines)

    nodes: NodeDict = {}
    # Make the node dictionary
    for y, line in enumerate(input_lines):
        for x, weight in enumerate(line):
            nodes[(x, y)] = int(weight)

    horiz = {}
    # Copy the original tile horizontally
    for offset in range(5):
        for (x, y), danger in nodes.items():
            horiz[(x + (tile_w * offset), y)] = danger + \
                offset if not (danger + offset >
                               9) else ((danger + offset + 1) % 10)

    # Copy the horizontal tiles vertically
    for offset in range(1, 5):
        # Now, extend them all vertically
        for (x, y), danger in horiz.items():
            nodes[(x, y + (tile_h * offset))] = danger + \
                offset if not (danger + offset >
                               9) else ((danger + offset + 1) % 10)

    # Add horiz items to nodes
    nodes.update(horiz)

    destination = (tile_w - 1, tile_h - 1)
    result, _ = dijkstras(nodes)

    print_solution(str(result[destination]))
