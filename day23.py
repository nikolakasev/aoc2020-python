# input = "389125467"
input = "327465189"

cups = list(map(int, input))

current_cup = cups[0]

for move in range(100):
    index = cups.index(current_cup)

    three = cups[index + 1:index + 4]

    d = 9 if current_cup == 1 else current_cup - 1
    while d in three:
        d -= 1
        if d < 1:
            d = 9

    after = cups[index + 4:] + cups[:index]
    d_index = after.index(d)

    cups = [current_cup] + after[:d_index] + [d] + three + after[d_index + 1:]
    current_cup = cups[1]

    print(f"at end, cups {cups}, current cup becomes {current_cup}")
