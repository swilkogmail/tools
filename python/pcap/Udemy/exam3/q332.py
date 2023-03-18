#!/usr/bin/python3
# Consider the code snippet below:

list_1 = ['France','USA$','Canada!','Italy2','Mexico']   # line 1
# insert code here                                       # line 2
print(list_2)


# Which of the code snippet below can you use as a replacement for line 2 to get the following output:

# ['France','Mexico']

# Explanation:

# This question is a classic use case to modify a list using a lambda function and the map() or filter() function.

# The  map() function applies the function passed by its first argument to all its second argument's elements, 
# and returns an iterator delivering all subsequent function results.

# The filter() function filters its second argument using its first argument as the filter condition for 
# each elements of its second argument. The elements which return True from the filter condition are kept 
# while the others are rejected. The function returns an iterator.

# For both functions map() and filter(), the resulting iterator can be converted to a list, tuple , etc...

# The list() function converts its argument into a list.


# Now, let's review each of the suggested answers:

# --> list_2 = list(map(lambda x: x.isalnum(), list_1))  :  
#   this will apply x.isalnum() to each element of list_1 and return a list - 
#   in other words, this will return : [True, False, False, True, True] (isalnum() 
#   returns True if string consists only of letters and digits, and returns False otherwise).

# --> list_2 = list(filter(lambda x: x[-1].isalpha(), list_1))  :  
#   this will filter list_1 based on condition x[-1].isalpha() applied to each element 
#   of list_1 and return a list - in other words, this will return : ['France','Mexico'] 
#   (only those two elements have their last character as a letter - as a reminder, isalpha() 
#   returns True if string consists only of letters, and returns False otherwise). This is the correct answer.

# --> list_2 = list(map(lambda x: x.isalpha(), list_1))  :   
#   this will apply x.isalpha() to each element of list_1 and return a list - in other words, this will return : [True, False, False, False, True].

# --> list_2 = list(filter(lambda x: x[-1].isalnum(), list_1))  
#   : this will filter list_1 based on condition x[-1].isalnum() applied to each element 
# of list_1 and return a list - in other words, this will return : ['France', 'Italy2', 'Mexico'] 
# (only those three elements have their last character as a letter or digits).