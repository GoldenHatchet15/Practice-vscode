#!/usr/bin/env python3

# create a tuple of numbers from 1 to 9
b = tuple(m for m in range(10) if m > 0)
print(b)

#list inside tuple
x = (m**2 for m in range(10) if m >= 1)
print(tuple(x))

#deletes an element in the list inside the tuple
x = ([1,2,3], [4,5,6], [7,8,9])
del (x[1][1])
print(x)