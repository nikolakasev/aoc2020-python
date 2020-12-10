a = []
for line in open('day10.txt').read().split('\n'):
    a.append(int(line))


device = max(a) + 3
# add the own device and the charging outlet
a = sorted(a + [device] + [0])

print(a)

one = 0
two = 0
three = 0

for i in range(len(a)-1):
    print(a[i+1] - a[i])
    if a[i+1] - a[i] == 1:
        one += 1
    elif a[i+1] - a[i] == 2:
        two += 1
    else:
        three += 1

print(one*three)
