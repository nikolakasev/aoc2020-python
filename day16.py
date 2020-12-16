import re
import math

range_pattern = r"(\w+\s?\w+):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)"
range_reg = re.compile(range_pattern)

a = []
for line in open('day16.txt').read().split('\n\n'):
    a.append(line)

valid_ranges = []
for i in a[0].split("\n"):
    valid_ranges.append((int(range_reg.match(i).groups()[
        1]), int(range_reg.match(i).groups()[2])))
    valid_ranges.append((int(range_reg.match(i).groups()[
        3]), int(range_reg.match(i).groups()[4])))


def ticket_to_values(t):
    return list(map(lambda f: int(f), t.split(",")))


# add my ticket to the list of valid ones
valid_tickets = [ticket_to_values(a[1].split("\n")[1])]

invalid = 0
for ticket in a[2].split("\n"):
    if ticket != "nearby tickets:":
        valid = True

        for f in ticket.split(","):
            field = int(f)

            # if the field value is not in at least onerange, the whole passport is invalid
            if sum(1 for i in valid_ranges if field >= i[0] and field <= i[1]) == 0:
                valid = False
                invalid += field

        if valid:
            valid_tickets.append(ticket_to_values(ticket))


print(invalid)


def positions_to_ranges(tickets, positions, ranges, range_indexes):
    # match positions to ranges such that
    return ((f, r) for f in positions for r in range_indexes
            # for all tickets
            if len(tickets) == sum(1 for t in tickets
                                   # the value on a given position is in one of the two ranges
                                   if (t[f] >= ranges[r*2][0] and t[f] <= ranges[r*2][1])
                                   or (t[f] >= ranges[r*2 + 1][0] and t[f] <= ranges[r*2 + 1][1])))


# each ticket has the same amount of fields, so take it from the first one
positions_left = set(range(len(valid_tickets[0])))
# ranges come in pairs, for example: 'class: 0-1 or 4-19' is (0, 1), (4, 19)
ranges_left = set(range(len(valid_ranges) // 2))

matches = set(positions_to_ranges(
    valid_tickets, positions_left, valid_ranges, ranges_left))


def unique_positions(matches, positions_left, ranges_left):
    while len(ranges_left) > 0:
        exact = list(r for r in ranges_left if sum(
            1 for m in matches if m[1] == r and m[0] in positions_left) == 1)

        exact_pairs = list(
            filter(lambda m: m[1] in exact and m[0] in positions_left, matches))

        positions_left = positions_left - set(map(lambda p: p[0], exact_pairs))
        ranges_left = ranges_left - set(exact)

        for p in exact_pairs:
            yield p[1], p[0]


# field -> position in the ticket
positions = dict(unique_positions(matches, positions_left, ranges_left))

# the fields that start with the word 'departure' are the first six fields in the ticket
# for my ticket, multiply the values from the positions of those fields
print(math.prod(valid_tickets[0][positions[f]] for f in range(6)))
