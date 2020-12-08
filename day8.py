import re

regex = r"(\w+)\s([-+]\d+)"
p = re.compile(regex)

a = []
for line in open('day8.txt').read().split('\n'):
    a.append(p.match(line).groups())


def go(instructions):
    pointer = 0
    visited = []
    acc = 0
    looped = False

    while True:
        if pointer in visited:
            looped = True
            break
        elif pointer == len(instructions):
            break
        else:
            visited.append(pointer)

            i, arg = instructions[pointer]

            if i == "nop":
                pointer += 1
            elif i == "acc":
                acc += int(arg)
                pointer += 1
            elif i == "jmp":
                pointer += int(arg)
            else:
                print("don't know {i} {arg}")
                break

    return (acc, looped)


print(go(a))


def fix(instructions):
    acc = -1

    for i in range(len(instructions)):
        a = instructions.copy()
        instr, arg = a[i]

        if instr == "nop":
            a[i] = ('jmp', arg)
        elif instr == "jmp":
            a[i] = ('nop', arg)
        else:
            a[i] = a[i]

        acc, result = go(a)

        if not result:
            break
        else:
            continue

    return acc


print(fix(a))
