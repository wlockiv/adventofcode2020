from typing import IO, List, Dict, Set
from collections import defaultdict
from adventofcode.util import print_solution


def is_cave_small(node: str) -> bool:
    if node.upper() == node:
        return False

    return True


def find_paths(graph, current_vertex, visited, all_paths: List[List[str]], small_counts: Dict[str, int] = defaultdict(int)):
    visited.append(current_vertex)
    if is_cave_small(current_vertex):
        small_counts[current_vertex] += 1

    if current_vertex == 'end':
        all_paths.append(visited)
        return

    for next_vertex in graph[current_vertex]:
        if next_vertex == 'start':
            continue
        if next_vertex in visited and is_cave_small(next_vertex):
            if list(small_counts.values()).count(2) == 1:
                continue

        find_paths(graph, next_vertex, visited.copy(),
                   all_paths, small_counts.copy())


def main(input_file: IO):
    input_lines: List[str] = input_file.read().splitlines()

    graph = defaultdict(set)
    for line in input_lines:
        start, end = line.split('-')
        graph[start].add(end)
        graph[end].add(start)

    paths = []
    find_paths(graph, 'start', [], paths)

    print_solution(str(len(paths)))
