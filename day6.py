from collections import Counter

fish_timers = Counter(int(l) for l in open('input6.txt').read().split(','))

def next_day(timers_today):
    timers_tomorrow = Counter()

    for count in range(8):
        timers_tomorrow[count] = timers_today[count + 1]

    timers_tomorrow[6] += timers_today[0]
    timers_tomorrow[8] = timers_today[0]

    return timers_tomorrow


def simulate(timers, days):
    for _ in range(days):
        timers = next_day(timers)

    return sum(timers.values())

print('Day 6 part 1', simulate(fish_timers, 80))
print('Day 6 part 2', simulate(fish_timers, 256))