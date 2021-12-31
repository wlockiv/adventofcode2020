from typing import IO, Dict, List, Tuple
from adventofcode.util import print_solution
from .day09a import find_low_points
from math import prod

Grid = Dict[Tuple[int, int], int]


def find_basins(grid: Grid, current_point: Tuple[int, int], visited: set):
    if grid.get(current_point) is None:
        # Is valid
        return visited

    if current_point in visited or grid[current_point] == 9:
        # Hasn't been visited
        return visited

    if grid[current_point] == 9:
        # Isn't a 9
        return visited

    visited.add(current_point)

    x, y = current_point
    neighbors = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]

    for n in neighbors:
        visited = find_basins(grid, n, visited)

    return visited


def main(input_file: IO):
    input_lines: List[str] = input_file.read().splitlines()

    grid: Grid = {}
    for y, row in enumerate(input_lines):
        for x, num in enumerate(row):
            grid[(x, y)] = int(num)

    low_points = find_low_points(grid)[0]

    basin_sizes = []
    for point in low_points:
        basin = find_basins(grid, point, set())
        basin_sizes.append(len(basin))

    basin_sizes.sort(reverse=True)

    print_solution(str(prod(basin_sizes[:3])))
