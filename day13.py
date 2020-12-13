a = []
for line in open('day13.txt').read().split('\n'):
    a.append(line)

print(a)

goal = int(a[0])
departures = list(filter(lambda f: f != 'x', a[1].split(',')))

gaps = list(map(lambda d: (goal // int(d)) *
                int(d) + int(d) - goal, departures))

print(gaps)

pairs = list(sorted(zip(gaps, departures)))
print(int(pairs[0][0]) * int(pairs[0][1]))
