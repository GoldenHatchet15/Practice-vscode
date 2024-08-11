#!/usr/bin/env python3

# This program takes a paragraph as input and prints each word in the paragraph with a number and also prints the total number of words in the paragraph.
usr = input("Paste Paragraph here: ")
splitted = usr.split()
arguments = len(splitted)

for index, item in enumerate(splitted, start = 1):
        print(f"{index}: {item}")

print(f"Total Words: {arguments}")