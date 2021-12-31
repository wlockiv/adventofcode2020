from typing import IO, List, Dict, Set, Tuple
from adventofcode.util import print_solution

Point = Tuple[int, int]
Grid = Dict[Point, int]


def get_neighbors(grid: Grid, point: Point) -> List[Point]:
    x, y = point
    neighbor_points = [(x+1, y), (x-1, y), (x, y+1), (x, y-1),
                       (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)]

    return [p for p in neighbor_points if grid.get(p) is not None]


def flash(grid: Grid) -> int:
    side_effects = []

    for point in grid:
        if grid[point] > 9:
            grid[point] = 0
            side_effects.append(point)

    if side_effects:
        for point in side_effects:
            neighbors = get_neighbors(grid, point)

            for n_point in neighbors:
                if grid[n_point] != 0:
                    grid[n_point] += 1

        return len(side_effects) + flash(grid)
    else:
        return len(side_effects)


def main(input_file: IO):
    input_lines: List[str] = input_file.read().splitlines()

    grid: Grid = {}
    for y, row in enumerate(input_lines):
        for x, num in enumerate(row):
            grid[(x, y)] = int(num)

    total_flashes = 0
    for _ in range(100):
        # Initial increments of the step
        for point in grid:
            grid[point] += 1

        total_flashes += flash(grid)

    print_solution(str(total_flashes))
