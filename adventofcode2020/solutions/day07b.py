from typing import IO


def parse_input_to_graph(input_lines):
    graph = {}
    for line in input_lines:
        top_color, contents = line.split('bags contain')
        top_color = top_color.strip()

        if 'no other' in contents:
            graph[top_color] = []
            continue

        inner_bags = contents.replace('.', '').replace('bags', '').replace('bag', '')
        inner_bags = inner_bags.split(',')

        graph[top_color] = [b.strip() for b in inner_bags]

    return graph


def get_bag(graph, start_color):
    total = 1
    if len(graph[start_color]) == 0:
        return 1
    for color in (graph[start_color]):
        total += int(color[:2].strip()) * get_bag(graph, color[2:])

    return total


def main(input_file: IO):
    input_lines = input_file.read().split('\n')
    graph = parse_input_to_graph(input_lines)

    print('The answer for Day 07 Part B :', get_bag(graph, 'shiny gold') - 1)
