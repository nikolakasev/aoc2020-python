from functools import lru_cache

a = []
for line in open('day13.txt').read().split('\n'):
    a.append(line)


goal = int(a[0])
departures = list(filter(lambda f: f != 'x', a[1].split(',')))

gaps = list(map(lambda d: (goal // int(d)) *
                int(d) + int(d) - goal, departures))


pairs = list(sorted(zip(gaps, departures)))
print(int(pairs[0][0]) * int(pairs[0][1]))


@lru_cache(maxsize=None)
def f(t):
    return t*17


@lru_cache(maxsize=None)
def g(t):
    return t*13


def find_cycle(f, g, t, t2, delta):

    start_of_cycle = False

    i = t + 1
    while True:
        tortoise = f(i)

        j = t2
        while True:
            hare = g(j)

            if hare == (tortoise + delta):
                start_of_cycle = True
                break
            elif hare > (tortoise + delta):
                break
            else:
                j += 1

        if start_of_cycle:
            break
        else:
            i += 1

    return(i, j)


print(find_cycle(f, g, -1, 0, 2))
print(find_cycle(f, g, 6, 8, 2))
print(find_cycle(f, g, 19, 25, 2))


@lru_cache(maxsize=None)
def acc(t):
    return t*(25 - 8)*13 + 8 * 13


@lru_cache(maxsize=None)
def z(t):
    return t*19


print(acc(2))

print(find_cycle(acc, z, -1, 0, 1))

offset = 3
print(z(180) - offset)
