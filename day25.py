# input = [5764801, 17807724]
input = [14222596, 4057428]


def transform(n, subject_number):
    # set the value to itself multiplied by the subject number
    n = n * subject_number
    # set the value to the remainder after dividing the value by 20201227
    _, remainder = divmod(n, 20201227)
    return remainder


def loop_size(subject_number, key):
    n = 1
    cycles = 0

    # with a little trial and error, work out the loop size
    while n != key:
        cycles += 1
        n = transform(n, subject_number)

    return cycles


def calculate_key(subject_number, loop_size):
    n = 1
    for _ in range(loop_size):
        n = transform(n, subject_number)

    return n


# star one
print(calculate_key(input[0], loop_size(7, input[1])))
