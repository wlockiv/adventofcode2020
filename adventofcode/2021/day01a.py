def main(input_file):
    input_list = [int(i) for i in input_file.read().splitlines()]

    count = 0
    for i in range(1, len(input_list)):
        last, current = input_list[i-1], input_list[i]

        count = count + 1 if current > last else count

    print('The answer for Day 01 Part A :', count)