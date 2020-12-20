from math import prod
import itertools

a = []
for line in open('day20.txt').read().split('\n\n'):
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


tiles = list(map(tile_from_string, a))

# a corner tile always has two of it's borders not connected
# find all tiles which still have 4 borders left (two original + two transformed) when substracting all other known borders
print(prod(t[0] for t in tiles if len(
    set(t[1]) - set(itertools.chain(*[r[1] for r in tiles if t[0] != r[0]]))) == 4))
