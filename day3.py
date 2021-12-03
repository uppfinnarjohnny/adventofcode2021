lines = list(open('input3.txt').readlines())

from collections import Counter

def part1(lines):
    counts = Counter()

    for line in lines:
        for digitIndex, digit in enumerate(line):
            if digit == '0':
                counts[digitIndex] -= 1
            if digit == '1':
                counts[digitIndex] += 1

    gamma = ''.join('1' if count > 0 else '0' for count in counts.values())
    epsilon = ''.join('0' if count > 0 else '1' for count in counts.values())
    
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    return gamma * epsilon

part1_answer = part1(lines)

assert part1_answer == 4147524

print("Day 3 part 1:", part1_answer)

def find_most_common_at_index(lines, index, on_draw):
    at_index = [l[index] for l in lines]
    item_counts = Counter(at_index).most_common()

    if len(item_counts) > 1 and item_counts[0][1] == item_counts[1][1]:
        return on_draw
    
    return item_counts[0][0]


def most_commonality(values, invert=False):
    index = 0
    
    while len(values) != 1:
        most_common_at_index = find_most_common_at_index(values, index, '1')

        if invert:
            most_common_at_index = '0' if most_common_at_index == '1' else '1'

        values = [l for l in values if l[index] == most_common_at_index]
        index += 1

    return values[0]


def part2(lines):
    oxygen = int(most_commonality(lines), 2)
    co2 = int(most_commonality(lines, invert=True), 2)

    return oxygen * co2


part2_answer = part2(lines)
assert part2_answer == 3570354

print("Day 3 part 2:", part2_answer)