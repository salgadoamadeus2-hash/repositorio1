#!/usr/bin/env python3
"""
Simple Calculator Program
Asks the user to input two numbers and an operation (+, -, *, /).
Performs the operation and prints the result.
Type 'q' at any prompt to quit.
"""

def get_number(prompt):
    while True:
        s = input(prompt).strip()
        if s.lower() == 'q':
            return None
        try:
            # support int or float
            if '.' in s:
                return float(s)
            return int(s)
        except ValueError:
            print("That's not a valid number. Try again or type 'q' to quit.")

def get_operation(prompt):
    valid = {'+','-','*','/','^'}
    while True:
        s = input(prompt).strip()
        if s.lower() == 'q':
            return None
        if s in valid:
            return s
        print("Invalid operation. Choose one of +, -, *, /, ^ (power), or type 'q' to quit.")

def calculate(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b
    if op == '^':
        return a ** b
    raise ValueError("Unknown operation")

def main():
    print("Simple Calculator — enter numbers and an operation (+, -, *, /, ^). Type 'q' to quit.")
    while True:
        a = get_number("Enter the first number: ")
        if a is None:
            break
        b = get_number("Enter the second number: ")
        if b is None:
            break
        op = get_operation("Enter an operation (+, -, *, /, ^): ")
        if op is None:
            break
        try:
            result = calculate(a, b, op)
        except ZeroDivisionError as e:
            print("Error:", e)
            continue
        except Exception as e:
            print("Error:", e)
            continue
        # print with integer formatting when possible
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        print(f"\nResult: {a} {op} {b} = {result}\n")

if __name__ == '__main__':
    main()
