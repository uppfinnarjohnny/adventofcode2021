from functools import partial

submarine_positions = [int(l) for l in open('input7.txt').read().split(',')]


def fuel_consumption_for_positions(positions, new_position, consumption_function):
    return sum(consumption_function(abs(p - new_position)) for p in positions)


part1_fuel_calculator = partial(fuel_consumption_for_positions, consumption_function=lambda d: d)
part2_fuel_calculator = partial(fuel_consumption_for_positions, consumption_function=lambda d: d * (d + 1) / 2)


def find_lowest_consumption(positions, fuel_calculator):
    lowest_consumption = lowest_consumption_position = None

    for new_position in range(min(submarine_positions), max(submarine_positions) + 1):
        consumption = fuel_calculator(positions, new_position)

        if lowest_consumption is None or consumption < lowest_consumption:
            lowest_consumption = consumption
            lowest_consumption_position = new_position
    
    return lowest_consumption, lowest_consumption_position


print("Day 7 part 1:", find_lowest_consumption(submarine_positions, part1_fuel_calculator))
print("Day 7 part 2:", find_lowest_consumption(submarine_positions, part2_fuel_calculator))
