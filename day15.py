
def remember(memory, number, turn):
    if number in memory.keys():
        history = memory[number]
        if type(history) is tuple:
            # the number was spoken twice already, shift turns - forget at history[0]
            memory[number] = (history[1], turn)
        else:
            # the number was spoken once already, remember the second turn as well
            memory[number] = (history, turn)
    else:
        # the first time the number was spoken
        memory[number] = turn

    return memory


def say(memory, turn, number):
    history = memory[number]

    # for each spoken number, keep the last one (int) or last two (tuple) turns it was spoken
    if type(history) is tuple:
        speak = history[1] - history[0]
    elif type(history) is int:
        speak = 0
    else:
        speak = number

    return speak


def play(numbers, target):
    # prepare the memory with the numbers so far and their corresponding turns
    m = dict()
    for i in range(len(numbers)):
        m[numbers[i]] = i + 1

    number = numbers[-1]

    for i in range(len(numbers) + 1, target + 1):
        # which number to say?
        number = say(m, i, number)
        # make sure to remember it was said
        m = remember(m, number, i)

    return number


n = [6, 4, 12, 1, 20, 0, 16]
print(play(n, 2020))
print(play(n, 30000000))
