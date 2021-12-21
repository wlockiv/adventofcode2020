def main(input_file):
    input_list = input_file.read().splitlines()

    valid_password_count = 0

    for i in input_list:
        minmax, char, password = i.split(' ')
        minmax = minmax.split('-')
        char = char[:-1]

        if int(minmax[0]) <= password.count(char) <= int(minmax[1]):
            valid_password_count += 1

    print('The answer for Day 02 Part A :', valid_password_count)
