#!/usr/bin/python3
# Consider the code snippet below:

list_1 = [2**x for x in range(5)]            # line 1
# [1, 2, 4, 8, 16] 
list_2 = list(map(lambda x: x//2, list_1))
print(list_2)
list_2 = list(filter(lambda x: x%2, list_1))
print(list_2)
list_2 = list(map(lambda x: x/2, list_1))
print(list_2)
list_2 = list(filter(lambda x: x//2, list_1))
print(list_2)

# filter - filters the list (doesn't apply the function) and returns the same list filtered
# map will map the function and return a new list

# Which of the code snippet below can you use as a replacement for line 2 to get the following output:
# [0, 1, 2, 4, 8]

# Explanation:
# This question is a classic use case to modify a list using a lambda function and the map() or filter() function.
# First, let's see what list_1 looks like : it's a list comprehension built applying operation 2**x  for x in 
# sequence 0, 1, 2, 3, 4 (range (5)) - in other words, list_1 = [1, 2, 4, 8, 16]  (** is the exponentiation operator).
# The  map() function applies the function passed by its first argument to all its second argument's elements, 
# and returns an iterator delivering all subsequent function results.
# The filter() function filters its second argument using its first argument as the filter condition for each 
# elements of its second argument. The elements which return True from the filter condition are kept while the 
# others are rejected. The function returns an iterator.
# For both functions map() and filter(), the resulting iterator can be converted to a list, tuple , etc...
# The list() function converts its argument into a list.

# Now, let's review each of the suggested answers:
# list_2 = list(map(lambda x: x//2, list_1))  -> this will apply x//2 to each element of list_1 and return a 
# list - in other words, this will return : [0, 1, 2, 4, 8] (remember that 1//2 returns 0) - this is the correct answer
# list_2 = list(filter(lambda x: x%2, list_1)) -> this will filter list_1 based on condition x%2 applied to 
# each element of list_1 and return a list - in other words, this will return : [1] (all elements of list_1, 
# except for 1 are even numbers - for those even numbers x : x%2 returns 0 which translates to False - 1%2 returns 1 which translates to True).
# list_2 = list(map(lambda x: x/2, list_1)) -> this will apply x/2 to each element of list_1 and return a 
# list - in other words, this will return : [0.5, 1.0, 2.0, 4.0, 8.0] (remember that operator / always returns a float)
# list_2 = list(filter(lambda x: x//2, list_1)) -> this will filter list_1 based on condition x//2 applied  
# to each element of list_1 and return a list - in other words, this will return : [2, 4, 8, 16] 
# (1//2 returns 0 which translates to False - so only element 1 is filtered out).