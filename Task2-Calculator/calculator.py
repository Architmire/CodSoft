def calculator():
    print("Choose operation: +, -, *, /")
    op = input("Operation: ")

    if op in ['+', '-', '*', '/']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Cannot divide by zero.")
                    return

            print(f"Result: {result}")
        except ValueError:
            print("Please enter valid numbers.")
    else:
        print("Invalid operation.")

if __name__ == "__main__":
    calculator()