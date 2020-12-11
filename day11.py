a = []
for line in open('day11.txt').read().split('\n'):
    a.append(list(line))


def adjacent_seats(x, y, max_x, max_y):
    return ((x, y) for x, y in [(x + 1, y), (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y), (x - 1, y - 1), (x, y - 1), (x + 1, y - 1)] if x >= 0 and y >= 0 and x <= max_x and y <= max_y)


def step(a):
    max_x = len(a[0])
    max_y = len(a)
    new_a = []
    for y in range(max_y):
        new_row = []
        for x in range(max_x):
            seats = adjacent_seats(x, y, max_x - 1, max_y - 1)
            if a[y][x] == "L" and len(list(filter(lambda s: a[s[1]][s[0]] == "#", seats))) == 0:
                new_row.append('#')
            elif a[y][x] == "#" and len(list(filter(lambda s: a[s[1]][s[0]] == "#", seats))) >= 4:
                new_row.append('L')
            else:
                new_row.append(a[y][x])

        new_a.append(new_row)

    return new_a


def layout(a):
    return "".join(map(lambda row: "".join(row), a))


visited = set()
count = 0

while True:
    a = step(a)
    if layout(a) in visited:
        break
    else:
        visited.add(layout(a))
        count += 1

print(count)
print(len(list(filter(lambda seat: seat == "#", layout(a)))))
