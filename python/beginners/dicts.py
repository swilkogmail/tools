#!/usr/bin/python3
my_dict = {'steve':48, 'dave':60, 'nick':41}
print(my_dict)
print(my_dict['steve'])
# add values
my_dict['Laurent'] = 50
print(my_dict)
# changes values
my_dict['Laurent'] = 55
print(my_dict)
# remove values
del my_dict['Laurent']
print(my_dict)
# in operations
print('laurent' in my_dict)
print('steve' in my_dict)
# creating dictionaries
weights = dict(steve=78, dave=90, nick=80)
print(weights)
colours = dict([('steve','red'), ('dave','blue'), ('nick','green')])
print(colours)
#
# dictionary methods
#
print(my_dict.keys()) # returns a list of keys
print(my_dict.values()) # returns a list of values
# both these need casting to a list though
print(list(my_dict.keys()))
print(my_dict.items()) # returns a list of values
print(list(my_dict.items())) # returns a list of tuples
