
import re

range_pattern = r"(\w+\s?\w+):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)"
range_reg = re.compile(range_pattern)

a = []
for line in open('day16.txt').read().split('\n\n'):
    a.append(line)

ranges = []
for i in a[0].split("\n"):
    ranges.append((int(range_reg.match(i).groups()[
                  1]), int(range_reg.match(i).groups()[2])))
    ranges.append((int(range_reg.match(i).groups()[
                  3]), int(range_reg.match(i).groups()[4])))


other_tickets = []
for o in a[2].split("\n"):
    if o != "nearby tickets:":
        other_tickets.extend(o.split(","))


invalid = 0
for o in other_tickets:
    valid = False
    ticket = int(o)

    if sum(1 for i in ranges if ticket >= i[0] and ticket <= i[1]) == 0:
        invalid += ticket


print(invalid)
