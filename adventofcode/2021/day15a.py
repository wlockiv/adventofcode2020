import heapq
from math import inf
from typing import IO, Dict, Iterable, List, Tuple

from adventofcode.util import print_solution

Coord = Tuple[int, int]
NodeDict = Dict[Coord, int]
EdgesDict = Dict[Tuple[Coord, Coord], int]
AdjacencyDict = Dict[Coord, NodeDict]


def get_neighbors_4(nodes: NodeDict, src: Tuple[int, int]) -> Iterable[Coord]:
    x, y = src
    neighbor_coords = [
        (x, y-1), (x+1, y), (x, y+1), (x-1, y),
    ]

    for n in neighbor_coords:
        if n in nodes:
            yield n


def dijkstras(nodes: NodeDict, source_coord: Coord = (0, 0)):
    shortest_dists = {n: inf for n in nodes}
    shortest_dists[source_coord] = 0
    queue: List[Tuple[int, Coord]] = [(0, source_coord)]
    visited = set()
    paths = {}

    while queue:
        dist, node = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)

        for neighbor in get_neighbors_4(nodes, node):
            if neighbor in visited:
                continue

            new_dist = dist + nodes[neighbor]

            if new_dist < shortest_dists[neighbor]:
                shortest_dists[neighbor] = new_dist
                paths[neighbor] = node
                heapq.heappush(queue, (new_dist, neighbor))

    return shortest_dists, paths


def main(input_file: IO):
    input_lines: List[str] = input_file.read().splitlines()
    max_x, max_y = len(input_lines[0])-1, len(input_lines)-1

    nodes: NodeDict = {}
    # Make the node dictionary
    for y, line in enumerate(input_lines):
        for x, weight in enumerate(line):
            nodes[(x, y)] = int(weight)

    result, _ = dijkstras(nodes)

    print_solution(str(result[(max_x, max_y)]))
