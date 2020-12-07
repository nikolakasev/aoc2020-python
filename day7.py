import re

holder = r"(\w+\s\w+)\sbags\scontain"
holder_reg = re.compile(holder)

contained = r"\d+\s(\w+\s\w+)\sbags*"
contained_reg = re.compile(contained)

a = []
for line in open('day7.txt').read().split('\n'):
    a.append(line)

shiny = "shiny gold"
count = 0

tree = []
for bag in a:
    name = holder_reg.match(bag).groups()[0]
    holding = contained_reg.findall(bag)
    tree.append((name, holding))


def get_holder(bag, tree):
    holders = []
    for name, holds in tree:
        if bag in holds:
            holders.append(name)
    if len(holders) == 0:
        return ","
    else:
        return ",".join(holders) + "," + ",".join(list(map(lambda holder: get_holder(holder, tree), holders)))


print(len(set(get_holder(shiny, tree).split(","))) - 1)
