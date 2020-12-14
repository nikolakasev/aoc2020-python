import re
from itertools import product

a = []
for line in open('day14.txt').read().split('\n'):
    a.append(line)

mask_pattern = r"mask\s=\s([X01]{36})"
mask = re.compile(mask_pattern)

write_pattern = r"mem\[(\d+)\]\s=\s(\d+)"
write = re.compile(write_pattern)


bit_length = 36


def value_to_36bit_list(value):
    bit_list = list(bin(value))

    if len(bit_list) < bit_length + 2:
        bit_list = ['0', 'b'] + ['0'] * \
            (bit_length - len(bit_list) + 2) + bit_list[2:]

    return bit_list


def apply_mask(mask, value):
    return ['0', 'b'] + list(map(lambda pair: pair[1] if pair[1] != 'X' else pair[0], zip(value_to_36bit_list(value)[2:], list(mask))))


def bit_list_to_int(bit_list):
    return int("".join(bit_list), 2)


memory = dict()

m = ""
for i in range(len(a)):
    its_a_mask = mask.match(a[i])
    its_a_write = write.match(a[i])

    if its_a_mask:
        m = its_a_mask.groups()[0]
    else:
        address = its_a_write.groups()[0]
        value = its_a_write.groups()[1]

        # write to memory
        memory[address] = bit_list_to_int(apply_mask(m, int(value)))


print(sum(memory.values()))


def replace_at(list, index, new):
    return list[0:index] + [new] + list[index+1:]


memory = dict()
m = ""
for i in range(len(a)):
    its_a_mask = mask.match(a[i])
    its_a_write = write.match(a[i])

    if its_a_mask:
        m = its_a_mask.groups()[0]
    else:
        address = int(its_a_write.groups()[0])
        value = int(its_a_write.groups()[1])

        # the indexes of the occurrence of floating bits
        mask_to_apply = list(filter(lambda p: p[1] == 'X', enumerate(m)))

        # apply the mask: 'X' marks it as 'X' (floating bit), 0 leaves the bit unchanged, otherwise replace the bit with 1
        result = list(map(lambda pair: 'X' if pair[1] == 'X' else (pair[0] if pair[1] == '0' else '1'), zip(
            value_to_36bit_list(address)[2:], list(m))))

        # produce tuples of all permutations of the bits
        # note: the tuples are always the same for each length, so the result of 'repeat' can be memoized to speed up if necessary
        for c in product([0, 1], repeat=len(mask_to_apply)):
            # for each floating bit
            for j in range(len(mask_to_apply)):
                # replace it with the corresponding value from the permutation tuple
                result = replace_at(result, mask_to_apply[j][0], str(c[j]))

            # all floating bits are now replaces, turn the bit sequence to an integer address and write a value on it
            memory[bit_list_to_int(result)] = value


print(sum(memory.values()))
