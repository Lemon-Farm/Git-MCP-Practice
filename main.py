def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    elif operator == '%':
        return a % b
    else:
        return "Invalid operator"

print(calculator(1, 2, '+'))
print(calculator(10, 3, '%')) 