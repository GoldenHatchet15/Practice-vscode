#!/usr/bin/env python3

from flask import Flask, request, render_template
from fractions import Fraction
import re

app = Flask(__name__)

def parse_input(expression):
    # Use a regular expression to extract numbers and the operator
    match = re.match(r'^\s*(\S+)\s*([\+\-\*/])\s*(\S+)\s*$', expression)
    if match:
        x_str, operator, y_str = match.groups()
        x = parse_number(x_str)
        y = parse_number(y_str)
        return x, operator, y
    else:
        raise ValueError("Invalid expression format. Please enter in the format 'a + b'.")

def parse_number(number_str):
    try:
        # Try to parse as a float
        return float(number_str)
    except ValueError:
        # If it fails, parse as a fraction
        return Fraction(number_str)

def calculate(expression):
    try:
        x, operator, y = parse_input(expression)
        if operator == '+': # Addition
            result = x + y 
        elif operator == '-': # Subtraction
            result = x - y
        elif operator == '*': # Multiplication
            result = x * y
        elif operator == '/': # Division
            result = x / y
        return f"{result}"
    except Exception as e:
        return str(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        expression = request.form['expression']
        result = calculate(expression)
        return render_template('index.html', result=result)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
