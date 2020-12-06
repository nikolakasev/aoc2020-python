import itertools

for c in itertools.combinations('ABCD', 2):
    one, two = c
    print(two)

head, *tail = [1, 2, 3, 4, 5]
print(head)

a = []
for line in open('day3.txt').read().split('\n'):
    a.append(line)

x = 0
y = 0

b, c, d, e, f = 0, 0, 0, 0, 0

h, *tail = [1, 2, 3, 4]

print(len(a))

while x + 1 < len(a):
    x = x + 1
    y = y + 1
    trees = list(a[x])*75
    if trees[y] == '#':
        b = b + 1

x = 0
y = 0

while x + 1 < len(a):
    x = x + 1
    y = y + 3
    trees = list(a[x])*75
    if trees[y] == '#':
        c = c + 1

x = 0
y = 0

while x + 1 < len(a):
    x = x + 1
    y = y + 5
    trees = list(a[x])*75
    if trees[y] == '#':
        d = d + 1

x = 0
y = 0

while x + 1 < len(a):
    x = x + 1
    y = y + 7
    trees = list(a[x])*75
    if trees[y] == '#':
        e = e + 1

x = 0
y = 0

while x + 2 < len(a):
    x = x + 2
    y = y + 1
    trees = list(a[x])*75
    if trees[y] == '#':
        f = f + 1


print(b*c*d*e*f)
