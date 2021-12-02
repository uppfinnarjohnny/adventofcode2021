lines = [l.strip() for l in open('input2.txt').readlines()]
pairs = [l.split(' ') for l in lines]
commands = [(p[0], int(p[1])) for p in pairs]


def part1(commands):
    horizontal_position = sum(a for c, a in commands if c == 'forward')
    depth = sum(a for c, a in commands if c == 'down')
    depth -= sum(a for c, a in commands if c == 'up')

    return horizontal_position * depth


def part2(commands):
    horizontal_position = depth = aim = 0

    for command, amount in commands:
        if command == 'forward':
            horizontal_position += amount
            depth += aim * amount
        
        if command == 'down':
            aim += amount
        
        if command == 'up':
            aim -= amount

    return horizontal_position * depth


print("Day 2 part 1:", part1(commands))
print("Day 2 part 2:", part2(commands))