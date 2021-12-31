from typing import IO, List, Tuple, Set
from adventofcode.util import print_solution
import re


def main(input_file: IO):
    all_points, raw_folds = input_file.read().split('\n\n')

    points: Set[Tuple[int, int]] = set()
    for raw_point in all_points.splitlines():
        x, y = raw_point.split(',')
        points.add((int(x), int(y)))

    raw_folds = raw_folds.splitlines()

    folds: List[Tuple[str, int]] = []
    for f in raw_folds:
        match = re.findall(r'[xy]=\d+$', f)
        axis, number = match[0].split('=')
        folds.append((axis, int(number)))

    for fold in folds:
        for point in points.copy():
            x, y = point
            if fold[0] == 'x' and fold[1] < point[0]:
                translation = (x - fold[1]) * 2
                points.remove(point)
                points.add((x-translation, y))
            if fold[0] == 'y' and fold[1] < point[1]:
                translation = (y - fold[1]) * 2
                points.remove(point)
                points.add((x, y-translation))

    xs, ys = list(zip(*list(points)))
    x_max = max(xs) + 1
    y_max = max(ys) + 1

    display = []
    for y in range(y_max):
        row = [' ']*(x_max)
        for x in range(x_max):
            if (x, y) in points:
                row[x] = '#'
        display.append('\t' + ''.join(row))

    print_solution('\n' + '\n'.join(display))
