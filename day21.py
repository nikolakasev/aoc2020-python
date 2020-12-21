import re
import itertools

reg = r'(.*)\s\(contains\s([\w\s\,]+)\)'
food = re.compile(reg)

input = []
for line in open('day21.txt').read().split('\n'):
    # print(food.match(line).groups())
    groups = food.match(line).groups()
    input.append((groups[0].split(' '), groups[1].split(', ')))

allergens = set(itertools.chain(*[f[1] for f in input]))
ingredients = set(itertools.chain(*[f[0] for f in input]))

potentials = set()
for a in allergens:
    potentials.update(set.intersection(
        *[set(f[0]) for f in input if a in f[1]]))

print(sum(1 for f in input for i in f[0] if i in ingredients - potentials))
