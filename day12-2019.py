import re
import itertools

regex = r"<x=(-*\d+),\sy=(-*\d+),\sz=(-*\d+)>"
p = re.compile(regex)


def moon(p_x, p_y, p_z, v_x, v_y, v_z):
    return {"pos": {"x": p_x, "y": p_y, "z": p_z}, "vel": {"x": v_x, "y": v_y, "z": v_z}}


a = []
for line in open('day12-2019.txt').read().split('\n'):
    x, y, z = p.match(line).groups()
    a.append(moon(int(x), int(y), int(z), 0, 0, 0))


def simulate_one_step(moons):
    for i in range(len(moons)):
        for j in range(i + 1, len(moons)):
            moon = moons[i]
            other = moons[j]
            updated_moon, updated_other = apply_gravity(
                moon, other)
            moons[i] = updated_moon
            moons[j] = updated_other

    for i in range(len(moons)):
        moons[i] = apply_velocity(moons[i])


def apply_gravity(one, another):
    return (moon(one["pos"]["x"],
                 one["pos"]["y"],
                 one["pos"]["z"],
                 one["vel"]["x"] + gravity(one["pos"]["x"],
                                           another["pos"]["x"]),
                 one["vel"]["y"] + gravity(one["pos"]["y"],
                                           another["pos"]["y"]),
                 one["vel"]["z"] + gravity(one["pos"]["z"],
                                           another["pos"]["z"])),
            moon(another["pos"]["x"],
                 another["pos"]["y"],
                 another["pos"]["z"],
                 another["vel"]["x"] + gravity(another["pos"]["x"],
                                               one["pos"]["x"]),
                 another["vel"]["y"] + gravity(another["pos"]["y"],
                                               one["pos"]["y"]),
                 another["vel"]["z"] + gravity(another["pos"]["z"],
                                               one["pos"]["z"]))
            )


def apply_velocity(m):
    return moon(m["pos"]["x"] + m["vel"]["x"],
                m["pos"]["y"] + m["vel"]["y"],
                m["pos"]["z"] + m["vel"]["z"],
                m["vel"]["x"],
                m["vel"]["y"],
                m["vel"]["z"],
                )


def gravity(a, b):
    if a < b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


for i in range(1000):
    simulate_one_step(a)


def total_energy(m):
    return (abs(m["pos"]["x"]) + abs(m["pos"]["y"]) + abs(m["pos"]["z"])) * \
        (abs(m["vel"]["x"]) + abs(m["vel"]["y"]) + abs(m["vel"]["z"]))


print(sum(map(total_energy, a)))
