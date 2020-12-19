import re
from functools import lru_cache

reg = r'^(\d+):\s(("([ab])")|((\d+)\s(\d+)\s\|\s(\d+)\s(\d+))|(\d+)|((\d+)\s\|\s(\d+))|((\d+)\s(\d+)))$'
rules_pattern = re.compile(reg)

a = []
for line in open('day19.txt').read().split('\n\n'):
    a.append(line)

rules = dict()

for rule in a[0].split('\n'):
    groups = rules_pattern.match(rule).groups()
    rules[groups[0]] = groups


@lru_cache(maxsize=None)
def pattern_for_rule(rule):
    r = rules[rule]
    parts = r[1].split(" ")

    if len(parts) == 5:
        return "((" + pattern_for_rule(parts[0]) + pattern_for_rule(parts[1]) + ")|(" + pattern_for_rule(parts[3]) + pattern_for_rule(parts[4]) + "))"
    elif len(parts) == 3:
        return "(" + pattern_for_rule(parts[0]) + "|" + pattern_for_rule(parts[2]) + ")"
    elif len(parts) == 2:
        return pattern_for_rule(parts[0]) + pattern_for_rule(parts[1])
    elif len(parts) == 1 and '"' in r[1]:
        # extract the 'a' or 'b', from the middle of the string, for example from "a"
        print(f"extracted char {r[1][1]}")
        return list(r[1])[1]
    elif len(parts) == 1 and r[1].isdigit():
        print(f"single number {r[1]}")
        return pattern_for_rule(r[1])
    else:
        return f"pattern unknown {r[0]}"


def validate(pattern, string):
    reg = re.compile("^" + pattern + "$")
    if reg.match(string):
        return True
    else:
        return False


# pattern = "a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b"
pattern = pattern_for_rule('0')
# print(validate(pattern, "bababa"))

print(sum(1 for m in a[1].split('\n') if validate(pattern, m)))
