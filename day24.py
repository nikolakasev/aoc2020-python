a = []
for line in open('s.txt').read().split('\n'):
    a.append(line)

print(a)


def opposite(direction):
    if direction == 'e':
        return 'w'
    elif direction == 'w':
        return 'e'
    elif direction == 'sw':
        return 'ne'
    elif direction == 'se':
        return 'nw'
    elif direction == 'nw':
        return 'se'
    elif direction == 'ne':
        return 'sw'


def find_neighbour(tree, tile, direction):
    if tile in tree and direction in tree[tile][1]:
        return tree[tile][1][direction]


def add_neighbour(tree, tile, direction, neighbour):
    neighbours = tree[tile][1]
    neighbours[direction] = neighbour
    tree[tile] = (tree[tile][0], neighbours)

    return neighbour


def add_tile(tree, tile):
    tree[tile] = (True, dict())
    return tile


def flip_tile(tree, tile):
    tree[tile] = (not tree[tile][0], tree[tile][1])
    return tile


# def get_tile_color(tree, tile):
#     return tree[tile][0]


def next_tile_num(tree):
    return max(tree.keys()) + 1


all_directions = set(['e', 'w', 'ne', 'se', 'nw', 'sw'])


def add_neighbours(tree, tile):
    neighbour = next_tile_num(tree)
    for d in all_directions - set(tree[tile][1].keys()):
        add_tile(tree, neighbour)
        add_neighbour(tree, tile, d, neighbour)
        add_neighbour(tree, neighbour, opposite(d), tile)
        neighbour += 1
    fully_link_neighbours(tree, tile)


def fully_link_neighbours(tree, tile):
    print(f"{tree[tile][1]}")
    for d, n in tree[tile][1].items():
        if d == 'e':
            add_neighbour(tree, n, 'nw', tree[tile][1]['ne'])
            add_neighbour(tree, n, 'sw', tree[tile][1]['se'])
        elif d == 'w':
            add_neighbour(tree, n, 'ne', tree[tile][1]['nw'])
            add_neighbour(tree, n, 'se', tree[tile][1]['sw'])
        elif d == 'ne':
            add_neighbour(tree, n, 'se', tree[tile][1]['e'])
            add_neighbour(tree, n, 'w', tree[tile][1]['nw'])
        elif d == 'nw':
            add_neighbour(tree, n, 'sw', tree[tile][1]['w'])
            add_neighbour(tree, n, 'e', tree[tile][1]['ne'])
        elif d == 'sw':
            add_neighbour(tree, n, 'nw', tree[tile][1]['w'])
            add_neighbour(tree, n, 'e', tree[tile][1]['se'])
        elif d == 'se':
            add_neighbour(tree, n, 'ne', tree[tile][1]['e'])
            add_neighbour(tree, n, 'w', tree[tile][1]['sw'])


def build_tree(input):
    tree = dict()
    tile = 1
    neighbour = None
    direction = None

    add_tile(tree, tile)

    for line in input:
        i = 0
        while i < len(line):
            if line[i] == 'e':
                direction = 'e'
            elif line[i] == 'w':
                direction = 'w'
            elif line[i] == 's' and line[i + 1] == 'e':
                i += 1
                direction = 'se'
            elif line[i] == 's' and line[i + 1] == 'w':
                i += 1
                direction = 'sw'
            elif line[i] == 'n' and line[i + 1] == 'e':
                i += 1
                direction = 'ne'
            else:
                i += 1
                direction = 'nw'

            neighbour = find_neighbour(tree, tile, direction)
            if not neighbour:
                neighbour = next_tile_num(tree)
                add_tile(tree, neighbour)

            add_neighbour(tree, tile, direction, neighbour)
            add_neighbour(tree, neighbour, opposite(direction), tile)

            tile = neighbour

            i += 1

        flip_tile(tree, neighbour)

    return tree


# print(build_tree(a))

# neighbours = [('ne', 2), ('w', 3)]
neighbours = []
sample = dict()
sample[1] = (True, dict((k, v) for k, v in neighbours))

add_neighbours(sample, 1)

print(sample)

# print(sample)

# print(find_neighbour(sample, 0, 'ne'))

# print(add_neighbour(sample, 0, 'sw', 4))
# print(sample)

# flip_tile(sample, 0)

# print(sample)

# print(next_tile_num(sample))
