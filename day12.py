a = []
for line in open('day12.txt').read().split('\n'):
    a.append(line)


def rotate(current, direction, num):
    if current == 'N':
        if direction == 'R':
            if num == 90:
                return 'E'
            elif num == 180:
                return 'S'
            else:
                return 'W'
        else:
            if num == 90:
                return 'W'
            elif num == 180:
                return 'S'
            else:
                return 'E'
    elif current == 'S':
        if direction == 'R':
            if num == 90:
                return 'W'
            elif num == 180:
                return 'N'
            else:
                return 'E'
        else:
            if num == 90:
                return 'E'
            elif num == 180:
                return 'N'
            else:
                return 'W'
    elif current == 'E':
        if direction == 'R':
            if num == 90:
                return 'S'
            elif num == 180:
                return 'W'
            else:
                return 'N'
        else:
            if num == 90:
                return 'N'
            elif num == 180:
                return 'W'
            else:
                return 'S'
    # west
    else:
        if direction == 'R':
            if num == 90:
                return 'N'
            elif num == 180:
                return 'E'
            else:
                return 'S'
        else:
            if num == 90:
                return 'S'
            elif num == 180:
                return 'E'
            else:
                return 'N'


def move(x, y, direction, num):
    if direction == 'E':
        return (x + num, y)
    elif direction == 'W':
        return (x - num, y)
    elif direction == 'N':
        return (x, y - num)
    elif direction == 'S':
        return (x, y + num)


orientation = 'E'
x = 0
y = 0

for i in range(len(a)):
    op = a[i][:1]
    num = int(a[i][1:])

    if op == 'F':
        x, y = move(x, y, orientation, num)
    elif op in ['E', 'W', 'N', 'S']:
        x, y = move(x, y, op, num)
    elif op in ['R', 'L']:
        orientation = rotate(orientation, op, num)
    else:
        print(f"don't know instruction {op} {num}")


print(x + y)

# East and South go plus, North and West go negative
waypoint = (10, -1)


def move_waypoint(w, direction, num):
    if direction == 'E':
        return (w[0] + num, w[1])
    elif direction == 'W':
        return (w[0] - num, w[1])
    elif direction == 'N':
        return (w[0], w[1] - num)
    else:
        # must be South
        return (w[0], w[1] + num)


def move_to_waypoint(x, y, w, times):
    return (x + w[0] * times, y + w[1] * times)


def rotate_waypoint(w, direction, degrees):
    if (direction == 'R' and degrees == 90) or (direction == 'L' and degrees == 270):
        return (-w[1], w[0])
    elif (direction == 'R' and degrees == 180) or (direction == 'L' and degrees == 180):
        return (-w[0], -w[1])
    else:
        # R 270 or L 90
        return (w[1], -w[0])


x = 0
y = 0
for i in range(len(a)):
    op = a[i][:1]
    num = int(a[i][1:])

    if op == 'F':
        x, y = move_to_waypoint(x, y, waypoint, num)
    elif op in ['E', 'W', 'N', 'S']:
        waypoint = move_waypoint(waypoint, op, num)
    elif op in ['R', 'L']:
        waypoint = rotate_waypoint(waypoint, op, num)
    else:
        print(f"don't know instruction {op} {num}")

print(abs(x) + abs(y))
