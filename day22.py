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


def recursive_combat(deck_one, deck_two, history=[]):
    one_won = True

    while len(deck_one) > 0 and len(deck_two) > 0:
        # infinite game prevention rule
        if sum(1 for h in history if deck_one == h[0] and deck_two == h[1]) > 0:
            # the game instantly ends in a win for player one
            one_won = True
            break
        else:
            # remember this round and how the decks are setup
            history.append((deck_one.copy(), deck_two.copy()))

        # both players play a card
        c = int(deck_one.pop(0))
        d = int(deck_two.pop(0))

        if c <= len(deck_one) and d <= len(deck_two):
            # the winner of this round will be determined by a new game of Recursive Combat!
            outcome, _ = recursive_combat(
                deck_one[:c], deck_two[:d], history=[])

            if outcome:
                one_won = True
                deck_one += [c, d]
            else:
                one_won = False
                deck_two += [d, c]
        elif (c > d):
            one_won = True
            deck_one += [c, d]
        else:
            one_won = False
            deck_two += [d, c]

    return (one_won, deck_one if one_won else deck_two)


# star two, takes about 20 seconds...
player_one = a[1:a.index('')]
player_two = a[a.index('') + 2:]

one, winning_deck = recursive_combat(player_one, player_two)
print(sum(multiplier * card for multiplier,
          # reverse the cards, enumerate them starting from 1 instead of 0 which is default
          card in enumerate(winning_deck[::-1], start=1)))
