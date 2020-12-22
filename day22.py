a = []
for line in open('day22.txt').read().split('\n'):
    a.append(line)


player_one = a[1:a.index('')]
player_two = a[a.index('') + 2:]

while len(player_one) > 0 and len(player_two) > 0:
    # take the left most card from both decks
    c = int(player_one.pop(0))
    d = int(player_two.pop(0))

    # append to the end of the list (on the right)
    if (c > d):
        player_one += [c, d]
    else:
        player_two += [d, c]

# star one
print(sum(multiplier * card for multiplier,
          # reverse the cards, enumerate them starting from 1 instead of 0 which is default
          card in enumerate((player_one + player_two)[::-1], start=1)))
