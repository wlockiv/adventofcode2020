from typing import IO, List, Dict, Union


class BagCount:
    color: str
    count: int

    def __init__(self, color: str, count: int):
        self.color = color
        self.count = count

    def __eq__(self, other):
        return other == self.color


class BagCountList(list):
    bag_counts: List[BagCount]

    def __init__(self):
        self.bag_counts = []

    def add_bag_count(self, bag_count: BagCount):
        self.bag_counts.append(bag_count)

    def __contains__(self, item: str):
        return item in [b.color for b in self.bag_counts]

    def __iter__(self):
        return self.bag_counts


class BagGraph:
    graph: Dict[str, BagCountList]

    def __init__(self):
        self.graph = {}

    def add_bag_rule(self, node_color: str, bag_count: BagCount):
        if not self.graph.get(node_color):
            self.graph[node_color] = BagCountList()

        self.graph[node_color].add_bag_count(bag_count)

    def get_rules(self, color):
        return self.graph[color]

    def __contains__(self, item):
        return item in self.graph.keys()


def parse_input_to_graph(input_lines):
    graph = BagGraph()

    for line in input_lines:
        top_color, contents = line.split('bags contain')
        top_color = top_color.strip()

        if 'no other bags' in contents:
            graph.add_bag_rule(top_color, BagCount(top_color, 0))
            continue

        inner_bags = contents.replace('.', '').replace('bags', '').replace('bag', '')
        inner_bags = inner_bags.split(',')

        for bag in inner_bags:
            count = int(bag[:2].strip())
            color = bag[2:].strip()
            bag_count = BagCount(color, count)
            graph.add_bag_rule(top_color, bag_count)

    return graph


def find_path(graph: BagGraph, start: Union[str, BagCount], end: str, path=None):
    if path is None:
        path = []

    start = BagCount(start, 1) if type(start) is str else start
    path = path + [start]

    if start == end:
        return path
    if start.color not in graph:
        return None
    for node in graph.get_rules(start.color):
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if new_path:
                return new_path
    return None


def main(input_file: IO):
    input_lines = input_file.read().split('\n')
    graph = parse_input_to_graph(input_lines)
    path = find_path(graph, 'plaid violet', 'shiny gold')

    print(path)

    # paths = set()
    #
    # for start in graph.keys():
    #     if path := find_path(graph, start, 'shiny gold'):
    #         paths.add(tuple(path))
    #
    # paths.remove(('shiny gold',))
    #
    # print('The answer for Day 07 Part A :', len(paths))
