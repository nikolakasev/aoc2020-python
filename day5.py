import math

seats = []
for line in open('day5.txt').read().split('\n'):
    seats.append(line)


def split_in_half(min, max, letters):
    if len(letters) == 1:
        letter = letters[0]
        if (letter == 'F') or (letter == 'L'):
            return min
        else:
            return max
    else:
        letter, *tail = letters
        if (letter == 'F') or (letter == 'L'):
            return split_in_half(min,
                                 min + int(math.floor((max - min) / 2)),
                                 tail)
        else:
            return split_in_half(min + int(math.floor((max - min) / 2 + 1)),
                                 max,
                                 tail)


def get_id(string):
    return split_in_half(0, 127, string[:7]) * 8
    + split_in_half(0, 7, string[-3:])


print(max(list(map(get_id, seats))))

last = 0
for seat in sorted(list(map(get_id, seats))):
    if last + 2 == seat:
        print(last + 1)
    else:
        last = seat
