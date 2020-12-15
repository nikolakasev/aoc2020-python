import sys
sys.setrecursionlimit(2025)

# input = [0, 3, 6]
input = [6, 4, 12, 1, 20, 0, 16]

memory = dict()


for i in range(len(input)):
    memory[input[i]] = i + 1


def remember(memory, number, turn):
    if number in memory.keys():
        history = memory[number]
        if type(history) is tuple:
            memory[number] = (history[1], turn)
        else:
            memory[number] = (history, turn)
    else:
        memory[number] = turn


def say(memory, turn, last_number_spoken, target):
    history = memory[last_number_spoken]

    if type(history) is tuple:
        speak = history[1] - history[0]
    elif type(history) is int:
        speak = 0
    else:
        speak = last_number_spoken

    remember(memory, speak, turn)

    if (target == turn):
        return speak
    else:
        return say(memory, turn + 1, speak, target)


print(say(memory, len(memory) + 1, 16, 2020))
# print(8 in memory.keys())
