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


def contiguous_list(numbers, invalid_number):
    latest_range = []
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            subset = numbers[i:j+1]
            if sum(subset) == invalid_number and len(latest_range) < len(subset):
                latest_range = subset

    return latest_range


c = contiguous_list(a, check(a, preamble))
print(min(c) + max(c))
