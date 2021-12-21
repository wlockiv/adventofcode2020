
def main(input_file):
    input_list = input_file.read().splitlines()

    horizontal, vertical = 0, 0

    for vector in input_list:
        direction, magnitude = vector.split(" ")
        magnitude = int(magnitude)

        if direction == 'forward':
            horizontal = horizontal + magnitude
        elif direction == 'up':
            vertical = vertical - magnitude
        else:
            vertical = vertical + magnitude

    print('The answer for Day 02 Part A :', horizontal * vertical)
