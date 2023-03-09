#!/usr/bin/python3
# What is the expected output of the following code?

List = (1, 2, 4, 8)
List = List[1:-2] # List[start:end] is slicing the tuple from start index (included) to end index (excluded)
print(List) # In this case list[1:-2] returns tuple (2,)
List = list(List)
print(List)

# Explanation:

# Variable List is a tuple.



# So, List[1:-2] returns a tuple that includes all values from index 1 included (i.e. 2nd value since index starts at 0) 
# to the 2nd to last value (excluded).

# In this case list[1:-2] returns tuple (2,)

# The list() function creates a list object from an iterable (tuple, sequence, etc..).

# So : list(List)  returns a list from tuple (2,) which is [2]