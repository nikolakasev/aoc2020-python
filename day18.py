import re

inner_brackets = r'\(([0-9\+\*\s]+)\)'
plus_recedence = r'(\d+\s\+\s\d+)'

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


def evaluate_plus_precedence(expression):
    while True:
        # evaluate pairs with '+' first
        if '+' in expression:
            match = re.search(plus_recedence, expression)
            expr_with_plus = match.groups()[0]
            expression = re.sub(plus_recedence,
                                str(evaluate(expr_with_plus)), expression, count=1)
        else:
            break

    return evaluate(expression)


def reduce(string, f=evaluate):
    # loop until all inner expressions containing brackets are evaluated
    while '(' in string:
        # find the first inner most brackets
        match = re.search(inner_brackets, string)
        if match:
            expr_in_brackets = match.groups()[0]
            # replace once
            string = re.sub(inner_brackets,
                            str(f(expr_in_brackets)), string, count=1)
        else:
            break

    return f(string)


# for each line, evaluate and sum all values
print(sum(map(reduce, a)))
print(sum(map(lambda e: reduce(e, f=evaluate_plus_precedence), a)))
