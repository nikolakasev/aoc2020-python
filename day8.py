import re

regex = r"(\w+)\s([-+]\d+)"
p = re.compile(regex)

a = []
for line in open('day8.txt').read().split('\n'):
    a.append(p.match(line).groups())

print(a)


def go(instruction_set):
    pointer = 0
    visited = []
    acc = 0

    while True:
        if pointer in visited:
            break
        else:
            visited.append(pointer)

            i, arg = a[pointer]

            print(i, arg, visited)

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

    return acc


print(go(a))
