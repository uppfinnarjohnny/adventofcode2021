lines = list(open('input3.txt').readlines())

from collections import defaultdict

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