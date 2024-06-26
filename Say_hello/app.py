#!/usr/bin/env python3
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'Holberton'  # Add a secret key for session management

@app.route('/hello')
def index():
    flash('What is your name?')
    return render_template('index.html')

@app.route('/greet', methods=['POST', 'GET'])
def greet():
    flash('Hello ' + str(request.form['name_input']) + ", great to see you!")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
