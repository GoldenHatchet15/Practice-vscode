#!/usr/bin/env python3

''' 
Task: Love Calculator

You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs.

Then check for the number of times the letters in the word LOVE occurs.

Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is *z*."
e.g.

name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53." 
'''

print("The Love Calculator is calculating your score...")
name1 = input("First lover name: ") # What is your name?
name2 = input("Second lover name: ") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = (name1 + name2).lower()

# Count occurrences for TRUE
true_count = sum(combined_names.count(letter) for letter in "true")

# Count occurrences for LOVE
love_count = sum(combined_names.count(letter) for letter in "love")

# Combine counts to create the love score
love_score = int(str(true_count) + str(love_count))

# Determine the message based on the love score
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
