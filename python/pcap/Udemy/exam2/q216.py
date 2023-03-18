#!/usr/bin/python3
my_tuple = ('Luke', 'Leia', 'Han', 'Darth')
my_v = [my_tuple[i] for i in range(1,4)]  # is a list comprehension and results in the following list:
for x in my_v:
    print(x, end=' ')


# Explanation:
# A tuple is an immutable sequence type !
# So del my_tuple[0]   is not permitted and will raise an exception.

# ['Leia', 'Han', 'Darth']
# which when printed element by element (with the optional end=' ' parameter within the print() function) gives :
# Leia Han Darth
# my_tuple[1:3] (slicing) returns : ('Leia', 'Han')  (new tuple with only the elements with index 1 and 2 from 
# the original tuple - remember element with index 3 is not included in the slice).
# Finally my_tuple.pop(0)  will raise an exception since there is no such method with tuples (it does work with lists).