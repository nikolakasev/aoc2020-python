import itertools

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
    tree[tile] = (False, dict())
    return tile


def flip_tile(tree, tile):
    print(f"flipped {tile} from {tree[tile][0]} to {not tree[tile][0]}")
    tree[tile] = (not tree[tile][0], tree[tile][1])
    return tile


def next_tile_num(tree):
    all_tiles = set(itertools.chain(*[v[1].values() for v in tree.values()]))

    return max([1] if all_tiles == set() else all_tiles) + 1


all_directions = set(['e', 'w', 'ne', 'se', 'nw', 'sw'])


def add_neighbours(tree, tile):
    print(f"to add {all_directions - set(tree[tile][1].keys())} to {tile}")
    for d in sorted(all_directions - set(tree[tile][1].keys())):
        neighbour = next_tile_num(tree)
        print(f"added {neighbour} on {d} to {tile}")
        add_tile(tree, neighbour)
        add_neighbour(tree, tile, d, neighbour)
        add_neighbour(tree, neighbour, opposite(d), tile)

    fully_link_neighbours(tree, tile)


def fully_link_neighbours(tree, tile):
    neighbours = tree[tile][1]

    for d, n in neighbours.items():
        if d == 'e':
            add_neighbour(tree, n, 'nw', neighbours['ne'])
            add_neighbour(tree, n, 'sw', neighbours['se'])
        elif d == 'w':
            add_neighbour(tree, n, 'ne', neighbours['nw'])
            add_neighbour(tree, n, 'se', neighbours['sw'])
        elif d == 'ne':
            add_neighbour(tree, n, 'se', neighbours['e'])
            add_neighbour(tree, n, 'w', neighbours['nw'])
        elif d == 'nw':
            add_neighbour(tree, n, 'sw', neighbours['w'])
            add_neighbour(tree, n, 'e', neighbours['ne'])
        elif d == 'sw':
            add_neighbour(tree, n, 'nw', neighbours['w'])
            add_neighbour(tree, n, 'e', neighbours['se'])
        elif d == 'se':
            add_neighbour(tree, n, 'ne', neighbours['e'])
            add_neighbour(tree, n, 'w', neighbours['sw'])


def build_tree(input):
    tree = dict()
    tile = 1
    neighbour = None
    direction = None

    add_tile(tree, tile)
    add_neighbours(tree, tile)

    for line in input:
        directions = []
        i = 0
        # every line starts from the same reference tile
        tile = 1
        while i < len(line):
            if line[i] == 'e':
                direction = 'e'
                # print(f"{direction}")
            elif line[i] == 'w':
                direction = 'w'
                # print(f"{direction}")
            elif line[i] == 's' and line[i + 1] == 'e':
                i += 1
                direction = 'se'
                # print(f"{direction}")
            elif line[i] == 's' and line[i + 1] == 'w':
                i += 1
                direction = 'sw'
                # print(f"{direction}")
            elif line[i] == 'n' and line[i + 1] == 'e':
                i += 1
                direction = 'ne'
                # print(f"{direction}")
            elif line[i] == 'n' and line[i + 1] == 'w':
                i += 1
                direction = 'nw'
            else:
                print(f"don't know!")
                # print(f"{direction}")

            neighbour = find_neighbour(tree, tile, direction)
            add_neighbours(tree, neighbour)

            print(f"moved from {tile} to {neighbour}")
            tile = neighbour

            i += 1
            directions.append(direction)

        flip_tile(tree, tile)
        print(f"{line} {directions} {tree}")

    return tree


tree = build_tree(a)
print(tree)
print(sum(1 for _, v in tree.items() if v[0]))
print(next_tile_num(tree))
# # neighbours = [('ne', 2), ('w', 3)]
# neighbours = []
# sample = dict()
# # sample[1] = (False, dict((k, v) for k, v in neighbours))


# add_tile(sample, 1)
# add_neighbours(sample, 1)
# # fully_link_neighbours(sample, 1)

# print(sample)


# print(max(set(itertools.chain(*[v[1].values() for v in sample.values()]))) + 1)
#
# print(sample)
# print(next_tile_num(sample))

# print(sample)

# print(find_neighbour(sample, 1, 'ne'))

# print(add_neighbour(sample, 0, 'sw', 4))
# print(sample)

# flip_tile(sample, 0)

# print(sample)

# print(next_tile_num(sample))
