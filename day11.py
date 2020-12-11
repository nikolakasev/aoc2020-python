from functools import lru_cache

a = []
for line in open('day11.txt').read().split('\n'):
    a.append(list(line))


def adjacent_seats(x, y, max_x, max_y):
    return ((x, y) for x, y in [(x + 1, y), (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y), (x - 1, y - 1), (x, y - 1), (x + 1, y - 1)] if x >= 0 and y >= 0 and x <= max_x and y <= max_y)


def step(layout):
    max_x = len(layout[0])
    max_y = len(layout)
    new_a = []
    for y in range(max_y):
        new_row = []
        for x in range(max_x):
            seats = adjacent_seats(x, y, max_x - 1, max_y - 1)
            if layout[y][x] == "L" and len(list(filter(lambda s: layout[s[1]][s[0]] == "#", seats))) == 0:
                new_row.append('#')
            elif layout[y][x] == "#" and len(list(filter(lambda s: layout[s[1]][s[0]] == "#", seats))) >= 4:
                new_row.append('L')
            else:
                new_row.append(layout[y][x])

        new_a.append(new_row)

    return new_a


def layout_to_str(layout):
    return "".join(map(lambda row: "".join(row), layout))


known = set()
count = 0

b = a.copy()
while True:
    b = step(b)
    if layout_to_str(b) in known:
        break
    else:
        known.add(layout_to_str(b))
        count += 1

print(len(list(filter(lambda seat: seat == "#", layout_to_str(b)))))


@lru_cache(maxsize=None)
def extra_sight(x, y, max_x, max_y):
    sight = [list((i, y) for i in range(x + 1, max_x))] + \
        [list((i, y) for i in range(x - 1, -1, -1))] + \
        [list((x, i) for i in range(y + 1, max_y))] + \
        [list((x, i) for i in range(y - 1, -1, -1))] + \
        [list((i, y + (x - i)) for i in range(x + 1, max_x))] + \
        [list((i, y - (x - i)) for i in range(x + 1, max_x))] + \
        [list((i, y + (x - i)) for i in range(x - 1, -1, -1))] + \
        [list((i, y - (x - i)) for i in range(x - 1, -1, -1))]

    return list(map(lambda s: list(filter(lambda p: p[0] >= 0 and p[0] < max_x and p[1] >= 0 and p[1] < max_y, s)), sight))


def step2(layout):
    max_x = len(layout[0])
    max_y = len(layout)
    new_a = []
    for y in range(max_y):
        new_row = []
        for x in range(max_x):
            lines = extra_sight(x, y, max_x, max_y)
            if layout[y][x] == "L" and sum(map(lambda l: see_occupied(l, layout), lines)) == 0:
                new_row.append('#')
            elif layout[y][x] == "#" and sum(map(lambda l: see_occupied(l, layout), lines)) >= 5:
                new_row.append('L')
            else:
                new_row.append(layout[y][x])

        new_a.append(new_row)

    return new_a


def see_occupied(line, layout):
    count = 0
    for seat in line:
        if layout[seat[1]][seat[0]] == ".":
            continue
        elif layout[seat[1]][seat[0]] == "L":
            break
        else:
            count += 1
            break

    return count


known = set()
count = 0

b = a.copy()
while True:
    b = step2(b)
    if layout_to_str(b) in known:
        break
    else:
        known.add(layout_to_str(b))
        count += 1

print(len(list(filter(lambda seat: seat == "#", layout_to_str(b)))))
