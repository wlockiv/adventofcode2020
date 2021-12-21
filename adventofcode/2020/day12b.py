from typing import IO, Tuple


class Ferry:
    position = {'N': 0, 'E': 0}
    waypoint = {'N': 1, 'E': 10}

    def move_ferry(self, times: int):
        n_total = self.waypoint['N'] * times
        e_total = self.waypoint['E'] * times
        self.position['N'] += n_total
        self.position['E'] += e_total

    def move_waypoint(self, _dir: str, units: int):
        if _dir == 'N':
            self.waypoint['N'] += units
        elif _dir == 'S':
            self.waypoint['N'] -= units
        elif _dir == 'E':
            self.waypoint['E'] += units
        elif _dir == 'W':
            self.waypoint['E'] -= units

    def _rotate_l(self, times):
        for t in range(times):
            self.waypoint = {
                'N': self.waypoint['E'],
                'E': self.waypoint['N'] * -1
            }

    def _rotate_r(self, times):
        for t in range(times):
            self.waypoint = {
                'N': self.waypoint['E'] * -1,
                'E': self.waypoint['N']
            }

    def rotate_waypoint(self, _dir: str, degrees):
        times = degrees // 90
        if _dir == 'R':
            self._rotate_r(times)
        elif _dir == 'L':
            self._rotate_l(times)

    @staticmethod
    def parse_input(_input: str) -> Tuple[str, int]:
        direction, units = _input[0], int(_input[1:])
        return direction, units


def main(input_file: IO):
    # Input Parsing
    input_lines = input_file.read().split('\n')

    ferry = Ferry()

    for vector in input_lines:
        _dir, units = Ferry.parse_input(vector)

        if _dir in 'NESW':
            ferry.move_waypoint(_dir, units)
        elif _dir in 'LR':
            ferry.rotate_waypoint(_dir, units)
        elif _dir == 'F':
            ferry.move_ferry(units)

    result = abs(ferry.position['E']) + abs(ferry.position['N'])
    print('The answer for Day 12 Part B :', result)
