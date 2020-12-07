import re

holder = r"(\w+\s\w+)\sbags\scontain"
holder_reg = re.compile(holder)

contained = r"\d+\s(\w+\s\w+)\sbags*"
contained_reg = re.compile(contained)

a = []
for line in open('day7.txt').read().split('\n'):
    a.append(line)

shiny = "shiny gold"

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
        # todo turn into a set
        return ",".join(holders) + "," + ",".join(list(map(lambda holder: get_holder(holder, tree), holders)))


# todo this is stupid
print(len(set(get_holder(shiny, tree).split(","))) - 1)

contained = r"(\d)+\s(\w+\s\w+)\sbags*"
contained_reg = re.compile(contained)

# todo refactor by using the same regular expression, but simplify the tuple for P1
tree = []
for bag in a:
    name = holder_reg.match(bag).groups()[0]
    holding = contained_reg.findall(bag)
    tree.append((name, holding))


def bags_total(bag, amount, tree):
    for name, holds in tree:
        if name == bag:
            if len(holds) == 0:
                # print(f"{amount} {bag} holds nothing")
                return 1 * amount
            else:
                total = sum(
                    list(map(lambda bag: bags_total(bag[1], int(bag[0]), tree), holds)))
                # print(f"{amount} {bag} holds {total}")
                return amount + amount * total


print(bags_total(shiny, 1, tree) - 1)
