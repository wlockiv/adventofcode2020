from typing import IO, Dict, List, Tuple
from adventofcode.util import print_solution

Point = Tuple[int, int]
Grid = Dict[Point, int]


def find_low_points(grid: Grid) -> Tuple[List[Point], List[int]]:
    low_points = []
    low_point_coords = []
    for coord, current in grid.items():
        x, y = coord
        bool_list = []
        up, down = grid.get((x, y-1)), grid.get((x, y+1))
        left, right = grid.get((x-1, y)), grid.get((x+1, y))

        bool_list = [current < comp for comp in (
            up, down, left, right) if comp is not None]

        if all(bool_list):
            low_points.append(current)
            low_point_coords.append(coord)

    return low_point_coords, low_points


def main(input_file: IO):
    input_lines: List[str] = input_file.read().splitlines()

    grid: Dict[Tuple[int, int], int] = {}
    for y, row in enumerate(input_lines):
        for x, num in enumerate(row):
            grid[(x, y)] = int(num)

    low_points = find_low_points(grid)[1]

    print_solution(str(sum(low_points) + len(low_points)))
