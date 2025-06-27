"""
Project: Number Statistics

Skills practiced:
- Conditionals (if/else)
- Loops (for, while)
- Functions and scope
- Dictionary manipulation
- Square root using math module
- Exception handling (try/except)
- Input and output (input/print)
"""

import math

def check_parity(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    limit = int(math.sqrt(num)) + 1
    for i in range(3, limit, 2):
        if num % i == 0:
            return False
            
    return True

def find_divisors(num):
    if num < 1:
        return []

    divisors = []
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            divisors.append(i)
    
    divisors.append(num)
    return divisors

def prime_factorization(num):
    if not isinstance(num, int) or num < 2:
        return "Prime factorization is defined for integers greater than 1."

    factors = {}
    divisor = 2
    temp_num = num

    while temp_num % divisor == 0:
        factors[divisor] = factors.get(divisor, 0) + 1
        temp_num //= divisor
    
    divisor = 3
    while divisor * divisor <= temp_num:
        while temp_num % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            temp_num //= divisor
        divisor += 2

    if temp_num > 2:
        factors[temp_num] = factors.get(temp_num, 0) + 1

    output_parts = []
    for base in sorted(factors.keys()):
        exponent = factors[base]
        if exponent == 1:
            output_parts.append(f"{base}")
        else:
            output_parts.append(f"{base}^{exponent}")
            
    return " x ".join(output_parts)

def main():
    try:
        num_input = int(input("Enter an integer: "))
        print()

        parity_result = check_parity(num_input)
        print(f"Parity: {parity_result}")

        if is_prime(num_input):
            print("Result: It is a Prime number.")
        else:
            print("Result: It is a Composite number.")
        
        divisors_list = find_divisors(num_input)
        if not divisors_list:
             print("Divisors: [] (negative numbers are not handled)")
        else:
            print(f"Divisors: {divisors_list}")

        factorization_result = prime_factorization(num_input)
        print(f"Factored: {factorization_result}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()