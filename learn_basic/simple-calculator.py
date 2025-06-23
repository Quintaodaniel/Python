"""
GOAL:
    Simple calculator (add, subtract, multiply, divide).

PRACTICE:
    Functions, basic operators, conditionals, error handling, input/output.
"""

def add(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def product(a, b):
    return a * b

def division(a, b):
    if b == 0:
        print("Error! Division by zero.")
        return None
    return a / b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("\nChoose the operation you want to perform:")
print("[1] Sum")
print("[2] Subtraction")
print("[3] Product")
print("[4] Division")

op = int(input("Option: "))

if op == 1:
    print(f"Result: {add(a, b)}")
elif op == 2:
    print(f"Result: {subtraction(a, b)}")
elif op == 3:
    print(f"Result: {product(a, b)}")
elif op == 4:
    result = division(a, b)
    if result is not None:
        print(f"Result: {result}")
else:
    print("Invalid option.")
