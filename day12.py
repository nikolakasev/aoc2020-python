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


print(x, y, orientation)
print(x + y)
