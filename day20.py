
from math import prod, sqrt
import itertools
import re

a = []
for line in open('day20.txt').read().split('\n\n'):
    a.append(line)


def rotate_90(tile):
    # rotate 90 degrees clockwise, 180 is then x2, 270 is x3
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
        left = left + tile[i][0]
        right = right + tile[i][item_length - 1]

    return [up, down, left, right]


def contents(tile):
    # extract the contents of a tile without the borders
    c = []
    item_length = len(tile[0])

    for i in range(1, len(tile) - 1):
        c.append(tile[i][1:item_length-1])

    return c


def tiles_borders_only(string):
    s = string.split('\n')

    return (
        int(s[0][5:9]), borders(s[1:11]) +
        list(map(lambda b: b[::-1], borders(s[1:11])))
    )


def transformations(tile):
    # for a tile, find all eight possible transformations
    # rotate 90 degrees clockwise
    r90 = rotate_90(tile)
    r180 = rotate_90(rotate_90(tile))
    r270 = rotate_90(rotate_90(rotate_90(tile)))

    # flip and rotate as well
    flipped = flip_down(tile)
    f90 = rotate_90(flipped)
    f180 = rotate_90(rotate_90(flipped))
    f270 = rotate_90(rotate_90(rotate_90(flipped)))

    return [(tile, borders(tile)),
            (r90, borders(r90)),
            (r180, borders(r180)),
            (r270, borders(r270)),
            (flipped, borders(flipped)),
            (f90, borders(f90)),
            (f180, borders(f180)),
            (f270, borders(f270))]


t = a[1].split('\n')[1:11]


def tiles_content(string):
    s = string.split('\n')
    return (int(s[0][5:9]), s[1:11])


tiles_with_borders = list(map(tiles_borders_only, a))


# a corner tile always has two of it's borders not connected
# find all tiles which still have 4 borders left (two original + two transformed) when substracting all other known borders
corner_tiles = list(t[0] for t in tiles_with_borders if len(
    set(t[1]) - set(itertools.chain(*[r[1] for r in tiles_with_borders if t[0] != r[0]]))) == 4)

# star one
print(corner_tiles, prod(corner_tiles))

pieces_per_row = int(sqrt(len(a)))

tiles = list(map(tiles_content, a))

tile_id = corner_tiles[0]
top_left_tile = list(t[1] for t in tiles if t[0] == tile_id)[0]


# start with the corner tile (original)
# rotate it in such a way that the right and bottom borders are the connecting ones
top_left_tile = list(t for t in transformations(top_left_tile) if set([t[1][1], t[1][3]]) -
                     set(itertools.chain(*[o[1] for o in tiles_with_borders if o[0] != tile_id])) == set())[1]

right = top_left_tile[1][3]
bottom = top_left_tile[1][1]

puzzle = []
connected = set()

for y in range(pieces_per_row):
    for x in range(pieces_per_row):
        if x == 0 and y == 0:
            puzzle.append(contents(top_left_tile[0]))
            connected.add(tile_id)
        elif x == 0:
            # left most piece of the puzzle on a new row
            next, id = list((t, o[0]) for o in tiles for t in transformations(o[1])
                            # will connect with it's upper border
                            if (o[0] not in connected) and t[1][0] == bottom)[0]
            right = next[1][3]
            bottom = next[1][1]
            puzzle.append(contents(next[0]))
            connected.add(id)
        else:
            # find the next available piece on the right
            next, id = list((t, o[0]) for o in tiles for t in transformations(o[1])
                            # with it's left border connecting
                            if (o[0] not in connected) and t[1][2] == right)[0]
            right = next[1][3]
            puzzle.append(contents(next[0]))
            connected.add(id)


def final(puzzle):
    # turn the array into a single image
    for i in map(lambda row_tuple: itertools.chain(*[row_tuple]),
                 zip(*[puzzle[i::pieces_per_row] for i in range(pieces_per_row)])):
        yield list(map(lambda r: "".join(r), zip(*i)))


image = list(itertools.chain(*final(puzzle)))

# this is the pattern for the example
# sea_monster = r'#[\.#]{5}#[\.#]{4}##[\.#]{4}##[\.#]{4}###[\.#]{5}#[\.#]{2}#[\.#]{2}#[\.#]{2}#[\.#]{2}#[\.#]{2}#'
sea_monster = r'(?=(#[\.#]{77}#[\.#]{4}##[\.#]{4}##[\.#]{4}###[\.#]{77}#[\.#]{2}#[\.#]{2}#[\.#]{2}#[\.#]{2}#[\.#]{2}#))'


def count_waves(string):
    return sum(1 for pixel in string if pixel == '#')


# rotate and flip to make sure the image is oriented correctly
for t in transformations(image):
    transformed = "".join(t[0])
    # note: the trick here is the use of a capturing group inside a lookahead
    # this makes sure that overlapping sea monsters can be detected as well
    found = re.findall(sea_monster, transformed)
    if found:
        # count the waves that are not part of one or more sea monsters which cause 15 waves each
        print(count_waves(transformed) - len(found)*15)
        break
