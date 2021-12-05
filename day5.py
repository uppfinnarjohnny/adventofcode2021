from collections import namedtuple, defaultdict

Line = namedtuple('Line', ['start', 'end'])
Point = namedtuple('Point', ['x', 'y'])

def parse_line(line):
    first = line.strip().split(' -> ')
    second = [first[0].split(','), first[1].split(',')]
    third = [Point(int(second[0][0]), int(second[0][1])), Point(int(second[1][0]), int(second[1][1]))]
    return Line(start=third[0], end=third[1])


def ints_from_to(start, end):
    step = -1 if end < start else 1
    end = end + 1 if end > start else end -1 
    return range(start, end, step)


def get_intermediary_points(line, include_diagonal=False):
    delta_x = line.start.x - line.end.x
    delta_y = line.start.y - line.end.y

    if delta_x == 0:
        return [Point(line.start.x, y) for y in ints_from_to(line.start.y, line.end.y)]
    
    if delta_y == 0:
        return [Point(x, line.start.y) for x in ints_from_to(line.start.x, line.end.x)]

    if abs(delta_x) == abs(delta_y):
        if include_diagonal:
            return [Point(x, y) for x, y in zip(ints_from_to(line.start.x, line.end.x), ints_from_to(line.start.y, line.end.y))]

    return []

lines = [parse_line(l) for l in open('input5.txt').readlines()]

def count_overlapping_points(lines, include_diagonals=False):
    point_counts = defaultdict(int)
    
    for line in lines:
        for point in get_intermediary_points(line, include_diagonals):
            point_counts[point] += 1

    return len(list(point for point, count in point_counts.items() if count > 1))


print('Day 5 part 1:', count_overlapping_points(lines))
print('Day 5 part 2:', count_overlapping_points(lines, include_diagonals=True))
