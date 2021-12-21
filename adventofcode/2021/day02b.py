
def main(input_file):
    input_list = input_file.read().splitlines()

    horizontal, vertical, aim = 0, 0, 0

    for vector in input_list:
        direction, magnitude = vector.split(" ")
        magnitude = int(magnitude)

        if direction == 'forward':
            horizontal = horizontal + magnitude
            vertical = vertical + (aim * magnitude)
        elif direction == 'up':
            aim = aim - magnitude
        else:
            aim = aim + magnitude

    print('The answer for Day 02 Part B :', horizontal * vertical)
