from math import prod
from itertools import chain

# input = "389125467"
input = "327465189"


def input_to_cups(input):
    # a ring structure where each cup points to the next one and the last points to the first
    cups = dict()

    first = True
    first_cup = 0
    previous = 0

    # for each cup
    for i in input:
        if first:
            first = False
            previous = i
            # remember it, it's needed at the end
            first_cup = i
        else:
            # the previous cup points to the current one
            cups[previous] = i
            previous = i

    # make the ring complete by linking the last cup with the first one
    cups[previous] = first_cup

    return cups


def take(how_many, after_cup, cups):
    # take N cups starting from the cup next after the given cup
    count = 0
    acc = []
    next = cups[after_cup]

    while count < how_many:
        acc.append(next)
        next = cups[next]
        count += 1

    return acc


def play(cups, start_with, cup_max_number, rounds, how_many, after_cup):
    current_cup = start_with

    for move in range(rounds):
        # pick up three cups immediately clockwise of the current cup
        three = take(3, current_cup, cups)
        # remove them from the circle
        cups[current_cup] = cups[three[-1]]

        # substracting from cup with label 1 will result in 0, so take the highest value instead
        d = cup_max_number if current_cup == 1 else current_cup - 1
        # if this selects one of the cups that were just picked up
        while d in three:
            # keep substracting until it finds a cup that wasn't just picked up
            d -= 1
            if d < 1:
                # wrap around to the highest value on any cup's label instead
                d = cup_max_number

        # point the last cup to the cup which the destination cup points to
        cups[three[-1]] = cups[d]
        # place the three cups immediately clockwise of the destination cup
        cups[d] = three[0]

        # the new current cup is immediately clockwise of the current cup
        current_cup = cups[current_cup]

    return take(how_many, after_cup, cups)


# star one
print("".join(
    map(str, play(input_to_cups(map(int, input)), int(input[0]), 9, 100, 8, 1))))

# star two
print(prod(play(input_to_cups(chain(map(int, input), range(10, 1000001))),
                int(input[0]), 1000000, 10000000, 2, 1)))
