#!/usr/bin/env python3

#create a list of numbers from 1 to 9
b = [m for m in range (10) if m > 0]
print(b)

#creates a list of squares of numbers from 1 to 9
x =[m**2 for m in range (10)if m >= 1]

print(x)

#deletes the 3rd element in the list
del x[2]
print(f"3rd element deleted: {x}")

#append list 90 to list x
x.append(90)
print(f"add 90 to list: {x}") 

#extend list x with list b and sort the list including repeated elements
x.extend(b)
x.sort()
print(f"extend and sort: {x}")

#insert 100 at index 5
x.insert(5, 100)
print(x)

x.insert(6, ['a', 'b', 'c'])
print(x)

#pop the last element in the list
print(f"pop {x.pop(), x}")
#print(x)

#remove the first instance of 1 in the list
x.remove(1)
print(x)

#reverse the list
x.reverse()
print(x)

#sort the list in ascending order
x.sort()
print(x)

#sort the list in descending order
x.sort(reverse=True)
print(x)