from math import prod, sqrt
import itertools

a = []
for line in open('s.txt').read().split('\n\n'):
    a.append(line)


def rotate_90_clockwise(tile):
    # rotate 90 degrees, 180 is then x2, 270 is x3
    return list(map(lambda a: "".join(a), zip(*tile[::-1])))


def print_tile(tile):
    for i in tile:
        print(i)


def flip_down(tile):
    return tile[::-1]


def borders(tile):
    # extract the borders of a tile
    item_length = len(tile[0])

    up = tile[0]
    down = tile[-1]
    left = ""
    right = ""

    for i in range(0, len(tile)):
        left = tile[i][0] + left
        right = right + tile[i][item_length - 1]

    return [up, down, left, right]


def contents(tile):
    # extract the contents of a tile without the borders
    c = []
    item_length = len(tile[0])

    for i in range(1, len(tile) - 1):
        c.append(tile[i][1:item_length-1])

    return c


def tiles_and_borders(string):
    s = string.split('\n')

    return (
        int(s[0][5:9]), borders(s[1:11]) +
        list(map(lambda b: b[::-1], borders(s[1:11])))
    )


tiles = list(map(tiles_and_borders, a))

# a corner tile always has two of it's borders not connected
# find all tiles which still have 4 borders left (two original + two transformed) when substracting all other known borders
corner_tiles = list(t[0] for t in tiles if len(
    set(t[1]) - set(itertools.chain(*[r[1] for r in tiles if t[0] != r[0]]))) == 4)

print(corner_tiles, prod(corner_tiles))

pieces_per_row = int(sqrt(len(a)))


# for a tile, return operation, borders and contents without the borders - lru_cache it, 8 distinct contents per tile, unique borders must be 8 in total
# O[\.#]{5}O[\.#]{4}OO[\.#]{4}OO[\.#]{4}OOO[\.#]{5}O[\.#]{2}O[\.#]{2}O[\.#]{2}O[\.#]{2}O[\.#]{2}O
# search for monster with r'#[\.#]{5}#[\.#]{4}##[\.#]{4}##[\.#]{4}###[\.#]{5}#[\.#]{2}#[\.#]{2}#[\.#]{2}#[\.#]{2}#[\.#]{2}#'

# start with the corner tile (original), pick right= and under= by finding the set intersection with all other tiles' borders, there must be 4 matches
# for each other not connected yet, find where it's left matches right= until 12 are connected (add to set of connected)
# next row, first match where top mathes under=, set new under=, repeat until 12 are connected (add to set of connected)
# finish when all 144 are connected

# turn the array into a single image
# rotate and flip, turn into a single string until one or more regex matches are found, count the total amount of # and substract monsters*15
