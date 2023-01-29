def evaluate_postfix(expression):
    stack = []

    expression = expression.split(" ")
    for character in expression:
        if character not in ['+', '-', '*', '/']:
            stack.append(character)
        else:
            operand1 = int(stack.pop(len(stack) - 1))
            operand2 = int(stack.pop(len(stack) - 1))
            result = 0
            if character == '+':
                result = operand2 + operand1
                stack.append(result)
            elif character == '-':
                result = operand2 - operand1
                stack.append(result)
            elif character == '*':
                result = operand2 * operand1
                stack.append(result)
            elif character == '/':
                result = operand2 // operand1
                stack.append(result)

    return stack[0]

def evaluate_prefix(expression):
    stack = []

    expression = reversed(expression.split(" "))
    for character in expression:
        if character not in ['+', '-', '*', '/']:
            stack.append(character)
        else:
            operand2 = int(stack.pop(len(stack) - 1))
            operand1 = int(stack.pop(len(stack) - 1))
            result = 0
            if character == '+':
                result = operand2 + operand1
                stack.append(result)
            elif character == '-':
                result = operand2 - operand1
                stack.append(result)
            elif character == '*':
                result = operand2 * operand1
                stack.append(result)
            elif character == '/':
                result = operand2 // operand1
                stack.append(result)

    return stack[0]