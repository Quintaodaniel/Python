"""
Project: Basic Calculator

Skills practiced:
- Functions and parameters
- Conditional logic (if/else)
- Exception handling (try/except)
- Dictionary for function mapping
- Input validation and error messages
- Type casting (str to float/int)
- Basic arithmetic operations
- Program structure with main()
"""


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Erro! Divisão por zero não é permitida.")
    return a / b

def main():
    operations = {
        1: add,
        2: subtract,
        3: multiply,
        4: divide
    }

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")
        return

    print("\nChoose the operation you want to perform:")
    print("[1] Sum")
    print("[2] Subtraction")
    print("[3] Product")
    print("[4] Division")

    try:
        choice = int(input("Option: "))
        operation_func = operations[choice]
    except (ValueError, KeyError):
        print("Opção inválida.")
        return

    try:
        result = operation_func(num1, num2)
        print(f"Result: {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()