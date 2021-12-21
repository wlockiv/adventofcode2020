
windows = [
    (0, 1, 2),
    (1, 2, 3),
    (2, 3, 4),
    (3, 4, 5)
]

offset = 4

def main(input_file):
    input_list = [int(i) for i in input_file.read().splitlines()]

    window_sums = []
    current_offset = 0
    in_range = True
    while in_range:
        for window in windows:
            try:
                current_window = [i + current_offset for i in window]
                window_sum = sum([input_list[i] for i in current_window])
                window_sums.append(window_sum)
            except IndexError:
                # This didn't finish, so we don't want it to add
                in_range = False
        current_offset = current_offset + offset


    count = 0
    for i in range(1, len(window_sums)):
        last, current = window_sums[i - 1], window_sums[i]

        count = count + 1 if current > last else count

    print('The answer for Day 01 Part B :', count)