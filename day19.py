import re
from functools import lru_cache

reg = r'(\d+):\s(([0-9\s\|\"ab])+)'
rules_pattern = re.compile(reg)

a = []
for line in open('day19.txt').read().split('\n\n'):
    a.append(line)

rules = dict()

for rule in a[0].split('\n'):
    groups = rules_pattern.match(rule).groups()
    rules[groups[0]] = groups[1]


@lru_cache(maxsize=None)
def pattern_for_rule(rule):
    # recursively generate a regular expression from the list of rules
    parts = rules[rule].split(" ")

    if len(parts) == 5:
        # a pair of rules with an AND or another pair of rules (also with an AND)
        return "((" + pattern_for_rule(parts[0]) + pattern_for_rule(parts[1]) + ")|(" + pattern_for_rule(parts[3]) + pattern_for_rule(parts[4]) + "))"
    elif len(parts) == 3:
        # one rule OR another
        return "(" + pattern_for_rule(parts[0]) + "|" + pattern_for_rule(parts[2]) + ")"
    elif len(parts) == 2:
        # one rule followed by another - AND
        return pattern_for_rule(parts[0]) + pattern_for_rule(parts[1])
    elif len(parts) == 1 and '"' in rules[rule]:
        # extract the 'a' or 'b', from the middle of the string, for example from "a"
        return rules[rule][1]
    elif len(parts) == 1 and rules[rule].isdigit():
        # one rule points to exactly one other rule
        return pattern_for_rule(rules[rule])
    else:
        return f"pattern unknown {rules[rule]}"


def validate(pattern, string):
    reg = re.compile("^" + pattern + "$")
    if reg.match(string):
        return True
    else:
        return False


# star one
pattern = pattern_for_rule('0')
print(sum(1 for message in a[1].split('\n') if validate(pattern, message)))

pattern_42 = pattern_for_rule('42')
pattern_31 = pattern_for_rule('31')

# star two
# after experimentation we notice that pattern 42 doesn't match if applied more than 7 times, hence the 8
# a full pattern will always include at least two patterns 42 and one pattern 31, hence j starts from 1 and i from 2
# there must always be one pattern 42 more than pattern 31 because combining rule 8 (42) and 11 (42 31) results in (42 42 31), hence j ends one less than i
# so for all those combinations, check how many messages match the final patter and sum them all
print(sum(1 for message in a[1].split('\n')
          for i in range(2, 8)
          for j in range(1, i) if validate(pattern_42*i + pattern_31*j, message)))
