a = []
for line in open('day10.txt').read().split('\n'):
    a.append(int(line))


device = max(a) + 3
# add the own device and the charging outlet
a = sorted(a + [device] + [0])

one = 0
three = 0

# assume there will be no difference of two, so only a difference of one and three
for i in range(len(a)-1):
    if a[i+1] - a[i] == 1:
        one += 1
    else:
        three += 1

print(one*three)

print(len(a), list(enumerate(a)))

# https://www.geeksforgeeks.org/overlapping-subproblems-property-in-dynamic-programming-dp-1/
# tabulated version, starting from the first entry, all entries are filled one by one
dp = [0] * len(a)
dp[0] = 1

for i in range(1, len(a)):
    for j in range(i):
        if a[i] - a[j] <= 3:
            dp[i] += dp[j]

print(dp[-1:])
