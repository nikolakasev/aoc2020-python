from math import prod, sqrt
import itertools

a = []
for line in open('s.txt').read().split('\n\n'):
    a.append(line)


def tile_from_string(string):
    s = string.split('\n')
    up = s[1]
    down = s[10]
    left = ""
    right = ""

    for i in range(1, 11):
        left = s[i][0] + left
        right = right + s[i][9]

    return (int(s[0][5:9]), [
        # tile borders
        up, down, left, right,
        # transformed counterparts
        up[::-1], down[::-1], left[::-1], right[::-1]
    ])


all_tiles = list(map(tile_from_string, a))

# a corner tile always has two of it's borders not connected
# find all tiles which still have 4 borders left (two original + two transformed) when substracting all other known borders
corner_tiles = list(t[0] for t in all_tiles if len(
    set(t[1]) - set(itertools.chain(*[r[1] for r in all_tiles if t[0] != r[0]]))) == 4)

print(corner_tiles)


pieces_per_row = int(sqrt(len(a)))

# rotate 90 degrees, 180 is then x2, 270 is x3
# flip down
# extract borders from tile
# extract the contents of a tile without the borders
# for a tile, return operation, borders and contents without the borders - lru_cache it
# O[\.#]{5}O[\.#]{4}OO[\.#]{4}OO[\.#]{4}OOO[\.#]{5}O[\.#]{2}O[\.#]{2}O[\.#]{2}O[\.#]{2}O[\.#]{2}O
# search for monster with r'#[\.#]{5}#[\.#]{4}##[\.#]{4}##[\.#]{4}###[\.#]{5}#[\.#]{2}#[\.#]{2}#[\.#]{2}#[\.#]{2}#[\.#]{2}#'

# start with the corner tile (original), pick right= and under= by finding the set intersection with all other tiles' borders, there must be 4 matches
# for each other not connected yet, find where it's left matches right= until 12 are connected (add to set of connected)
# next row, first match where top mathes under=, set new under=, repeat until 12 are connected (add to set of connected)
# finish when all 144 are connected

# turn the array into a single image
# rotate and flip until one or more regex matches are found, count the total amount of # and substract monsters*15
