import re

reg = r'^(\d+):\s(("([ab])")|((\d+)\s(\d+)\s\|\s(\d+)\s(\d+))|(\d+)|((\d+)\s\|\s(\d+))|((\d+)\s(\d+)))$'
rules_pattern = re.compile(reg)

a = []
for line in open('day19.txt').read().split('\n\n'):
    a.append(line)

for rule in a[0].split('\n'):
    print(rules_pattern.match(rule).groups())
