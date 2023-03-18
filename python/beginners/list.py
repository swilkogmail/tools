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

# reassigning items by slicing
my_list[2:3] = ['goodbye']
print(my_list)
# removing from the list
my_list[2:3] = []
print(my_list)
# or to use del statement (without passing the index it will delete the list)
del my_list[0]
print(my_list)

## LIST FUNCTIONS AND METHODS
##
my_list = [1,2,3,4,5]
print(my_list)
my_list.append(6)
print(my_list)
my_list.insert(0,'a')
print(my_list)
my_list.index('a')
print(my_list.index('a'))
if 4 in my_list: # returns true
    print('true')
if 10 in my_list: # returns false
    print('true')
# print(sorted(my_list)) # not able to sort between integer and string
my_list = [1,4,3,2,5]
print(sorted(my_list))
print(reversed(my_list)) # this returns a reversed iterator object (not helpful so need to assign it to a list)
my_list = list(reversed(my_list))
print(my_list)
my_list = list(reversed(sorted(my_list)))
print(my_list)

# matrices and cubes
my_matrix = [[1,2,3],
             [4,5,6]]
print(my_matrix)
row_count = len(my_matrix) # this will return the number of rows
column_count = len(my_matrix[0]) # this will return the number of rows
print(row_count)
print(column_count)
print(my_matrix[0][1])
print(my_matrix[1][1])

# squares (a 2 x 2 matrix)
# a cube is a matrix that has the same number of columns and rows