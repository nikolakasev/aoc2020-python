import re

a = []
for line in open('day14.txt').read().split('\n'):
    a.append(line)

mask_pattern = r"mask\s=\s([X01]{36})"
mask = re.compile(mask_pattern)

write_pattern = r"mem\[(\d+)\]\s=\s(\d+)"
write = re.compile(write_pattern)


bit_length = 36


def apply_mask(mask, value):
    bit_list = list(bin(value))

    if len(bit_list) < bit_length + 2:
        bit_list = ['0', 'b'] + ['0'] * \
            (bit_length - len(bit_list) + 2) + bit_list[2:]

    return ['0', 'b'] + list(map(lambda pair: pair[1] if pair[1] != 'X' else pair[0], zip(bit_list[2:], list(mask))))


def bit_list_to_int(bit_list):
    return int("".join(bit_list), 2)


memory = dict()

# print(bit_list_to_int(apply_mask('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 0)))
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
