#!/usr/bin/python3
# You need to create a generator func() that will be used to create a list of 
# integers between 0 and 100 (included) that are  multiple of 6.

# Which code snippet will meet these requirements ?

# Explanation:

# The yield keyword allows to turn a function into a generator. The answer using 
# return in the above func() are functions and not generators. A generator cannot be 
# invoked explicitly - it needs to be used in conjunction with a function, loop, etc...

# To create a list object out of a generator, the list() function can be used or a list comprehension (among other methods).

def func(x):
    for i in range(x+1):
        if i%6 == 0:
            yield i
list1 = [x for x in func(100)]    # list comprehension
 
print(list1)
#[0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]
 
list2 = list(func(100))    # using function list()
 
print(list2)
#[0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]