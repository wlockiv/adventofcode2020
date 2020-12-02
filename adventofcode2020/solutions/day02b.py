with open('../../inputs/day02a.txt') as input_file:
    input_list = input_file.read().splitlines()

valid_password_count = 0

for i in input_list:
    positions, char, password = i.split(' ')
    positions = positions.split('-')
    char = char[:-1]

    char_a = password[int(positions[0]) - 1]
    char_b = password[int(positions[1]) - 1]

    if char_a == char != char_b:
        valid_password_count += 1
    elif char_a != char == char_b:
        valid_password_count += 1

print('The answer for Day 02 Part B:', valid_password_count)
