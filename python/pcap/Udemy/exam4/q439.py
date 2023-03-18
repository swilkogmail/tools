#!/usr/bin/python3
# Consider the list below :
list1 = [6, 2, 8, 56, 33, 78, 42, 98]

# Which code snippet below will filter the above list with numbers multiple of 3 only?

# list2 = list(filter(lambda x : x%3==0,    ))
# (Correct)

# list2 = list(filter(lambda : x%3==0, list1))

# list2 = list(filter(list1, lambda x : x%3==0))

# list2 = filter(lambda x : x%3==0, list1)


# Explanation:
# The filter() function filters its second argument using its first argument as the filter 
# condition for each elements of its second argument. The elements which return 
# True from the filter condition are kept while the others are rejected. The 
# function returns an iterator. The resulting iterator can be converted to a list, tuple , etc...
# The list() function converts its argument into a list.
# Here, lambda function lambda x : x%3==0 is being used as the filter condition in the 
# filter() function. Any elements from list1 where x%3==0 are kept while others are rejected.