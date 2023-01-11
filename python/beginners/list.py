#!/usr/bin/python3
my_list = [1,2,"hello",4,5.2]

print(my_list[2])

print(len(my_list))
print(my_list[0::2])

# lists can be modified in place
my_list[0] = 'a'
print(my_list)
print (my_list + ['more', 'values'])
print(my_list)
my_list += ['more', 'values']
print(my_list)

# reassigning items byv slicing
5.04