from itertools import product

input = []

y = 0
z = 0
w = 0

for line in open('day17.txt').read().split('\n'):
    for (x, cube) in enumerate(list(line)):
        if cube == '#':
            input.append((x, y, z, w))
    y += 1

# think of each tuple as a function that is being applied with the coordinates as input
# for example (-1, 1, 0) applied to x=-1,y=3,z=2 equals x=-2,y=4,z=2
neighbours = set(product([-1, 0, 1], repeat=4)) - {(0, 0, 0, 0)}


def cycle(space, bounds_x, bounds_y, bounds_z, bounds_w):
    new_space = []

    for x in range(bounds_x[0], bounds_x[1]):
        for y in range(bounds_y[0], bounds_y[1]):
            for z in range(bounds_z[0], bounds_z[1]):
                for w in range(bounds_w[0], bounds_w[1]):
                    active = active_neighbours(space, x, y, z, w)

                    # the cube is active
                    if (x, y, z, w) in space:
                        # keep active if 2 or 3 neighbours are also active
                        if active == 2 or active == 3:
                            new_space.append((x, y, z, w))
                        else:
                            # deactivate it otherwise
                            continue
                    elif active == 3:
                        # active a new cube because it has exactly three active neighbours
                        new_space.append((x, y, z, w))

    return new_space


def active_neighbours(space, x, y, z, w):
    return sum(1 for n in neighbours if (x + n[0], y + n[1], z + n[2], w + n[3]) in space)


min_x = 0
max_x = 8
min_y = 0
max_y = 8
min_z = 0
max_z = 1
min_w = 0
max_w = 1

space = input
for c in range(6):
    # very naive, expand the boundaries on each cycle
    # it would be more efficient to expand the boundary only when one or more cubes are activated
    # and shrink if all cubes in a plane are deactivated
    min_x -= 1
    min_y -= 1
    min_z -= 1
    min_w -= 1

    max_x += 1
    max_y += 1
    max_z += 1
    max_w += 1

    space = cycle(space, (min_x, max_x), (min_y, max_y),
                  (min_z, max_z), (min_w, max_w))
    print(f"{len(space)} cubes in cycle {c}")
