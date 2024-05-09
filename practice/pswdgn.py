#!/usr/bin/python3
import random
import string

def generate_password(length=9):
    # Characters to choose from
    char_set = string.ascii_letters + string.digits + string.punctuation

    # Generate random password
    password = ''.join(random.choice(char_set) for _ in range(length))

    return password

# Generate and print the password
print(generate_password())
