
import re

range_pattern = r"(\w+\s?\w+):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)"
range_reg = re.compile(range_pattern)

a = []
for line in open('s.txt').read().split('\n\n'):
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
print(valid_tickets)
print(valid_ranges)

# # for each field position
# for i in range(len(valid_tickets[0])):
#     # # for each ticket
#     # for t in valid_tickets:
#     #     # must fit exactly one field range
#     #     if all(()):
#     #         print(f"match found for {i}")
#     for r in range(len(ranges) // 2):
#         for t in valid_tickets:
#             # print(f"looking at {t[i]}")
#             if (t[i] >= ranges[r*2][0] and t[i] <= ranges[r*2][1]) \
#                     or (t[i] >= ranges[r*2 + 1][0] and t[i] <= ranges[r*2 + 1][1]):
#                 print(f"matched pos {i} for range {r}")
#         # if all((True for t in valid_tickets if (t[i] >= ranges[r*2][0] and t[i] <= ranges[r*2][1])
#         #         or (t[i] >= ranges[r*2 + 1][0] and t[i] <= ranges[r*2 + 1][1]))):
#         #     print(
#         #         f"match found for {i} in range {ranges[r*2]}, {ranges[r*2 + 1]}")


def positions_to_ranges(tickets, positions, ranges, range_indexes):
    return ((i, r) for i in positions for r in range_indexes
            if len(tickets) == sum(1 for t in tickets
                                   if (t[i] >= ranges[r*2][0] and t[i] <= ranges[r*2][1])
                                   or (t[i] >= ranges[r*2 + 1][0] and t[i] <= ranges[r*2 + 1][1])))


print(list(positions_to_ranges(valid_tickets, range(
    len(valid_tickets[0])), valid_ranges, range(len(valid_ranges) // 2))))

index_ranges = range(len(valid_ranges) // 2)

print(list(index_ranges))
