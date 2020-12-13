from functools import lru_cache, partial

a = []
for line in open('day13.txt').read().split('\n'):
    a.append(line)


goal = int(a[0])
departures = list(filter(lambda f: f != 'x', a[1].split(',')))

gaps = list(map(lambda d: (goal // int(d)) *
                int(d) + int(d) - goal, departures))


pairs = list(sorted(zip(gaps, departures)))
print(int(pairs[0][0]) * int(pairs[0][1]))


# @lru_cache(maxsize=None)
# def f(t):
#     return t*17


# @lru_cache(maxsize=None)
# def g(t):
#     return t*13


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


# print(find_cycle(f, g, -1, 0, 2))
# print(find_cycle(f, g, 6, 8, 2))


# @lru_cache(maxsize=None)
# def acc(t):
#     return t*(25 - 8)*13 + 8 * 13


# @lru_cache(maxsize=None)
# def z(t):
#     return t*19


# print("acc", acc(1))


# print(find_cycle(acc, z, -1, 0, 1))
# print(find_cycle(acc, z, 15, 180, 1))

# offset = 3
# print(z(180) - offset)


# busses = ['17', 'x', '13', '19']
busses = [1789, 37, 47, 1889]


def n(t): return t*int(busses[0])


offset = 0
# todo maybe just add the offset for the first pair at the end of the calculation?
first_pair = True
for bus in busses[1:]:
    print(bus)
    if (bus == 'x'):
        offset += 1
        continue
    else:
        offset += 1
        _id = int(bus)
        def m(t, _id=_id): return t*_id

        print(f"to find cycle {n(1)}")
        t1, t2 = find_cycle(n, m, -1, 0, offset)
        t3, t4 = find_cycle(n, m, t1, t2, offset)

        @lru_cache(maxsize=None)
        def b(t, t2=t2, t4=t4, _id=_id): return t * (t4 - t2) * _id + \
            (0 if first_pair else t2 * _id)

        first_pair = False
        offset = 0
        n = b

        print(f"{(t1, t2, t3, t4)}")

        print(f"returns {n(1)}")
