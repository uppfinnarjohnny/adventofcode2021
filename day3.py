lines = list(open('input3.txt').readlines())

from collections import defaultdict, Counter

def part1(lines):
    counts = defaultdict(int)

    for line in lines:
        for digitIndex, digit in enumerate(line):
            if digit == '0':
                counts[digitIndex] -= 1
            if digit == '1':
                counts[digitIndex] += 1

    gamma = ""
    epsilon = ""

    for digitIndex in counts:
        count = counts[digitIndex]
        if count > 0:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    return gamma * epsilon


print("Day 3 part 1:", part1(lines))

def find_most_common_at_index(lines, index, on_draw):
    at_index = [l[index] for l in lines]
    result = Counter(at_index).most_common()

    if len(result) == 1:
        most_common = result[0][0]
    elif result[0][1] == result[1][1]:
        most_common = on_draw
    else:
        most_common = result[0][0]
    
    return most_common

def part2(lines):
    oxygen = co2 = 0

    oxygen_index = 0
    oxygen_filtered = lines

    while len(oxygen_filtered) != 1:
        most_common_at_index = find_most_common_at_index(oxygen_filtered, oxygen_index, '1')
        oxygen_filtered = [l for l in oxygen_filtered if l[oxygen_index] == most_common_at_index]
        oxygen_index += 1

    oxygen = int(oxygen_filtered[0], 2)
    
    co2_index = 0
    co2_filtered = lines
    
    while len(co2_filtered) != 1:
        least_common_at_index = '1' if find_most_common_at_index(co2_filtered, co2_index, '1') == '0' else '0'

        co2_filtered = [l for l in co2_filtered if l[co2_index] == least_common_at_index]
        co2_index += 1

    co2 = int(co2_filtered[0], 2)

    return oxygen * co2


print("Day 3 part 2:", part2(lines))