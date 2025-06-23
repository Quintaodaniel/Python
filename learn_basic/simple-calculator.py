def sum(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def product(a, b):
    return a * b

def division(a, b):
    if b == 0:
        print("Error! Division by zero")
        return
    return a / b

a = int(input("Enter with the first number: "))
b = int(input("Enter with the second numbers: "))
print("\nChoose which operation you want:")
print("\n[1] Sum")
print("[2] Subtraction")
print("[3] Product")
print("[4] Division")

op = int(input("Option: "))

if op == 1:
    print(f"Result: {sum(a,b)}")
elif op == 2:
    print(f"Result: {subtraction(a,b)}")
elif op == 3:
    print(f"Result: {product(a,b)}")
elif op == 4:
    print(f"Result: {division(a,b)}")
else:
    print("Option Invalid")