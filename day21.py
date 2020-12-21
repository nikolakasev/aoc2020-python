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
    print(
        f"potentials for {a} are {set.intersection(*[set(f[0]) for f in input if a in f[1]])}")

    potentials.update(set.intersection(
        *[set(f[0]) for f in input if a in f[1]]))

# star one
print(sum(1 for f in input for i in f[0] if i in ingredients - potentials))

# star two, solved by hand :)
# potentials for sesame are {'lmxt', 'nmtzlj'}
# potentials for peanuts are {'lmxt', 'gpxmf'}
# potentials for soy are {'nmtzlj', 'dlkxsxg', 'gpxmf', 'fvqg'}
# potentials for wheat are {'mxf', 'gpxmf', 'dxzq'}
# potentials for dairy are {'lmxt'}
# potentials for shellfish are {'dlkxsxg', 'gpxmf'}
# potentials for fish are {'mxf', 'dlkxsxg'}
# potentials for eggs are {'lmxt', 'dlkxsxg', 'fvqg', 'rggkbpj'}

# lmxt dairy
# rggkbpj eggs
# mxf fish
# gpxmf peanuts
# nmtzlj sesame
# dlkxsxg shellfish
# fvqg soy
# dxzq wheat

# lmxt,rggkbpj,mxf,gpxmf,nmtzlj,dlkxsxg,fvqg,dxzq
