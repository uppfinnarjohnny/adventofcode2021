values = list(map(int, open('input1.txt').readlines()))

def count_increases(v):
    return sum(map(lambda vs: int(vs[0] > vs[1]), zip(v + [v[-1]], [v[0]] + v)))

def triplet_sums(v):
    return [sum(vs) for vs in zip(v, v[1:], v[2:])]

print("Day 1 part 1:", count_increases(values))
print("Day 1 part 2:", count_increases(triplet_sums(values)))
