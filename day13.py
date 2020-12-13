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


def find_start_cycle(f, g, delta):
    t = 0
    t2 = 0
    start_of_cycle = False

    while True:
        tortoise = f(t)

        t2 = 0
        while True:
            hare = g(t2)

            if hare == (tortoise + delta):
                start_of_cycle = True
                break
            elif hare > (tortoise + delta):
                break
            else:
                t2 += 1

        if start_of_cycle:
            break
        else:
            t += 1

    return(t, t2)


print(find_start_cycle(f, g, 1))
