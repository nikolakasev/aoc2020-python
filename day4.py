import re

a = []
for line in open('day4.txt').read().split('\n\n'):
    a.append(line)


count = 0

reg = r"(?=.*(byr:(\d{4}))\s)(?=.*(eyr:(\d{4}))\s)(?=.*(iyr:(\d{4}))\s)(?=.*(hgt:(\d+)(cm|in))\s)(?=.*(hcl:#[0-9a-f]{6})\s)(?=.*(ecl:(amb|blu|brn|gry|grn|hzl|oth))\s)(?=.*(pid:\d{9})\s)"
p = re.compile(reg)

for passport in a:
    string = " ".join(passport.split("\n")) + " "
    if ("byr" in passport) and ("iyr" in passport) \
            and ("eyr" in passport) and ("hgt" in passport) \
            and ("hcl" in passport) and ("ecl" in passport) \
            and ("pid" in passport):
        result = p.match(string)
        if result:
            groups = result.groups()
            byr = int(groups[1])
            iyr = int(groups[5])
            eyr = int(groups[3])
            hgt = int(groups[7])
            t = groups[8]
            if byr >= 1920 and byr <= 2002 \
                    and iyr >= 2010 and iyr <= 2020\
                    and eyr >= 2020 and eyr <= 2030\
                    and ((t == "cm" and (hgt >= 150 and hgt <= 193))
                         or (t == "in" and (hgt >= 59 and hgt <= 76))):
                print(groups)
                count += 1


print(count)
