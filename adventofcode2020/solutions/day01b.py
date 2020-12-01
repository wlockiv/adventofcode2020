with open('../../inputs/day01a.txt') as input_file:
    input_list = input_file.read().splitlines()

# Sort the input array
input_list = [int(i) for i in input_list]

sum_equals_2020 = (0, 0, 0)
it = 0

for idx, i in enumerate(input_list):
    for j in input_list[idx + 1:]:
        for k in input_list[idx + 2:]:
            it += 1
            if sum((i, j, k)) == 2020:
                sum_equals_2020 = (i, j, k)
                break

print('Iterations', it)
print('The following numbers sum to 2020:', sum_equals_2020)
print('The answer for today is', sum_equals_2020[0] * sum_equals_2020[1] * sum_equals_2020[2])
