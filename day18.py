import re

inner_brackets = r'\(([0-9\+\*\s]+)\)'
plus_recedence = r'\d+\s\+\s\d+'

a = []
for line in open('day18.txt').read().split('\n'):
    a.append(line)


def evaluate(expression):
    # evaluate an expression without brackets
    result = 1
    symbol = '*'
    expression = expression.split(" ")

    for i in range(len(expression)):
        # assume always positive integers
        if expression[i].isdigit():
            operand = int(expression[i])
            if symbol == '*':
                result = result * operand
            else:
                result = result + operand
        else:
            symbol = expression[i]

    return result


def reduce(string):
    # loop until all inner expressions containing brackets are evaluated
    while '(' in string:
        # find the first inner most brackets
        match = re.search(inner_brackets, string)
        if match:
            expr_in_brackets = match.groups()[0]
            # replace once
            string = re.sub(inner_brackets,
                            str(evaluate(expr_in_brackets)), string, count=1)
        else:
            break

    return evaluate(string)


# for each line, evaluate and sum all values
print(sum(map(reduce, a)))
