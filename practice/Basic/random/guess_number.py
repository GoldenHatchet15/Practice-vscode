#!/usr/bin/env python3

from Basic.random.random_number import RandomNumber

def main(): 
    while True:
        try:
            usr_input = int(input("Enter a number between 1 and 5: "))
            if usr_input < 1 or usr_input > 5:
                print("Invalid input, try again")
        
            elif usr_input == RandomNumber.random_number():
                print("You guessed the right number!")
                break

        except ValueError:
            print("Invalid input, try again")

if __name__ == "__main__":
    main()
