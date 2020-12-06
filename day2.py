import re

reg = r"(\d*)-(\d*)\s(\w*):\s(\w*)"
p = re.compile(reg)

a = []
for line in open('day2.txt').read().splitlines():
    a.append(line)

count = 0

for password in a:
    groups = p.match(password).groups()
    i = int(groups[0])
    j = int(groups[1])
    letter = groups[2]
    password = list(groups[3])
    if (password[i - 1] == letter or password[j - 1] == letter) \
            and (not(password[i - 1] == letter and password[j - 1] == letter)):
        count = count + 1

print(count)
