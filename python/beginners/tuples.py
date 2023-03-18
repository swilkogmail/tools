#!/usr/bin/python3
point = (2.0, 3.0) # this is immutable
# when you initialize a tuple you have mto have aty least one column as otherwise it
# thinks you're trying to do maths, i.e. a one item tuple need to needs to be declared as
point_3d = point + (4.0,)
print(point_3d)
# when using tuples vs list
# tuple:
# when you know the length of the list
my_list = [1,2,3]
my_tuple = (my_list, 1)
print(my_tuple)
other_list = [1,2,my_tuple]
print(other_list)
my_list.append(1)
print(my_tuple)
print(other_list)