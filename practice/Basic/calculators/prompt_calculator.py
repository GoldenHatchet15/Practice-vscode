#!/usr/bin/env python3

# Import the necessary modules
from fractions import Fraction
import re

def calculator():
    # Define a function to get a number, supporting fractions
    def get_number(prompt):
        while True:
            try:
                return Fraction(prompt)
            except ValueError:
                print("Invalid input. Please enter a valid number or fraction (e.g., 3/4).")
                prompt = input("Enter the expression again: ")

    def parse_input(expression):
        # Use a regular expression to extract numbers and the operator
        match = re.match(r'^\s*(\S+)\s*([\+\-\*/])\s*(\S+)\s*$', expression)
        if match:
            x_str, operator, y_str = match.groups()
            x = get_number(x_str)
            y = get_number(y_str)
            return x, operator, y
        else:
            raise ValueError("Invalid expression format. Please enter in the format 'a + b'.")

    while True:
        # Get the user's input
        expression = input("Enter your calculation (e.g., '5/4 + 3/4'): ")
        try:
            x, operator, y = parse_input(expression)
            break
        except ValueError as e:
            print(e)
            continue
    
    if operator == '+': # Addition
        result = x + y 
        print(f"The result of {x} + {y} = {result}")
    elif operator == '-': # Subtraction
        result = x - y
        print(f"The result of {x} - {y} = {result}")
    elif operator == '*': # Multiplication
        result = x * y
        print(f"The result of {x} * {y} = {result}")
    elif operator == '/': # Division
        result = x / y
        print(f"The result of {x} / {y} = {result}")

if __name__ == "__main__":
    calculator()
