#!/usr/bin/python3
# What is the expected output of the following snippet ?

my_list1=list('Skywalker') # ['S', 'k', 'y', 'w', 'a', 'l', 'k', 'e', 'r']
my_list2=list('Vader') # ['V', 'a', 'd', 'e', 'r']
my_list3=list(filter(lambda x: x not in my_list2, my_list1))
print(my_list3)


# Knowledge Area : Miscellaneous

# Topic : lambda functions, filter(), converting generator objects into lists using the list() function

# Explanation:

# The list() constructor returns a list. When used with a string, list() will return a list of all characters of this string.

# So, list('Skywalker')  returns :

# ['S', 'k', 'y', 'w', 'a', 'l', 'k', 'e', 'r']
# and list('Vader')  returns:

# ['V', 'a', 'd', 'e', 'r']
# The third list (my_list3) is created using a list comprehension. This list comprehension uses the filter() function to generate the list. 
# This function filters its second argument while being guided by directions flowing 
# from the function specified as the first argument. The elements which return True from the function pass the filter - the others are rejected.

# In this case, the function used for the filter is a lambda function.

# In the above code, the filter() function will simply filter my_list1 with those characters that are NOT in my_list2, i.e. : 'S', 'k', 'y', 'w', 'l', 'k' .

# And the resulting list is : ['S', 'k', 'y', 'w', 'l', 'k']