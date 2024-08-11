#!/usr/bin/env python3

# Print the sum of two numbers with two decimal places
def addition(x,y):
    return x + y
    
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

result=addition(num1,num2)

print(f"Result: {result:.2f}")