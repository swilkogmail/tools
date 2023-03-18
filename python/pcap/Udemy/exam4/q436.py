#!/usr/bin/python3
# Consider the code snippet below:



list_1 = [x for x in 'Abc#$%123']           # line 1
# insert code here                          # line 2
print(list_2)                               # line 3


# Which code snippet below can you insert (in line 2) to get the following output:
# ['A', 'b', 'c']

# Explanation:

# list_1  is a list comprehension built by extracting each character of the string 'Abc#$%123' , i.e :

# ['A', 'b', 'c', '#', '$', '%', '1', '2', '3']

# The  map() function applies the function passed by its first argument to all its second argument's 
# elements, and returns an iterator delivering all subsequent function results.

# The filter() function filters its second argument using its first argument as the filter 
# condition for each elements of its second argument. The elements which return True from the 
# filter condition are kept while the others are rejected. The function returns an iterator.

# For both functions map() and filter(), the resulting iterator can be converted to a list, tuple , etc...

# The list() function converts its argument into a list.

# Now, let's review the suggested answers:

# --> because the resulting list has only 3 elements (and the initial list had 9 elements), we can be 
# sure that one of the answer uses the filter() function. So, we can discard all answers with the map() function.

# --> isalpha() is a string method that returns True if the string is only composed of characters (a..z, A..Z), and 
# False otherwise. Whereas isalnum()  is a string method that returns True if the string is only composed of alpha-numeric characters (0..9, a..z, A..Z), and False otherwise.

# Here, because the resulting list is a list of characters only, the isalpha() method was used as a filter and 
# consequently the correct answer is :

# list_2 = list(filter(lambda x: x.isalpha(), list_1))