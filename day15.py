input = [0, 3, 6]

memory = dict()


for i in range(len(input)):
    memory[input[i]] = i + 1


def remember(memory, number, turn):
    print(f"to remember {number} on turn {turn}")
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
        print(f"{history} for {last_number_spoken} is a tuple")
        speak = history[1] - history[0]
    elif type(history) is int:
        print(f"{history} for {last_number_spoken} is an int")
        speak = 0
    else:
        print(f"{history} no, NEW {last_number_spoken}")
        speak = last_number_spoken

    remember(memory, speak, turn)

    if (target == turn):
        return speak
    else:
        return say(memory, turn + 1, speak, target)


print(say(memory, len(memory) + 1, 6, 2020), memory)
# print(8 in memory.keys())
