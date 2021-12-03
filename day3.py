from collections import Counter

def string_to_booleans(string):
    return [character == '1' for character in string]


def booleans_to_int(booleans):
    return int(''.join('1' if boolean else '0' for boolean in booleans), 2)


lines = [string_to_booleans(l.strip()) for l in open('input3.txt').readlines()]


def part1(lines):
    counts = Counter()

    for line in lines:
        for index, boolean in enumerate(line):
            counts[index] = counts[index] + 1 if boolean else counts[index] - 1
            
    gamma = booleans_to_int(count > 0 for count in counts.values())
    epsilon = booleans_to_int(count < 0 for count in counts.values())

    return gamma * epsilon


def find_most_common_at_index(lines, index, on_draw):
    at_index = [l[index] for l in lines]
    item_counts = Counter(at_index).most_common()

    if len(item_counts) > 1 and item_counts[0][1] == item_counts[1][1]:
        return on_draw
    
    return item_counts[0][0]


def most_commonality(values, invert=False):
    index = 0
    
    while len(values) != 1:
        most_common_at_index = find_most_common_at_index(values, index, on_draw=True)

        if invert:
            most_common_at_index = not most_common_at_index

        values = [l for l in values if l[index] == most_common_at_index]
        index += 1

    return values[0]


def part2(lines):
    oxygen = booleans_to_int(most_commonality(lines))
    co2 = booleans_to_int(most_commonality(lines, invert=True))

    return oxygen * co2


print("Day 3 part 1:", part1(lines))
print("Day 3 part 2:", part2(lines))