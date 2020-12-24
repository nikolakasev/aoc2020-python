import itertools

a = []
for line in open('day24.txt').read().split('\n'):
    a.append(line)


def lay_tiles(input):
    # the coordinate system is inspired (proudly copied) from https://www.redblobgames.com/grids/hexagons/
    # see the "double-width" horizontal layout that doubles the column values
    mozaic = dict()

    for line in input:
        # every line starts from the same reference tile
        row = 0
        column = 0

        i = 0
        while i < len(line):
            if line[i] == 'e':
                row += 2
            elif line[i] == 'w':
                row -= 2
            elif line[i] == 's' and line[i + 1] == 'e':
                row += 1
                column += 1
                i += 1
            elif line[i] == 's' and line[i + 1] == 'w':
                row -= 1
                column += 1
                i += 1
            elif line[i] == 'n' and line[i + 1] == 'e':
                row += 1
                column -= 1
                i += 1
            else:
                row -= 1
                column -= 1
                i += 1

            i += 1

        if (row, column) in mozaic.keys():
            # flip to the other side
            mozaic[(row, column)] = not mozaic[(row, column)]
        else:
            # flip to black
            mozaic[(row, column)] = True

    return mozaic


# star one
tile_floor = lay_tiles(a)
# how many tiles are still black?
print(sum(1 for _, v in tile_floor.items() if v))


def adjacent_tiles(tile):
    row = tile[0]
    column = tile[1]

    return [
        # east, west
        (row + 2, column), (row - 2, column),
        # se, sw
        (row + 1, column + 1), (row - 1, column + 1),
        # ne, nw
        (row + 1, column - 1), (row - 1, column - 1)]


def exhibit(mozaic, for_days):
    # due to the "double-width" nature of the coordinate system:
    # make sure to start with the adjacent tiles of the currently known ones
    min_row = min(t[0] for t in mozaic) - 2
    min_col = min(t[1] for t in mozaic) - 2
    max_row = max(t[0] for t in mozaic) + 2
    max_col = max(t[1] for t in mozaic) + 2

    for _ in range(for_days):
        new = set()
        for row in range(min_row, max_row):
            for column in range(min_col, max_col):
                tile = (row, column)

                adjacent_black_tiles = sum(1 for a in adjacent_tiles(
                    tile) if a in mozaic)

                # any black tile
                if tile in mozaic:
                    # with zero or more than two black tiles immediately adjacent to it is flipped to white
                    if adjacent_black_tiles == 0 or adjacent_black_tiles > 2:
                        pass
                    else:
                        # stays black
                        new.add(tile)
                # any white tile
                else:
                    # with exactly two black tiles adjacent to it
                    if adjacent_black_tiles == 2:
                        # is flipped to black
                        new.add(tile)

        # resize again accordingly
        min_row = min(t[0] for t in new) - 2
        min_col = min(t[1] for t in new) - 2
        max_row = max(t[0] for t in new) + 2
        max_col = max(t[1] for t in new) + 2

        mozaic = new.copy()

    return mozaic


# star two
print(len(exhibit(set(k for k, v in tile_floor.items() if v), 100)))
