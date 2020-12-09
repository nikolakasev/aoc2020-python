import itertools

a = []
for line in open('day9.txt').read().split('\n'):
    a.append(float(line))


preamble = 25


def check(numbers, preamble):
    for i in range(preamble, len(numbers)):
        valid = False
        for a, b in itertools.combinations(numbers[(i - preamble):i], 2):
            if (a + b == numbers[i]):
                valid = True
                break

        if not valid:
            return numbers[i]


print(check(a, preamble))
