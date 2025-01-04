def evaluate_rpn(expression):

        stack = []

        tokens = expression.split()

        for token in tokens:
            if token.isdigit():
                  stack.append(int(token))
            elif token in "+-*/":
                num2=stack.pop()
                num1=stack.pop()

                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                elif token == '/':
                    if num2 != 0:
                        stack.append(num1 / num2)
                    else:
                        return "Error: Division by zero"
            elif token=="=":
                return stack.pop()
        return "Error: Invalid expression"


expressions = [
    "2 3 + =",
    "2 4 1 + * =",
    "2 3 + 4 5 + * =",
    "8 3 1 + / 3 2 - 4 + * ="
]

for exp in expressions:
     print(f"Expression: {exp} Result: {evaluate_rpn(exp)}")