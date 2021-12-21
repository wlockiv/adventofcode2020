from typing import IO, Tuple


class Ferry:
    _bearing: int

    def __init__(self, bearing: str = 'E'):
        self._bearing = Ferry.dir_to_degrees(bearing)
        self.north_position = 0
        self.east_position = 0

    def adjust_bearing(self, direction: str, degrees: int):
        """Rotates the ship based on current bearing and inputs."""
        if direction == 'L':
            self._bearing -= degrees
        elif direction == 'R':
            self._bearing += degrees

    def move(self, direction: str, units: int):
        """Moves the ship in a direction by a certain amount."""
        if (d := direction) == 'N':
            self.north_position += units
        elif d == 'S':
            self.north_position -= units
        elif d == 'E':
            self.east_position += units
        elif d == 'W':
            self.east_position -= units
        elif d == 'F':
            bearing = Ferry.degrees_to_dir(self._bearing)
            self.move(bearing, units)

    @staticmethod
    def parse_input(_input: str) -> Tuple[str, int]:
        direction, units = _input[0], int(_input[1:])
        return direction, units

    @staticmethod
    def dir_to_degrees(direction: str) -> int:
        dir_map = {'E': 0, 'S': 90, 'W': 180, 'N': 270}
        return dir_map[direction]

    @staticmethod
    def degrees_to_dir(degrees: int):
        dir_map_pos = {0: 'E', 90: 'S', 180: 'W', 270: 'N'}
        dir_map_neg = {0: 'E', -270: 'S', -180: 'W', -90: 'N'}

        if degrees >= 360:
            rounds = degrees // 360
            degrees = degrees - 360 * rounds
        if degrees <= -360:
            rounds = degrees // 360
            degrees = degrees + 360 * rounds

        if degrees > 0:
            return dir_map_pos[degrees]
        return dir_map_neg[degrees]


def main(input_file: IO):
    # Input Parsing
    input_lines = input_file.read().split('\n')

    ferry = Ferry()

    for vector in input_lines:
        _dir, units = Ferry.parse_input(vector)

        if _dir in 'NESWF':
            ferry.move(_dir, units)
        else:
            ferry.adjust_bearing(_dir, units)

    result = abs(ferry.east_position) + abs(ferry.north_position)
    print('The answer for Day 12 Part A :', result)
