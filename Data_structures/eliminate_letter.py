#!/usr/bin/env python3

def no_c(my_string):
    new_string = "" 
    for letter in my_string:
        if letter != 'c'and letter != 'C':
            new_string += letter
    return new_string
            


print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))