

a = []
for line in open('day6.txt').read().split('\n\n'):
    a.append(line)

print(sum(map(lambda group: len(set(list("".join(group.split('\n'))))), a)))


def all_answers(group):
    unique = set(list("".join(group.split('\n'))))
    people = group.split('\n')
    return len(set.intersection(
        *([unique] + list(
            map(lambda person: set(list(person)),
                people)))
    ))


print(sum(map(all_answers, a)))
