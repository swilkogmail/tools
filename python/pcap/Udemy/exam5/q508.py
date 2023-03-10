#!/usr/bin/python3
# Consider the following object:

my_list = (1, 5, 10, 19, 20)

# Which of the code snippets below would produce a new object like the following?

# (1, 5, 10, 19)

# Explanation:

# The my_list object is NOT a list, it is a tuple. The big difference is that, unlike 
# lists, tuples are immutable. A tuple cannot be modified in place.

# The del function , pop() and remove() methods works fine on lists but NOT on tuples ! 
# They are not valid for tuples and will raise an exception.

# So, none of the above is the correct answer.

# Try it yourself:

my_list = (1, 5, 10, 19, 20)    # this is a tuple
#del my_list[-1]                # raise an exception
 
my_list = (1, 5, 10, 19, 20)
#my_list.pop()                  # raise an exception
 
my_list = (1, 5, 10, 19, 20)
#my_list.remove(20)             # raise an exception
 
my_list = [1, 5, 10, 19, 20]    # this is a list
del my_list[-1]
print(my_list)                  # [1, 5, 10, 19]
 
my_list = [1, 5, 10, 19, 20]
my_list.pop()
print(my_list)                  #  [1, 5, 10, 19]
 
my_list = [1, 5, 10, 19, 20]
my_list.remove(20)
print(my_list)                  #  [1, 5, 10, 19]