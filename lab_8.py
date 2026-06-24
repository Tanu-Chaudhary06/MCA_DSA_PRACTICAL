def evaluate_postfix(expression):
    stack = []

    for char in expression:
        if char == ' ':
            continue

        if char.isdigit():
            stack.append(int(char))
        else:
            a = stack.pop()
            b = stack.pop()

            if char == '+':
                result = b + a
            elif char == '-':
                result = b - a
            elif char == '*':
                result = b * a
            elif char == '/':
                result = b / a

            stack.append(result)

    return stack[0]


expression = input("Enter a postfix expression: ")
result = evaluate_postfix(expression)
print("Result:", result)