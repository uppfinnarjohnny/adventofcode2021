submarine_positions = [int(l) for l in open('input7.txt').read().split(',')]

def part2_fuel(distance):
    return distance * (distance + 1) / 2

def fuel_consumption_for_positions(positions, new_position):
    return sum(abs(p - new_position) for p in positions)


def part2_fuel_consumption_for_positions(positions, new_position):
    return sum(part2_fuel(abs(p - new_position)) for p in positions)


def find_lowest_consumption(positions):
    lowest_consumption_position = None
    lowest_consumption = None

    for new_position in range(min(submarine_positions), max(submarine_positions) + 1):
        consumption = fuel_consumption_for_positions(positions, new_position)

        if lowest_consumption is None or consumption < lowest_consumption:
            lowest_consumption = consumption
            lowest_consumption_position = new_position
    
    return lowest_consumption, lowest_consumption_position


def part2_find_lowest_consumption(positions):
    lowest_consumption_position = None
    lowest_consumption = None

    for new_position in range(min(submarine_positions), max(submarine_positions) + 1):
        consumption = part2_fuel_consumption_for_positions(positions, new_position)

        if lowest_consumption is None or consumption < lowest_consumption:
            lowest_consumption = consumption
            lowest_consumption_position = new_position
    
    return lowest_consumption, lowest_consumption_position


assert fuel_consumption_for_positions([16,1,2,0,4,2,7,1,2,14], 2) == 37
print("Day 7 part 1:", find_lowest_consumption(submarine_positions))
print("Day 7 part 2:", part2_find_lowest_consumption(submarine_positions))
