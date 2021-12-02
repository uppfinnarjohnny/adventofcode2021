commands = list(map(lambda l: l.strip(), open('input2.txt').readlines()))

def part1(commands):
    horizontal_position = 0
    depth = 0

    for command in commands:
        command_name, amount = command.split(' ')
        amount = int(amount)

        if command_name == 'forward':
            horizontal_position += amount
        
        if command_name == 'down':
            depth += amount
        
        if command_name == 'up':
            depth -= amount

    return horizontal_position * depth

def part2(commands):
    horizontal_position = 0
    depth = 0
    aim = 0

    for command in commands:
        command_name, amount = command.split(' ')
        amount = int(amount)

        if command_name == 'forward':
            horizontal_position += amount
            depth += aim * amount
        
        if command_name == 'down':
            aim += amount
        
        if command_name == 'up':
            aim -= amount

    return horizontal_position * depth

print("Day 2 part 1:", part1(commands))
print("Day 2 part 2:", part2(commands))