values = list(map(int, open('input1.txt').readlines()))

def count_increases(values):
    return sum(int(pair[0] > pair[1]) for pair in zip(values + [values[-1]], [values[0]] + values))

def triplet_sums(values):
    return [sum(triplet) for triplet in zip(values, values[1:], values[2:])]

print("Day 1 part 1:", count_increases(values))
print("Day 1 part 2:", count_increases(triplet_sums(values)))
