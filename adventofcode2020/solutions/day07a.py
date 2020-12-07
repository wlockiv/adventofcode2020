from typing import IO


def parse_input_to_graph(input_lines):
    graph = {}
    for line in input_lines:
        top_color, contents = line.split('bags contain')
        inner_bags = contents.replace('.', '').replace('bags', '').replace('bag', '')
        inner_bags = inner_bags.split(',')
        graph[top_color.strip()] = [b[2:].strip() for b in inner_bags]

    return graph


def find_path(graph: dict, start: str, end: str, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.get(start):
        return None
    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if new_path:
                return new_path
    return None


def main(input_file: IO):
    input_lines = input_file.read().split('\n')
    graph = parse_input_to_graph(input_lines)
    paths = set()

    for start in graph.keys():
        if path := find_path(graph, start, 'shiny gold'):
            paths.add(tuple(path))

    paths.remove(('shiny gold',))

    print('The answer for Day 07 Part A :', len(paths))
