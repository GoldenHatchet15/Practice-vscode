#!/usr/bin/env python3

#dictionary of food and their weights
x = {'pork': 25, 'beef': 33, 'chicken': 22, 'fish': 17}
print(x)

#dictionary of food and their weights different syntax
x =dict([('pork', 25), ('beef', 33), ('chicken', 22), ('fish', 17)])
print(x)

#dictionary of food and their weights different syntax
x = dict(pork=25, beef=33, chicken=22, fish=17)
print(x)


#change value of pork to 30
x['pork'] = 30
print(x)
 
#delete beef from the dictionary
del x['beef']
print(x)

#get length of dictionary
print(len(x))

#delete  all elements in the dictionary
x.clear()

#delete the dictionary
del x

#acces key and value of dictionary
x = {'pork': 25, 'beef': 33, 'chicken': 22, 'fish': 17}
for key, value in x.items():
    print(f"{key}: {value}")

