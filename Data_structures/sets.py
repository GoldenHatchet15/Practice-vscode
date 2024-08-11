#!/usr/bin/env python3

#empty set
b =set()

#set of numbers from 1 to 9
x = {1, 2, 3, 4, 5, 6, 7, 8, 9}

#create a set of numbers from 1 to 9
b = {m for m in range(10) if m > 0}
print(b)

#creates a set of multiples of 3
x = {3*j for j in range(10) if j > 5}
print(x)
