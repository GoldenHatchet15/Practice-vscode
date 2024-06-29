#!/usr/bin/env python3

# Import the math module
import math 
from fractions import Fraction

def calculator():
    # print the menu
    print("Calculator menu")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        # Get the user's choice
        # Check if the choice is valid

        choice = input("Enter your choice: ")
        if choice in ['1', '2', '3', '4']: 
            break
        else:
            choice = input("Invalid choice. Please enter a valid choice: ")

    def get_number(prompt):
        while True:
            try:
                return Fraction(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    if choice == '1': # Addition________________________________________________________________________________________________________________________
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = x + y 
        print(f"The result of {x} + {y} = {result}")
    elif choice == '2':# Subtraction_____________________________________________________________________________________________________________________
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = x - y
        print(f"The result of {x} - {y} = {result}")
    elif choice == '3': # Multiplication_____________________________________________________________________________________________________________________
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = x * y
        print(f"The result of {x} * {y} = {result}")
    elif choice == '4': # Division_____________________________________________________________________________________________________________________
        x = get_number("Enter the first number: ")
        y = get_number("Enter the second number: ")
        result = x / y
        print(f"The result of {x} / {y} = {result}")
    else:
        print("Invalid choice. Please enter a valid choice.")
    
if __name__ == "__main__":
    calculator()
        