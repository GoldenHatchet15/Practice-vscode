#!/usr/bin/env python3
from practice.aritmetic_function import ArithmeticFunctions

def main():
    while True:
        user_input = input("Enter 1 for add, 2 for subtract, or any other key to exit: ")

        if user_input == '1' or user_input == '2':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            if user_input == '1':
                result = ArithmeticFunctions.add_func(num1, num2)
                print("The result of addition is: ", result)

            elif user_input == '2':
                result = ArithmeticFunctions.sub_func(num1, num2)
                print("The result of subtraction is: ", result)

        else:
            break  # Exit the loop if user input is not 1 or 2

if __name__ == "__main__":
    main()
